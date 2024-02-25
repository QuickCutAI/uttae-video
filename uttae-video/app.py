from flask import Flask, request, jsonify, url_for
import os

from functions.file_control import save_file, file_delete, new_filename, get_filename
from functions.video_control import remove_silent_parts

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/upload", methods=["POST"])
def upload_file():
    # 업로드된 파일 확인
    if "file" not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files["file"]

    return save_file(file, app.config["UPLOAD_FOLDER"])

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return jsonify({"file_url": url_for("uploaded_file", filename=filename)})

@app.route("/delete_file", methods=["DELETE"])
def delete_file():
    file_path = request.form.get("path")
    return file_delete(file_path)

@app.route("/trim_video", methods=["PUT"])
def trim_video():
    file_path = request.form.get("path")
    new_path = new_filename(file_path)
    remove_silent_parts(file_path, new_path)

    return jsonify({
        "file_url": url_for(
            "uploaded_file", filename=get_filename(new_path)
        )
    })

if __name__ == "__main__":
    app.run(debug=True)