from flask import Flask

app = Flask('ping')
# usage:
# curl http://127.0.0.1:9696/ping
# or go to webbrowser:
# http://localhost:9696/ping

@app.route('/ping', methods=['GET'])
def ping():
    return "response: PONG"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
