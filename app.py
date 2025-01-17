from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Globals to track the current state
current_user = None
start_time = None
leaderboard = {}

@app.route('/click', methods=['POST'])
def click_button():
    global current_user, start_time, leaderboard

    data = request.json
    user = data.get("name")

    current_time = time.time()

    if current_user is not None:
        # Calculate time for the previous user
        elapsed_time = current_time - start_time
        leaderboard[current_user] = leaderboard.get(current_user, 0) + elapsed_time

    # Update to the new user
    current_user = user
    start_time = current_time

    return jsonify({"message": f"{user} is now active!", "leaderboard": leaderboard})

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    return jsonify(sorted_leaderboard)

if __name__ == '__main__':
    app.run(debug=True)
