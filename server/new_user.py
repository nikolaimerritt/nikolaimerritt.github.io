from models import User, Area, Boss


def add_areas(user: User):
    area_limgrave = Area(name="Limgrave")
    area_limgrave.bosses.append(Boss(name="Beastman of Farum Azula", defeated=False))
    area_limgrave.bosses.append(Boss(name="Bell Bearing Hunter", defeated=False))
    area_limgrave.bosses.append(Boss(name="Black Knife Assassin", defeated=False))
    area_limgrave.bosses.append(Boss(name="Bloodhound Knight Darriwil", defeated=False))
    area_limgrave.bosses.append(Boss(name="Crucible Knight", defeated=False))
    area_limgrave.bosses.append(Boss(name="Deathbird", defeated=False))
    area_limgrave.bosses.append(Boss(name="Demi-Human Chief", defeated=False))
    area_limgrave.bosses.append(
        Boss(name="Erdtree Burial Watchdog (Stormfoot Catacombs)", defeated=False)
    )
    area_limgrave.bosses.append(Boss(name="Flying Dragon Agheel", defeated=False))
    area_limgrave.bosses.append(Boss(name="Godrick the Grafted", defeated=False))
    area_limgrave.bosses.append(Boss(name="Grafted Scion", defeated=False))
    area_limgrave.bosses.append(Boss(name="Grave Warden Duelist", defeated=False))
    area_limgrave.bosses.append(Boss(name="Guardian Golem", defeated=False))
    area_limgrave.bosses.append(Boss(name="Mad Pumpkin Head", defeated=False))
    area_limgrave.bosses.append(Boss(name="Margit, the Fell Omen", defeated=False))
    area_limgrave.bosses.append(Boss(name="Night's Cavalry", defeated=False))
    area_limgrave.bosses.append(Boss(name="Patches", defeated=False))
    area_limgrave.bosses.append(Boss(name="Soldier of Godrick", defeated=False))
    area_limgrave.bosses.append(Boss(name="Stonedigger Troll", defeated=False))
    area_limgrave.bosses.append(Boss(name="Tibia Mariner", defeated=False))
    area_limgrave.bosses.append(Boss(name="Tree Sentinel", defeated=False))
    area_limgrave.bosses.append(Boss(name="Ulcerated Tree Spirit", defeated=False))
    user.areas.append(area_limgrave)

    area_weeping_peninsula = Area(name="Weeping Peninsula")
    area_weeping_peninsula.bosses.append(
        Boss(name="Ancient Hero of Zamor", defeated=False)
    )
    area_weeping_peninsula.bosses.append(Boss(name="Cemetery Shade", defeated=False))
    area_weeping_peninsula.bosses.append(Boss(name="Deathbird", defeated=False))
    area_weeping_peninsula.bosses.append(Boss(name="Erdtree Avatar", defeated=False))
    area_weeping_peninsula.bosses.append(
        Boss(name="Erdtree Burial Watchdog (Impaler's Catacombs)", defeated=False)
    )
    area_weeping_peninsula.bosses.append(
        Boss(name="Leonine Misbegotten", defeated=False)
    )
    area_weeping_peninsula.bosses.append(
        Boss(name="Miranda the Blighted Bloom", defeated=False)
    )
    area_weeping_peninsula.bosses.append(Boss(name="Night's Cavalry", defeated=False))
    area_weeping_peninsula.bosses.append(Boss(name="Runebear", defeated=False))
    area_weeping_peninsula.bosses.append(Boss(name="Scaly Misbegotten", defeated=False))
    user.areas.append(area_weeping_peninsula)

    area_liurnia_of_the_lakes = Area(name="Liurnia of the Lakes")
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Adan, Thief of Fire", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Alecto, Black Knife Ringleader", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Bell Bearing Hunter", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Black Knife Assassin", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Bloodhound Knight", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Bols, Carian Knight", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(Boss(name="Cemetery Shade", defeated=False))
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Cleanrot Knight", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(Boss(name="Crystalian", defeated=False))
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Crystalian Spear & Crystalian Staff (Duo)", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Death Rite Bird", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(Boss(name="Deathbird", defeated=False))
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Erdtree Avatar (Liurnia Northeast)", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Erdtree Avatar (Liurnia Southwest)", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Erdtree Burial Watchdog", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Glintstone Dragon Adula", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Glintstone Dragon Smarag", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Magma Wyrm Makar", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Night's Cavalry (Liurnia North)", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Night's Cavalry (Liurnia South)", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(Boss(name="Omenkiller", defeated=False))
    area_liurnia_of_the_lakes.bosses.append(Boss(name="Onyx Lord", defeated=False))
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Red Wolf of Radagon", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Rennala, Queen of the Full Moon", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Royal Knight Loretta", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(Boss(name="Royal Revenant", defeated=False))
    area_liurnia_of_the_lakes.bosses.append(
        Boss(name="Spirit-Caller Snail", defeated=False)
    )
    area_liurnia_of_the_lakes.bosses.append(Boss(name="Tibia Mariner", defeated=False))
    user.areas.append(area_liurnia_of_the_lakes)

    area_ainsel_river = Area(name="Ainsel River")
    area_ainsel_river.bosses.append(
        Boss(name="Dragonkin Soldier of Nokstella", defeated=False)
    )
    user.areas.append(area_ainsel_river)

    area_siofra_river = Area(name="Siofra River")
    area_siofra_river.bosses.append(Boss(name="Ancestor Spirit", defeated=False))
    area_siofra_river.bosses.append(Boss(name="Dragonkin Soldier", defeated=False))
    user.areas.append(area_siofra_river)

    area_caelid = Area(name="Caelid")
    area_caelid.bosses.append(Boss(name="Cemetery Shade", defeated=False))
    area_caelid.bosses.append(Boss(name="Commander O'Neil", defeated=False))
    area_caelid.bosses.append(
        Boss(name="Crucible Knight & Misbegotten Warrior", defeated=False)
    )
    area_caelid.bosses.append(Boss(name="Death Rite Bird", defeated=False))
    area_caelid.bosses.append(Boss(name="Decaying Ekzykes", defeated=False))
    area_caelid.bosses.append(
        Boss(name="Erdtree Burial Watchdog (Duo)", defeated=False)
    )
    area_caelid.bosses.append(Boss(name="Fallingstar Beast", defeated=False))
    area_caelid.bosses.append(Boss(name="Frenzied Duelist", defeated=False))
    area_caelid.bosses.append(Boss(name="Mad Pumpkin Heads", defeated=False))
    area_caelid.bosses.append(Boss(name="Magma Wyrm", defeated=False))
    area_caelid.bosses.append(Boss(name="Night's Cavalry", defeated=False))
    area_caelid.bosses.append(Boss(name="Nox Swordstress & Nox Priest", defeated=False))
    area_caelid.bosses.append(Boss(name="Putrid Avatar", defeated=False))
    area_caelid.bosses.append(Boss(name="Starscourge Radahn", defeated=False))
    user.areas.append(area_caelid)

    area_altus_plateau = Area(name="Altus Plateau")
    area_altus_plateau.bosses.append(
        Boss(name="Ancient Dragon Lansseax", defeated=False)
    )
    area_altus_plateau.bosses.append(Boss(name="Ancient Hero of Zamor", defeated=False))
    area_altus_plateau.bosses.append(
        Boss(name="Black Knife Assassin (Sage's Cave)", defeated=False)
    )
    area_altus_plateau.bosses.append(
        Boss(name="Black Knife Assassin (Sainted Hero's Grave)", defeated=False)
    )
    area_altus_plateau.bosses.append(
        Boss(name="Crystalian Spear & Crystalian Ringblade", defeated=False)
    )
    area_altus_plateau.bosses.append(
        Boss(name="Demi-Human Queen Gilika", defeated=False)
    )
    area_altus_plateau.bosses.append(Boss(name="Elemer of the Briar", defeated=False))
    area_altus_plateau.bosses.append(
        Boss(name="Erdtree Burial Watchdog", defeated=False)
    )
    area_altus_plateau.bosses.append(Boss(name="Fallingstar Beast", defeated=False))
    area_altus_plateau.bosses.append(Boss(name="Godefroy The Grafted", defeated=False))
    area_altus_plateau.bosses.append(Boss(name="Godskin Apostle", defeated=False))
    area_altus_plateau.bosses.append(Boss(name="Necromancer Garris", defeated=False))
    area_altus_plateau.bosses.append(Boss(name="Night's Cavalry", defeated=False))
    area_altus_plateau.bosses.append(
        Boss(name="Omenkiller & Miranda the Blighted Bloom", defeated=False)
    )
    area_altus_plateau.bosses.append(
        Boss(name="Perfumer Tricia & Misbegotten Warrior", defeated=False)
    )
    area_altus_plateau.bosses.append(Boss(name="Sanguine Noble", defeated=False))
    area_altus_plateau.bosses.append(Boss(name="Stonedigger Troll", defeated=False))
    area_altus_plateau.bosses.append(Boss(name="Tibia Mariner", defeated=False))
    area_altus_plateau.bosses.append(Boss(name="Tree Sentinel (Duo)", defeated=False))
    area_altus_plateau.bosses.append(Boss(name="Wormface", defeated=False))
    user.areas.append(area_altus_plateau)

    area_nokron__eternal_city = Area(name="Nokron, Eternal City")
    area_nokron__eternal_city.bosses.append(Boss(name="Mimic Tear", defeated=False))
    area_nokron__eternal_city.bosses.append(
        Boss(name="Regal Ancestor Spirit", defeated=False)
    )
    area_nokron__eternal_city.bosses.append(
        Boss(name="Valiant Gargoyle & Valiant Gargoyle (Twinblade)", defeated=False)
    )
    user.areas.append(area_nokron__eternal_city)

    area_deeproot_depths = Area(name="Deeproot Depths")
    area_deeproot_depths.bosses.append(
        Boss(name="Crucible Knight Siluria", defeated=False)
    )
    area_deeproot_depths.bosses.append(Boss(name="Fia's Champions", defeated=False))
    area_deeproot_depths.bosses.append(
        Boss(name="Lichdragon Fortissax", defeated=False)
    )
    user.areas.append(area_deeproot_depths)

    area_capital_outskirts = Area(name="Capital Outskirts")
    area_capital_outskirts.bosses.append(
        Boss(name="Bell Bearing Hunter", defeated=False)
    )
    area_capital_outskirts.bosses.append(
        Boss(name="Crucible Knight & Crucible Knight Ordovis", defeated=False)
    )
    area_capital_outskirts.bosses.append(Boss(name="Deathbird", defeated=False))
    area_capital_outskirts.bosses.append(
        Boss(name="Draconic Tree Sentinel", defeated=False)
    )
    area_capital_outskirts.bosses.append(Boss(name="Fell Twins", defeated=False))
    area_capital_outskirts.bosses.append(
        Boss(name="Grave Warden Duelist", defeated=False)
    )
    area_capital_outskirts.bosses.append(Boss(name="Onyx Lord", defeated=False))
    user.areas.append(area_capital_outskirts)

    area_mt__gelmir = Area(name="Mt. Gelmir")
    area_mt__gelmir.bosses.append(Boss(name="Abductor Virgins (Duo)", defeated=False))
    area_mt__gelmir.bosses.append(Boss(name="Demi-Human Queen Maggie", defeated=False))
    area_mt__gelmir.bosses.append(Boss(name="Demi-Human Queen Margot", defeated=False))
    area_mt__gelmir.bosses.append(
        Boss(name="Full-Grown Fallingstar Beast", defeated=False)
    )
    area_mt__gelmir.bosses.append(
        Boss(name="God-Devouring Serpent / Rykard, Lord of Blasphemy", defeated=False)
    )
    area_mt__gelmir.bosses.append(Boss(name="Godskin Noble", defeated=False))
    area_mt__gelmir.bosses.append(Boss(name="Kindred of Rot (Duo)", defeated=False))
    area_mt__gelmir.bosses.append(Boss(name="Magma Wyrm (Fort Laiedd)", defeated=False))
    area_mt__gelmir.bosses.append(Boss(name="Red Wolf of the Champion", defeated=False))
    area_mt__gelmir.bosses.append(Boss(name="Ulcerated Tree Spirit", defeated=False))
    user.areas.append(area_mt__gelmir)

    area_lake_of_rot = Area(name="Lake of Rot")
    area_lake_of_rot.bosses.append(
        Boss(name="Astel, Naturalborn of the Void", defeated=False)
    )
    area_lake_of_rot.bosses.append(Boss(name="Dragonkin Soldier", defeated=False))
    user.areas.append(area_lake_of_rot)

    area_dragonbarrow = Area(name="Dragonbarrow")
    area_dragonbarrow.bosses.append(Boss(name="Battlemage Hugues", defeated=False))
    area_dragonbarrow.bosses.append(
        Boss(name="Beastman of Farum Azula (Duo)", defeated=False)
    )
    area_dragonbarrow.bosses.append(Boss(name="Bell Bearing Hunter", defeated=False))
    area_dragonbarrow.bosses.append(Boss(name="Black Blade Kindred ", defeated=False))
    area_dragonbarrow.bosses.append(Boss(name="Cleanrot Knight (Duo)", defeated=False))
    area_dragonbarrow.bosses.append(Boss(name="Flying Dragon Greyll", defeated=False))
    area_dragonbarrow.bosses.append(Boss(name="Godskin Apostle", defeated=False))
    area_dragonbarrow.bosses.append(
        Boss(name="Night's Cavalry (Dragonbarrow)", defeated=False)
    )
    area_dragonbarrow.bosses.append(Boss(name="Putrid Avatar", defeated=False))
    area_dragonbarrow.bosses.append(Boss(name="Putrid Crystalian Trio", defeated=False))
    area_dragonbarrow.bosses.append(Boss(name="Putrid Tree Spirit", defeated=False))
    user.areas.append(area_dragonbarrow)

    area_leyndell__royal_capital = Area(name="Leyndell, Royal Capital")
    area_leyndell__royal_capital.bosses.append(
        Boss(name="Esgar, Priest of Blood", defeated=False)
    )
    area_leyndell__royal_capital.bosses.append(
        Boss(name="Godfrey, First Elden Lord", defeated=False)
    )
    area_leyndell__royal_capital.bosses.append(
        Boss(name="Mohg, the Omen", defeated=False)
    )
    area_leyndell__royal_capital.bosses.append(
        Boss(name="Morgott, the Omen King", defeated=False)
    )
    user.areas.append(area_leyndell__royal_capital)

    area_forbidden_lands = Area(name="Forbidden Lands")
    area_forbidden_lands.bosses.append(Boss(name="Black Blade Kindred", defeated=False))
    area_forbidden_lands.bosses.append(Boss(name="Night's Cavalry", defeated=False))
    area_forbidden_lands.bosses.append(Boss(name="Stray Mimic Tear", defeated=False))
    user.areas.append(area_forbidden_lands)

    area_mountaintops_of_the_giants = Area(name="Mountaintops of the Giants")
    area_mountaintops_of_the_giants.bosses.append(
        Boss(name="Ancient Hero of Zamor", defeated=False)
    )
    area_mountaintops_of_the_giants.bosses.append(
        Boss(name="Borealis the Freezing Fog", defeated=False)
    )
    area_mountaintops_of_the_giants.bosses.append(
        Boss(name="Commander Niall", defeated=False)
    )
    area_mountaintops_of_the_giants.bosses.append(
        Boss(name="Death Rite Bird", defeated=False)
    )
    area_mountaintops_of_the_giants.bosses.append(
        Boss(name="Erdtree Avatar", defeated=False)
    )
    area_mountaintops_of_the_giants.bosses.append(
        Boss(name="Fire Giant", defeated=False)
    )
    area_mountaintops_of_the_giants.bosses.append(
        Boss(
            name="Godskin Apostle and Godskin Noble (Spiritcaller Snail)",
            defeated=False,
        )
    )
    area_mountaintops_of_the_giants.bosses.append(
        Boss(name="Ulcerated Tree Spirit", defeated=False)
    )
    area_mountaintops_of_the_giants.bosses.append(
        Boss(name="Vyke, Knight of the Roundtable", defeated=False)
    )
    user.areas.append(area_mountaintops_of_the_giants)

    area_consecrated_snowfield = Area(name="Consecrated Snowfield")
    area_consecrated_snowfield.bosses.append(
        Boss(name="Astel, Stars of Darkness", defeated=False)
    )
    area_consecrated_snowfield.bosses.append(
        Boss(name="Death Rite Bird", defeated=False)
    )
    area_consecrated_snowfield.bosses.append(
        Boss(name="Great Wyrm Theodorix", defeated=False)
    )
    area_consecrated_snowfield.bosses.append(
        Boss(name="Misbegotten Crusader", defeated=False)
    )
    area_consecrated_snowfield.bosses.append(
        Boss(name="Night's Cavalry (Duo)", defeated=False)
    )
    area_consecrated_snowfield.bosses.append(Boss(name="Putrid Avatar", defeated=False))
    area_consecrated_snowfield.bosses.append(
        Boss(name="Putrid Grave Warden Duelist", defeated=False)
    )
    user.areas.append(area_consecrated_snowfield)

    area_mohgwyn_palace = Area(name="Mohgwyn Palace")
    area_mohgwyn_palace.bosses.append(Boss(name="Mohg, Lord of Blood", defeated=False))
    user.areas.append(area_mohgwyn_palace)

    area_miquella_s_haligtree = Area(name="Miquella's Haligtree")
    area_miquella_s_haligtree.bosses.append(
        Boss(name="Loretta, Knight of the Haligtree", defeated=False)
    )
    area_miquella_s_haligtree.bosses.append(
        Boss(name="Malenia, Blade of Miquella", defeated=False)
    )
    user.areas.append(area_miquella_s_haligtree)

    area_crumbling_farum_azula = Area(name="Crumbling Farum Azula")
    area_crumbling_farum_azula.bosses.append(
        Boss(name="Beast Clergyman / Maliketh, the Black Blade", defeated=False)
    )
    area_crumbling_farum_azula.bosses.append(
        Boss(name="Dragonlord Placidusax", defeated=False)
    )
    area_crumbling_farum_azula.bosses.append(Boss(name="Godskin Duo", defeated=False))
    user.areas.append(area_crumbling_farum_azula)

    area_leyndell__ashen_capital = Area(name="Leyndell, Ashen Capital")
    area_leyndell__ashen_capital.bosses.append(
        Boss(name="Godfrey, First Elden Lord (Hoarah Loux)", defeated=False)
    )
    area_leyndell__ashen_capital.bosses.append(
        Boss(name="Sir Gideon Ofnir, the All-Knowing", defeated=False)
    )
    user.areas.append(area_leyndell__ashen_capital)

    area_gravesite_plain = Area(name="Gravesite Plain")
    area_gravesite_plain.bosses.append(Boss(name="Blackgaol Knight", defeated=False))
    area_gravesite_plain.bosses.append(Boss(name="Chief Bloodfiend", defeated=False))
    area_gravesite_plain.bosses.append(
        Boss(name="Demi-Human Swordmaster Onze", defeated=False)
    )
    area_gravesite_plain.bosses.append(
        Boss(name="Divine Beast Dancing Lion", defeated=False)
    )
    area_gravesite_plain.bosses.append(Boss(name="Ghostflame Dragon", defeated=False))
    area_gravesite_plain.bosses.append(Boss(name="Red Bear", defeated=False))
    area_gravesite_plain.bosses.append(
        Boss(name="Rellana Twin Moon Knight", defeated=False)
    )
    user.areas.append(area_gravesite_plain)

    area_scadu_altus = Area(name="Scadu Altus")
    area_scadu_altus.bosses.append(Boss(name="Black Knight Edredd", defeated=False))
    area_scadu_altus.bosses.append(Boss(name="Black Knight Garrew", defeated=False))
    area_scadu_altus.bosses.append(
        Boss(name="Count Ymir, Mother of Fingers", defeated=False)
    )
    area_scadu_altus.bosses.append(Boss(name="Curseblade Labirith", defeated=False))
    area_scadu_altus.bosses.append(Boss(name="Death Knight", defeated=False))
    area_scadu_altus.bosses.append(Boss(name="Dryleaf Dane", defeated=False))
    area_scadu_altus.bosses.append(Boss(name="Ghostflame Dragon", defeated=False))
    area_scadu_altus.bosses.append(Boss(name="Golden Hippopotamus", defeated=False))
    area_scadu_altus.bosses.append(Boss(name="Jori, Elder Inquisitor", defeated=False))
    area_scadu_altus.bosses.append(
        Boss(name="Messmer the Impaler + Base Serpent Messmer", defeated=False)
    )
    area_scadu_altus.bosses.append(
        Boss(name="Metyr, Mother of Fingers", defeated=False)
    )
    area_scadu_altus.bosses.append(Boss(name="Rakshasa", defeated=False))
    area_scadu_altus.bosses.append(
        Boss(name="Ralva the Great Red Bear", defeated=False)
    )
    user.areas.append(area_scadu_altus)

    area_rauh_base = Area(name="Rauh Base")
    area_rauh_base.bosses.append(Boss(name="Death Knight", defeated=False))
    area_rauh_base.bosses.append(
        Boss(name="Rugalea the Great Red Bear", defeated=False)
    )
    user.areas.append(area_rauh_base)

    area_cerulean_coast = Area(name="Cerulean Coast")
    area_cerulean_coast.bosses.append(Boss(name="Dancer of Ranah", defeated=False))
    area_cerulean_coast.bosses.append(
        Boss(name="Demi-Human Queen Marigga", defeated=False)
    )
    area_cerulean_coast.bosses.append(Boss(name="Ghostflame Dragon", defeated=False))
    area_cerulean_coast.bosses.append(Boss(name="Putrescent Knight", defeated=False))
    user.areas.append(area_cerulean_coast)

    area_charo_s_hidden_grave = Area(name="Charo's Hidden Grave")
    area_charo_s_hidden_grave.bosses.append(
        Boss(name="Death Rite Bird", defeated=False)
    )
    area_charo_s_hidden_grave.bosses.append(Boss(name="Lamenter", defeated=False))
    user.areas.append(area_charo_s_hidden_grave)

    area_scaduview = Area(name="Scaduview")
    area_scaduview.bosses.append(Boss(name="Commander Gaius", defeated=False))
    area_scaduview.bosses.append(Boss(name="Scadutree Avatar", defeated=False))
    user.areas.append(area_scaduview)

    area_hinterlands = Area(name="Hinterlands")
    area_hinterlands.bosses.append(Boss(name="Fallingstar Beast", defeated=False))
    area_hinterlands.bosses.append(Boss(name="Tree Sentinel (1)", defeated=False))
    area_hinterlands.bosses.append(Boss(name="Tree Sentinel (2)", defeated=False))
    user.areas.append(area_hinterlands)

    area_abyssal_woods = Area(name="Abyssal Woods")
    area_abyssal_woods.bosses.append(
        Boss(name="Midra Lord of Frenzied Flame", defeated=False)
    )
    user.areas.append(area_abyssal_woods)

    area_jagged_peak = Area(name="Jagged Peak")
    area_jagged_peak.bosses.append(Boss(name="Ancient Dragon Senessax", defeated=False))
    area_jagged_peak.bosses.append(Boss(name="Ancient Dragon-Man", defeated=False))
    area_jagged_peak.bosses.append(Boss(name="Bayle the Dread", defeated=False))
    area_jagged_peak.bosses.append(
        Boss(name="Jagged Peak Drake (Jagged Peak Foothills)", defeated=False)
    )
    area_jagged_peak.bosses.append(
        Boss(name="Jagged Peak Drake (Jagged Peak)", defeated=False)
    )
    user.areas.append(area_jagged_peak)

    area_ancient_ruins_of_rauh = Area(name="Ancient Ruins of Rauh")
    area_ancient_ruins_of_rauh.bosses.append(
        Boss(name="Divine Beast Dancing Lion", defeated=False)
    )
    area_ancient_ruins_of_rauh.bosses.append(
        Boss(name="Romina, Saint of the Bud", defeated=False)
    )
    user.areas.append(area_ancient_ruins_of_rauh)

    area_enir_ilim = Area(name="Enir-Ilim")
    area_enir_ilim.bosses.append(
        Boss(
            name="Promised Consort Radahn + Radahn Consort of Miquella", defeated=False
        )
    )
    user.areas.append(area_enir_ilim)

    area_elden_throne = Area(name="Elden Throne")
    area_elden_throne.bosses.append(
        Boss(name="Radagon of the Golden Order / Elden Beast", defeated=False)
    )
    user.areas.append(area_elden_throne)
