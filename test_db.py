from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://carlos:74097400Cr.@localhost/frutas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Suministro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

with app.app_context():
    # Crear tablas si no existen
    db.create_all()

    # Insertar un suministro de prueba
    nuevo = Suministro(nombre='Guantes', cantidad=100)
    db.session.add(nuevo)
    db.session.commit()

    # Consultar todos los suministros
    todos = Suministro.query.all()
    for s in todos:
        print(f"{s.nombre}: {s.cantidad} unidades")
