from dataclasses import dataclass

@dataclass
class Show:
    id: int
    show_name: str
    show_logo_url: str
    website_url: str
    archived: int
    feed_url: str
    internal_rating: int
    episode_url: str
    episode_pub_date: str
    episode: Episode
