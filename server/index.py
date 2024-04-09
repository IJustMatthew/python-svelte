from flask import Flask, request
from flask_cors import CORS, cross_origin
from modules.youtube_downloader import download_source, list_videos
from modules.web_scraper import scrape_website
from modules.ai import get_generated_images
from modules.todo import add_todo, delete_todo, get_todos, update_todo

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


# Post download video from youtube
@app.route(
    "/api/yt-download",
    methods=["POST"],
)
@cross_origin()
def yt_download():
    request_data = request.get_json()

    if request.method == "POST" and "video_url" in request_data:
        response = download_source(request_data["video_url"])
        return response


# Get downloaded videos as a list
@app.route(
    "/api/get-videos",
    methods=["GET"],
)
@cross_origin()
def list_yt_videos():
    response = list_videos()
    return response


# Scrape website
@app.route(
    "/api/scrape-website",
    methods=["POST"],
)
@cross_origin()
def scrape():
    request_data = request.get_json()
    response = scrape_website(request_data["category"])

    return response


# Todo - Get Todos
@app.route(
    "/api/todos",
    methods=["GET"],
)
@cross_origin()
def delegate_get_todos():
    response = get_todos()

    return response


# Todo - Add
@app.route(
    "/api/todo/add",
    methods=["POST"],
)
@cross_origin()
def delegate_add_todo():
    request_data = request.get_json()
    response = add_todo(request_data)

    return response


# Todo - Delete
@app.route(
    "/api/todo/delete",
    methods=["POST"],
)
@cross_origin()
def delegate_delete_todo():
    request_data = request.get_json()
    response = delete_todo(request_data["id"])

    return response


# Todo - Update
@app.route(
    "/api/todo/update",
    methods=["POST"],
)
@cross_origin()
def delegate_update_todo():
    request_data = request.get_json()
    response = update_todo(request_data)

    return response


# AI Image generation
@app.route(
    "/api/ai/image-creation",
    methods=["POST"],
)
@cross_origin()
def delegate_image_creation():
    request_data = request.get_json()
    response = get_generated_images(request_data)

    return response


if __name__ == "__main__":
    app.run(debug=True)
