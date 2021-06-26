"""from app.database import database

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250),nullable=False)
    email = db.Column(db.String(250),nullable=False,unique=True)
    
    def __str__(self):
        return f"id : {self.id}, nombre : {self.nombre}, email : {self.email}"
"""