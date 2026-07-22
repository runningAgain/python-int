"""
Typehints: Vorschläge für Datentypen (Meta-Informationen)
wichtig für Editoren, Type-Checker (tool die auf CLI / Editor)

mypy ist Standard für statische Code-Analyse (Typing)
pyrefly (Meta) ist die moderne Alternative (schneller, besser)
ty (Astral) in der frühen Beta
"""

from typing import Sequence, Iterable


def open_database(host: str, port: int, password: str, name: str) -> int:
    return 1


open_database(host="localhost", port=5432, password="abc", name="db1")


def print_values(values: list | set) -> None:
    for value in values:
        print(value[:2])


values = {"a", "b", "c", "42"}
print_values(values)
