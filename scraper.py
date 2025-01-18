from requests import get
from pathlib import Path
from bs4 import BeautifulSoup, Tag
from dataclasses import dataclass
from table2ascii import table2ascii as t2a

PAGE_URL="https://eldenring.wiki.fextralife.com/Bosses"
PAGE_CACHE_DIR=Path("tmp")

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


def _get_html() -> BeautifulSoup:
    PAGE_CACHE_DIR.mkdir(exist_ok=True)
    _html_cache = Path(PAGE_CACHE_DIR, "boss-list.html")
    if not _html_cache.exists():
        _html_cache.write_bytes(get(PAGE_URL).content)
    html = _html_cache.read_text()
    return BeautifulSoup(html, "html.parser")

def _parse_bosses(boss_container: Tag) -> list[Boss]:
    bosses: list[Boss] = []
    for location_container in boss_container.find_all("div", class_="col-sm-4"):
        if not isinstance(location_container, Tag):
            raise Exception(location_container.text)
        location = location_container.find("h4").find("a", class_="wiki_link").text
        print(location_container, "\n")
        for boss_bullet_point in location_container.find_all("li"):
            boss_link = boss_bullet_point.find("a", class_="wiki_link")
            bosses.append(Boss(name=boss_link.text, location=location))
    return bosses

def _sort_by_location(bosses: list[Boss]) -> list[Boss]:
    bosses = list(bosses)
    bosses.sort(key = lambda boss: (boss.location, boss.name))
    return bosses

def _format_as_table(bosses: list[Boss]) -> str:
    output = t2a(
        header=["Location", "Name"],
        body=[[boss.location, boss.name] for boss in bosses],
        first_col_heading=True
    )
    return output

boss_container = _get_html()

bosses = _sort_by_location(_parse_bosses(boss_container))
# divisions = len(_format_as_table(bosses)) // 1900
divisions = 3
count = len(bosses) // divisions
for division in range(0, divisions):
    start = division * count
    max = (division + 1) * count if division + 1 < divisions else len(bosses)
    print(_format_as_table(bosses[division * count : max]))
    print()