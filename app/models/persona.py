from app.database import * 

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    email = db.Column(db.String(250))
    
    def __str__(self):
        return f"id : {self.id}, nombre : {self.nombre}, email : {self.email}"
    