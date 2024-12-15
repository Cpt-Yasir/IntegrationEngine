from flask import Flask, request, jsonify, Response
import json, random

app = Flask(__name__)
HOST = '0.0.0.0'
PORT = 8080




@app.route('/detects/queries/detects/v1', methods=['GET'])
def get_detections():
    res = {'detects': [
        {
            'user_context': {
                'username': 'test1',
                'email': 'test1@email.com'
            }
        },
        {
            'user_context': {
                'username': 'test2',
                'email': 'test2@email.com'
            }
        },
        {
            'user_context': {
                'username': 'test2',
                'email': 'test2@email.com'
            }
        }
    ]}
    return Response(json.dumps(res), status=200 if res else 404, headers={'Content-Type': 'application/json'})





if __name__ == "__main__":
    print(" Mock Service has started...")
    app.run(debug=True, host=HOST, port=PORT)