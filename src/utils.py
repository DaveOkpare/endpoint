import codecs
import csv
import json
from typing import IO, Iterator, List


def csv_decoder(csv_file: IO, encoding: str = "utf-8") -> Iterator[str]:
    """
    Decodes a CSV file from a byte stream to a sequence of Unicode strings.

    Args:
        csv_file: A file object representing a CSV file in a byte stream format.
        encoding: The character encoding used in the byte stream. Default is "utf-8".

    Returns:
        An iterator over the decoded Unicode strings in the CSV file.

    Raises:
        UnicodeDecodeError: If the byte stream cannot be decoded using the specified encoding.
    """
    decoded_lines = codecs.iterdecode(csv_file, encoding)
    return decoded_lines


def csv_serializer(csv_file: str) -> List[dict]:
    """
    Parses a CSV file and returns a list of dictionaries.

    Args:
        csv_file: A string representing the path to the CSV file.

    Returns:
        A list of dictionaries representing the rows in the CSV file, with keys
        corresponding to the column headers and values corresponding to the cell values.

    Raises:
        FileNotFoundError: If the specified file does not exist or cannot be opened.
        UnicodeDecodeError: If the CSV file cannot be decoded using the default UTF-8 encoding.
    """
    rows = []

    with open(csv_file, "rb") as file:
        decoded_line = csv_decoder(file)
        csv_reader = csv.DictReader(decoded_line)

        for row in csv_reader:
            rows.append(row)

    return rows


def array_to_string(arr: list) -> str:
    """Converts a list to a JSON-formatted string.

    Args:
        arr (list): The list to convert.

    Returns:
        str: A JSON-formatted string representation of the list.
    """
    return json.dumps(arr)


def string_to_array(json_str: str) -> list:
    """Converts a JSON-formatted string to a list.

    Args:
        json_str (str): The JSON-formatted string to convert.

    Returns:
        list: A list representation of the JSON-formatted string.
    """
    return json.loads(json_str)
