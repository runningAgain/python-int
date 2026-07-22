"""
postionelle Argumente VS Keyword Argumente
"""


def fn(a, b, c):
    print(a, b, c)


def delete_hosts(host1, host2, host3):
    pass


fn(1, 2, 3)  # positionellen Argumente
delete_hosts("localhost", "db", "www.web")
delete_hosts(host2="db", host3="www.web", host1="locahlost")


def load_csv(filename, encoding):
    print(f"{filename=} hat {encoding=}")


# Reihenfolge spielt keine Rolle
load_csv(filename="data.csv", encoding="utf-8")
load_csv(encoding="utf-8", filename="data.csv")

player_stat = {
    "bilbo": {
        "life": 100,
        "power": 29,
        "weapons": {"knife", "stick"},
    },
    "gollum": {
        "life": 120,  # 140
        "power": 29,
        "weapons": set(),
    },
}
# Schreibe eine Funktion add_player_lifepoints(gollum, 20), mit keyword args!
# Übergeben werden der Spielername (gollum), lifepoints (20)
# Funktion hat keinen Rückgabewert


def add_player_lifepoints(playername, lifepoints):
    """Add lifepoints to global playerstat."""
    # für key playername soll der aktuelle lifepoint + lifepoints
    if playername in player_stat:
        # player_stat[playername]["life"] = player_stat[playername]["life"] + lifepoints
        player_stat[playername]["life"] += lifepoints


add_player_lifepoints(playername="gollum", lifepoints=20)
print(player_stat)
