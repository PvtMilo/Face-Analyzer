# face_similarity
Face Similarity Web App
=======================

A simple Flask web application that compares the similarity between two uploaded face images using the DeepFace library.

-----------------------
FEATURES
-----------------------

- Upload two face images
- Uses DeepFace (Facenet model) for face verification
- Displays both images and the similarity score
- Built with Flask and TensorFlow

-----------------------
PROJECT STRUCTURE
-----------------------

face_similarity/
|
├── app.py               -> Main Flask app
├── requirements.txt     -> Dependencies
├── README.txt           -> This file
├── templates/
│   └── index.html       -> Web page template
├── static/              -> Uploaded images are saved here
└── venv/                -> Virtual environment (should be excluded from version control)

-----------------------
REQUIREMENTS
-----------------------

- Python 3.10
- Virtual environment (venv)

-----------------------
SETUP INSTRUCTIONS
-----------------------

1) Clone the repository:
   git clone <your-repo-url>
   cd face_similarity

2) Create and activate a virtual environment:
   # Make sure you are using Python 3.10
   python3.10 -m venv venv

   # Activate (Git Bash)
   source venv/Scripts/activate

   # Or PowerShell / CMD
   venv\Scripts\activate

3) Install dependencies:
   pip install -r requirements.txt

4) Run the app:
   python app.py

5) Open in your browser:
   http://127.0.0.1:5000/

-----------------------
HOW TO USE
-----------------------

1) Upload two face images
2) Click Submit
3) View the similarity score and the preview images

-----------------------
RECOMMENDED VERSIONS
-----------------------

- TensorFlow 2.10.0
- Keras 2.10.0
- DeepFace 0.0.83

-----------------------
LICENSE
-----------------------

This project is for educational and demonstration purposes.

-----------------------
AUTHOR
-----------------------

Built by [Pvt.Milo]
