from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np


app = Flask(__name__)
CORS(app)

# Load the model
model = load_model(r"C:\Users\91969\Desktop\Fake currency Detection12\fake_currency_detector.h5")

# Preprocess image
def preprocess_image(image):
    image = image.convert("L")  
    image = image.resize((256, 256))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    image = np.expand_dims(image, axis=-1)  
    
    return image


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files or not request.files["file"]:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    try:
        # Process the image
        image = Image.open(file.stream)
        processed_image = preprocess_image(image)
    except Exception as e:
        return jsonify({"error": f"Error processing image: {str(e)}"}), 400

    try:
        # Make prediction
        prediction = model.predict(processed_image)
        result = "Fake" if prediction[0][0] > 0.5 else "Real"
        confidence = round(float(prediction[0][0]), 2)

        # Return JSON response
        return jsonify({"prediction": result, "confidence": confidence})
    except Exception as e:
        return jsonify({"error": f"Error during prediction: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
