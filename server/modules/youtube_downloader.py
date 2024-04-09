from pytube import YouTube
import shutil
import os
from os import walk
import re
from services.validators import is_valid_youtube_url


def download_source(link):
    """Function for download video from youtube"""

    if is_valid_youtube_url(link):
        url = YouTube(link)
        try:
            video = url.streams.filter(
                progressive=True, file_extension="mp4"
            ).get_highest_resolution()
            video_title = re.sub("[^a-zA-Z0-9 \n\.]", "", video.title)
            video_thumbnail = url.thumbnail_url

        except Exception:
            return (
                {"error": "Video is age restricted, or not available!"},
                401,
                {"Content-Type": "application/json"},
            )

    else:
        return (
            {"error": "Please enter valid YouTube video URL!"},
            400,
            {"Content-Type": "application/json"},
        )

    try:
        # Download the video
        video.download(
            output_path="youtube",
            filename=f"{video_title}.mp4",
            skip_existing=True,
            max_retries=0,
        )

        # Move the downloaded file to the client folder
        download_location = os.path.join(os.getcwd(), "youtube")
        source_folder = download_location + "\\" + video_title + ".mp4"
        altered_path = os.getcwd().replace("server", "client")
        move_folder = altered_path + "\static\youtube\\" + video_title + ".mp4"

        shutil.move(source_folder, move_folder)

        return {"path": move_folder, "file": video_title, "thumbnail": video_thumbnail}

    except Exception:
        return (
            {"error": "Something went wrong. Please try again!"},
            401,
            {"Content-Type": "application/json"},
        )


def list_videos():
    """List downloaded videos"""
    altered_path = os.getcwd().replace("server", "client")
    videos_folder = altered_path + "\static\youtube\\"
    video_files = []
    for dirpath, dirnames, filenames in walk(videos_folder):
        video_files.extend(filenames)
        break

    return video_files
