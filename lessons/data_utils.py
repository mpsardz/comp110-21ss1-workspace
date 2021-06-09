"""Data utility functions. """
from csv import DictReader

def read_csv_rows(path: str) -> list[dict[str, str]]:
    """Read a CSV file and return a list of its rows."""
    file_handle = open(path, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    table: list[dict[str, str]] = []
    for row in csv_reader:
        table.append(row)
    return table

def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Return a column's values."""
    values: list[str] = []
    for row in table:
        values.append(row[column])
    return values

def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Convert a table of rows to a table of columns."""
    result: dict[str, list[str]] = {}
    keys = table[0].keys()
    for key in keys:
        result[key] = column_values(table, key)
    return result

table = read_csv_rows("data/weather.csv")
#print(table)
dates = column_values(table, "date")
print(dates)
high = column_values(table, "high")
print(high)

