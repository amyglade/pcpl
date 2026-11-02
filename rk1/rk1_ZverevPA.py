# pcpl
from dataclasses import dataclass


# 1. Классы данных

@dataclass
class ТаблицаДанных:
    id: int
    name: str


@dataclass
class СтрокаДанных:
    id: int
    name: str
    elements_count: int
    table_id: int


@dataclass
class СтрокиТаблиц:
    row_id: int
    table_id: int


# 2. Тестовые данные

tables = [
    ТаблицаДанных(1, "Таблица студентов"),
    ТаблицаДанных(2, "Таблица преподавателей"),
    ТаблицаДанных(3, "Расписание занятий")
]

rows = [
    СтрокаДанных(1, "Строка студента", 5, 1),
    СтрокаДанных(2, "Дополнительная строка", 3, 1),
    СтрокаДанных(3, "Строка преподавателя", 4, 2),
    СтрокаДанных(4, "Строка расписания", 8, 3)
]

# Связь многие-ко-многим
rows_tables = [
    СтрокиТаблиц(1, 1),
    СтрокиТаблиц(2, 1),
    СтрокиТаблиц(3, 2),
    СтрокиТаблиц(4, 3),
    СтрокиТаблиц(1, 2)
]


# 3. Запрос № 1

print("ЗАПРОС №1")

for table in sorted(tables, key=lambda item: item.name):
    print(f"\n{table.name}:")

    linked_rows = [
        row for row in rows
        if row.table_id == table.id
    ]

    for row in linked_rows:
        print(f"  {row.name}")


# 4. Запрос № 2

print("\nЗАПРОС №2")

table_totals = [
    (
        table,
        sum(
            row.elements_count
            for row in rows
            if row.table_id == table.id
        )
    )
    for table in tables
]

for table, total in sorted(table_totals, key=lambda item: item[1]):
    print(f"{table.name}: {total} элементов")


# 5. Запрос № 3

print("\nЗАПРОС №3")

selected_tables = [
    table for table in tables
    if "таблица" in table.name.lower()
]

for table in selected_tables:
    print(f"\n{table.name}:")

    linked_rows = [
        row for link in rows_tables
        if link.table_id == table.id
        for row in rows
        if row.id == link.row_id
    ]

    for row in linked_rows:
        print(f"  {row.name}")
