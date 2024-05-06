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

# Route pour ajouter un utilisateur
@app.route("/add_user")
def add_user():
    # Créer un nouvel utilisateur
    new_user = User(username="example_user")
    # Ajouter l'utilisateur à la base de données
    db.session.add(new_user)
    db.session.commit()
    return "User added successfully!"

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
