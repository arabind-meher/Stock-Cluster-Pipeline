import re


def process_string(key: str):
    return (
        re.sub(r"[()\']", "", key)
        .strip()
        .lower()
        .replace(" ", "_")
        .replace("-", "_")
        .replace(".", "")
        .replace("52", "fifty_two")
    )
