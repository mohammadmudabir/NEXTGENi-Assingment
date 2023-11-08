from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name)
app.config["JWT_SECRET_KEY"] = "your-secret-key"  # Replace with your own secret key
jwt = JWTManager(app)

# Simulated user database (you should use a real database)
users = {
    "user1": {"password": "password1"},
    "user2": {"password": "password2"},
}

# Endpoint for user registration (simplified)
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Create user in the database (simulated)
    users[username] = {"password": password}
    return jsonify({"message": "User registered successfully"})

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username]["password"] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# Protected endpoint for creating a new blog post
@app.route('/create_post', methods=['POST'])
@jwt_required
def create_post():
    current_user = get_jwt_identity()
    # Check JWT token to ensure the user is authenticated
    # Create a new blog post (simulated)
    return jsonify({"message": f"Blog post created by {current_user}"})

if __name__ == '__main__':
    app.run(debug=True)
