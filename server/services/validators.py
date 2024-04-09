import re


def is_valid_youtube_url(video_url):
    """Validates youtube video url"""
    validateVideoUrl = (
        r"(https?://)?(www\.)?"
        "(youtube|youtu|youtube-nocookie)\.(com|be)/"
        "(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})"
    )
    validVideoUrl = re.match(validateVideoUrl, video_url)
    if validVideoUrl:
        return True
    return False


def get_size_by_aspect_ratio(type):
    """Returns the resolution of the image"""
    size = type.split("-")[1]

    if size == "512":
        resolution = [512, 512]
    elif size == "1024":
        resolution = [1024, 1024]
    elif size == "1280":
        resolution = [1280, 720]
    elif size == "1920":
        resolution = [1920, 1080]
    else:
        resolution = [512, 512]

    return resolution
