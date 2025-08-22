from flask import Flask, jsonify
import json

app = Flask(__name__)

# API route
@app.route('/api', methods=['GET'])
def get_data():
    try:
        # Read data from backend file (data.json)
        with open("data.json", "r") as f:
            data = json.load(f)
        return jsonify(data), 200
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
