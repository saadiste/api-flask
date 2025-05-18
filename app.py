from flask import Flask, jsonify, request
import jwt, datetime

app = Flask(__name__)
SECRET = 'monsecret'

@app.route('/')
def accueil():
    return jsonify(message="Bienvenue dans l'API Flask")

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data['username'] == 'admin' and data['password'] == 'admin':
        token = jwt.encode({"user": "admin", "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET, algorithm="HS256")
        return jsonify(token=token)
    return jsonify(message="Identifiants invalides"), 401

@app.route('/donnee')
def donnee():
    auth_header = request.headers.get('Authorization')
    if not auth_header: return jsonify(message="Token manquant"), 403
    token = auth_header.split(" ")[1]
    try:
        jwt.decode(token, SECRET, algorithms=["HS256"])
        return jsonify(data="Ceci est une donnée protégée")
    except:
        return jsonify(message="Token invalide ou expiré"), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
