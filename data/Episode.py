from dataclasses import dataclass
from datetime import datetime

@dataclass
class Episode:
    episode_title: str
    publish_date: datetime
    episode_url: str
    episode_file_name: str
    mime_type: str

    def get_episode_file_name(self):
        file_name_start_position = self.episode_url.rfind("/") + 1

        if "mp3" in self.episode_url:
            file_name_end_position = self.episode_url.rfind("mp3") + 3
        elif "m4a" in self.episode_url:
            file_name_end_position = self.episode_url.rfind("m4a") + 3
        else:
            file_name_end_position = len(self.episode_url)

        self.episode_file_name = self.episode_url[file_name_start_position:file_name_end_position]
        return self.episode_file_name
