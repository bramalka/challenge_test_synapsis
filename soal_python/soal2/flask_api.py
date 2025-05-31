import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "function"))

from flask import Flask, request, jsonify # type: ignore
from grade_processor import GradeProcessor # type: ignore

app = Flask(__name__)
processor = GradeProcessor()


@app.route("/api/<candidate_name>", methods=["POST"])
def processGrade(candidate_name):
    """API endpoint to process grade and return result"""
    try:
        # Get JSON data from request
        data = request.get_json()
        
        # Process the grade using GradeProcessor
        result = processor.processGradeData(data, candidate_name)
        
        return jsonify(result), 200
        
    except Exception as e:
        # Return error response for any unexpected errors
        return jsonify({
            "nama": candidate_name,
            "nilai": "Invalid",
            "status": "tidak lulus"
        }), 400


if __name__ == "__main__":
    print("Starting Flask application on port 8080...")
    print("API Endpoint: POST /api/<nama_kandidat>")
    print("JSON Input: {\"nilai\": 85}")
    print("Example: curl -X POST http://localhost:8080/api/bram -H \"Content-Type: application/json\" -d \"{\\\"nilai\\\": 85}\"")
    
    app.run(host="0.0.0.0", port=8080, debug=True)