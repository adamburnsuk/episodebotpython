from dataclasses import dataclass

@dataclass
class Podcast:
    id: int
    name: str
    url: str
    file_name: str
    date: str
