from flask import Flask, render_template, request
from deepface import DeepFace
import os
import uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

print("[INFO] Loading face recognition model...")
model_name = "Facenet"
DeepFace.build_model(model_name)
print("[INFO] Model loaded.")

@app.route("/", methods=["GET", "POST"])
def index():
    similarity = None
    image1_url = None
    image2_url = None
    error = None

    if request.method == "POST":
        image1 = request.files.get("image1")
        image2 = request.files.get("image2")

        if image1 and image2:
            filename1 = f"user1_{uuid.uuid4()}.jpg"
            filename2 = f"user2_{uuid.uuid4()}.jpg"
            path1 = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(filename1))
            path2 = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(filename2))
            image1.save(path1)
            image2.save(path2)

            image1_url = path1
            image2_url = path2

            try:
                print(f"[DEBUG] Comparing {path1} vs {path2}")
                result = DeepFace.verify(
                    img1_path=path1,
                    img2_path=path2,
                    model_name=model_name,
                    enforce_detection=False
                )
                similarity = round((1 - result["distance"]) * 100, 2)
            except Exception as e:
                print("[ERROR]", e)
                error = "Gagal membandingkan wajah. Pastikan gambar mengandung wajah yang jelas."

    return render_template("index.html", similarity=similarity, image1=image1_url, image2=image2_url, error=error)

if __name__ == "__main__":
    app.run(debug=True)
