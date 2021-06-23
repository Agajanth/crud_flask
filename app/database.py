from re import A
from app import app 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#Configuracion base de datos
USER_DB = 'postgres'
PASSWORD_DB = 'david123.4'
URL_DB = 'localhost'
NAME_DB = 'sap_flask_db'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASSWORD_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#Inicializamos la variable db
db = SQLAlchemy(app)

#Configurar flask migrate
migrate = Migrate()
migrate.init_app(app,db)

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250),nullable=False)
    email = db.Column(db.String(250),nullable=False,unique=True)
    
    def __str__(self):
        return f"id : {self.id}, nombre : {self.nombre}, email : {self.email}"
