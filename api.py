from flask import Flask, request

app = Flask(__name__)


@app.route("/articles", methods=["GET"])
def get_articles():
    title = "Qiita Title"
    url = "https://qiita.com/"
    return {
        "title": title,
        "url": url,
    }


@app.route("/articles_form", methods=["GET"])
def get_articles_with_form():
    title = request.form["title"]
    url = request.form["url"]
    return {
        "title": title,
        "url": url,
    }


@app.route("/articles_json", methods=["GET"])
def get_articles_with_json():
    data = request.get_json()
    title = data["title"]
    url = data["url"]
    return {
        "title": title,
        "url": url,
    }


@app.route("/articles_args", methods=["GET"])
def get_articles_with_args():
    title = request.args.get("title")
    url = request.args.get("url")
    return {
        "title": title,
        "url": url,
    }
