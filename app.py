from flask import Flask, request, render_template
import os

from extractor import extract_info
from doc_generator import generate_doc
from coverage_checker import calculate_coverage

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["file"]
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Process file
        functions, classes = extract_info(filepath)
        doc = generate_doc(functions, classes)
        coverage = calculate_coverage(functions, classes, filepath)

        return render_template("result.html",
                               functions=functions,
                               classes=classes,
                               doc=doc,
                               coverage=coverage)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)