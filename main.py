from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Simulasi data pengguna untuk demonstrasi
users = [
    {
        "user_id": 1,
        "email": "abyan@gmail.com",
        "password": "abyan123",
        "username": "SiPecintaUnikom",
        "gender": "Laki-laki",
        "rentang_waktu_olahraga": "8-9 jam",
        "olahraga_yang_sering": "Futsal",
        "tempat_olahraga": "Gor"
    },
    {
        "user_id": 2,
        "email": "fadli@gmail.com",
        "password": "fadli123",
        "username": "FadliKesayanganBuRiani",
        "gender": "Laki-laki",
        "rentang_waktu_olahraga": "2-3 jam",
        "olahraga_yang_sering": "Basket",
        "tempat_olahraga": "Lapang"
    },
    {
        "user_id": 5,
        "email": "tri@gmail.com",
        "password": "tri123",
        "username": "MangTri",
        "gender": "Laki-laki",
        "rentang_waktu_olahraga": "4-5 jam",
        "olahraga_yang_sering": "Futsal",
        "tempat_olahraga": "Gor"
    }
]


@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/users', methods=['GET'])
def get_users_by_email():
    email = request.args.get('email')
    
    if not email:
        return jsonify({"status": "Failed", "message": "Email parameter is required"}), 400
    
    filtered_users = [user for user in users if user["email"] == email]
    
    if filtered_users:
        response = {
            "status": "Success",
            "data": filtered_users
        }
        return jsonify(response), 200
    else:
        response = {
            "status": "Failed",
            "message": "No users found with the given email"
        }
        return jsonify(response), 404

@app.route('/api/login/', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = next((user for user in users if user["email"] == email and user["password"] == password), None)
    if user:
        # Generate a random token for each login
        login_token = secrets.token_hex(16)
        
        response = {
            "status": "Success",
            "message": "Login success",
            "data": {"email": email, "password": password},
            "token": {"login_token": login_token}
        }
        return jsonify(response), 200
    else:
        response = {
            "status": "Failed",
            "login": "Invalid email or password"
        }
        return jsonify(response), 401

@app.route('/api/users/', methods=['POST'])
def create_user():
    data = request.get_json()
    
    new_user = {
        "user_id": len(users) + 1,
        "email": data.get("email"),
        "password": data.get("password"),
        "username": data.get("username"),
        "gender": data.get("gender"),
        "rentang_waktu_olahraga": data.get("rentang_waktu_olahraga"),
        "olahraga_yang_sering": data.get("olahraga_yang_sering"),
        "tempat_olahraga": data.get("tempat_olahraga")
    }
    
    users.append(new_user)
    
    response = {
        "message": "User created successfully",
        "status": "Success"
    }
    
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
