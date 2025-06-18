from flask import Flask, render_template, request
from deepface import DeepFace
import os
import uuid
from PIL import Image

app = Flask(__name__)
UPLOAD_FOLDER = "static"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    similarity = None
    user_path = None
    target_path = None

    if request.method == "POST":
        user_img = request.files.get("user_img")
        target_img = request.files.get("target_img")

        if user_img and target_img:
            user_filename = f"user_{uuid.uuid4()}.jpg"
            target_filename = f"target_{uuid.uuid4()}.jpg"

            user_path = os.path.join(app.config["UPLOAD_FOLDER"], user_filename)
            target_path = os.path.join(app.config["UPLOAD_FOLDER"], target_filename)

            user_img.save(user_path)
            target_img.save(target_path)

            try:
                result = DeepFace.verify(user_path, target_path, model_name='VGG-Face')
                similarity = round((1 - result["distance"]) * 100, 2)
            except Exception as e:
                similarity = f"Error: {str(e)}"

    return render_template("index.html", similarity=similarity,
                           user_img=user_path, target_img=target_path)

if __name__ == "__main__":
    app.run(debug=True)
