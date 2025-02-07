"""Server for Emotion Detection API using Flask"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """Renderiza la página de inicio"""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """Procesa el texto enviado por el usuario y devuelve las emociones detectadas"""
    text_to_analyze = request.form.get("text")
    emotions = emotion_detector(text_to_analyze)

    if emotions["dominant_emotion"] is None:
        return "Invalid text! Please try again."

    response_text = (
        "For the given statement, the system response is "
        f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, \n"
        f"'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}.\n"
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )

    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
