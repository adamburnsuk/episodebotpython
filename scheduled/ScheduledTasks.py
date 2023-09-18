import schedule
import time
from datetime import datetime
import shutil
import eyed3

# Scheduled Task
def add_podcast_episode_to_db():
    # Your logic here
    pass

# Schedule the task to run every hour
schedule.every(60).minutes.do(add_podcast_episode_to_db)

# Generate Filename
def generate_filename(show, episode):
    date_format = "%y%m%d"
    str_date = episode['publish_date'].strftime(date_format)
    
    episode_name = show['show_name'].replace("[^a-zA-Z0-9_]", "").lower() + str_date
    
    if 'mpeg' in episode['mime_type']:
        episode_name += ".mp3"
    elif 'm4a' in episode['mime_type']:
        episode_name += ".m4a"
        
    return episode_name

# Move File
def move_file(show, episode):
    src = f"/data/pride48/podcasts/tmp/{generate_filename(show, episode)}"
    dst = f"/data/pride48/podcasts/General_Rotation/{generate_filename(show, episode)}"
    shutil.move(src, dst)

# Tag File
def tag_file(show, episode):
    file_path = f"/data/pride48/podcasts/tmp/{generate_filename(show, episode)}"
    audio_file = eyed3.load(file_path)

    # Set Title to Show Name + Publish Date
    date_format = "%m/%d/%Y"
    str_title_date = episode['publish_date'].strftime(date_format)
    audio_file.tag.title = f"{show['show_name']} {str_title_date}"

    # Set Artist to Show Name
    audio_file.tag.artist = show['show_name']

    # Set Album Name to Show Name
    audio_file.tag.album = show['show_name']

    # Set artwork
    with open("/data/pride48/podcasts/tmp/geekygaylogo1400.png", "rb") as img:
        audio_file.tag.images.set(3, img.read(), "image/png")
        
    audio_file.tag.save()

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)


