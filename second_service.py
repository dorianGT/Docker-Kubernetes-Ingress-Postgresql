from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://myuser:mypassword@postgresql:5432/mydatabase'  # Remplacez avec vos informations de connexion
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialisation de l'extension SQLAlchemy
db = SQLAlchemy(app)

# Modèle de données SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

@app.route("/second")
def hello():
    return "Hello From Service 2!"

# Route pour afficher les utilisateurs
@app.route("/second/show_user")
def show_users():
    # Récupérer tous les utilisateurs de la base de données
    users = User.query.all()
    # Générer une chaîne pour afficher les utilisateurs
    users_str = ""
    for user in users:
        users_str += f"ID: {user.id}, Username: {user.username}<br>"
    return users_str

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
