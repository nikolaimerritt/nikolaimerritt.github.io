from requests import get
from pathlib import Path
from bs4 import BeautifulSoup, Tag
from dataclasses import dataclass
from table2ascii import table2ascii as t2a, Alignment
import re

PAGE_URL = "https://eldenring.wiki.fextralife.com/Bosses"
PAGE_CACHE_DIR = Path("tmp")
JAVASCRIPT_OUT_FILE = Path("bosses.js")


@dataclass
class Boss:
    name: str
    location: str

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, type(self)):
            return False
        return self.name == value.name and self.location == value.location

    def __hash__(self) -> int:
        return hash((self.name, self.location))

    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)

    def to_js(self) -> str:
        return f'{{ "name": "{self.name}", "location": "{self.location}", "defeated": false }}'


def _get_html() -> BeautifulSoup:
    PAGE_CACHE_DIR.mkdir(exist_ok=True)
    _html_cache = Path(PAGE_CACHE_DIR, "boss-list.html")
    if not _html_cache.exists():
        _html_cache.write_bytes(get(PAGE_URL).content)
    html = _html_cache.read_text()
    return BeautifulSoup(html, "html.parser")


def _remove_non_prinable(string: str) -> str:
    return re.sub(r"[^\x00-\x7f]", " ", string)


def _parse_bosses(boss_container: Tag) -> list[Boss]:
    bosses: list[Boss] = []
    for location_container in boss_container.find_all("div", class_="col-sm-4"):
        if not isinstance(location_container, Tag):
            raise Exception(location_container.text)
        location = _remove_non_prinable(
            location_container.find("h4").find("a", class_="wiki_link").text
        )
        for boss_bullet_point in location_container.find_all("li"):
            name = _remove_non_prinable(boss_bullet_point.text)
            bosses.append(Boss(name=name, location=location))
    return bosses


def _is_duplicate(boss: Boss) -> bool:
    return (
        ("mohg" in boss.name.lower() and "ashen" in boss.location.lower())
        or ("leda" in boss.name.lower())
        or ("esgar" in boss.name.lower() and "ashen" in boss.location.lower())
    )


def _sort_by_location(bosses: list[Boss]) -> list[Boss]:
    bosses = list(bosses)
    bosses.sort(key=lambda boss: (boss.location, boss.name))
    return bosses


def _format_as_table(bosses: list[Boss]) -> str:
    output = t2a(
        header=["Location", "Name"],
        body=[[boss.location, boss.name] for boss in bosses],
        first_col_heading=True,
        alignments=Alignment.LEFT,
    )
    return output


def _format_as_js(bosses: list[Boss]) -> str:
    bosses_json = "[" + ",\n".join([boss.to_js() for boss in bosses]) + "]"
    return f"const BOSSES = {bosses_json};"


boss_container = _get_html()
bosses = [
    boss
    for boss in _sort_by_location(_parse_bosses(boss_container))
    if not _is_duplicate(boss)
]
for location in set(boss.location for boss in bosses):
    print(location, len([boss for boss in bosses if boss.location == location]))

print(_format_as_table(bosses))
print(len(bosses))
JAVASCRIPT_OUT_FILE.write_text(_format_as_js(bosses))
