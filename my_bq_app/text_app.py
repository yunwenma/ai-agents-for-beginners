# text_app.py
from flask import Flask, request, jsonify
import traceback

app = Flask(__name__)

try:
    from analyze import analyze_behavior_text
except Exception as e:
    analyze_behavior_text = None
    load_error = str(e)

@app.route("/analyze", methods=["POST"])
def analyze():
    if analyze_behavior_text is None:
        return jsonify({
            "error": "Failed to load analyzer. Please ensure ChromaDB collection exists by running rag_preprocess.py.",
            "details": load_error
        }), 500

    try:
        data = request.get_json()
        question = data.get("question", "")
        answer = data.get("answer", "")
        role = data.get("role", "")

        result = analyze_behavior_text(question, answer, role)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({
            "error": "Something went wrong during analysis.",
            "details": traceback.format_exc()
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)