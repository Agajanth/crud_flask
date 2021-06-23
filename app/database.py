from app import app 
from flask_sqlalchemy import SQLAlchemy
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