from app import app
from werkzeug.security import check_password_hash, generate_password_hash
from app.database import *
from flask import jsonify, Response,request,session
from app.utils.parser import Parse
import os
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies
secret_key = os.urandom(16)
jwt_secret_key = os.urandom(32)
#configure secret key for session flask
app.config['SECRET_KEY'] = secret_key
#configure jwt token secret key 
app.config["JWT_SECRET_KEY"] = jwt_secret_key
# Here you can globally configure all the ways you want to allow JWTs to
# be sent to your web application. By default, this will be only headers.
#app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
app.config["JWT_TOKEN_LOCATION"] = ["headers"]
#routes
jwt = JWTManager(app)
@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    #hash_password = generate_password_hash(password)
    user = Usuario.query.filter_by(username=username).first()
    #password_db = Usuario.query.filter_by(password=password).one()
    
    if not user or not check_password_hash(user.password,password):
        return jsonify({'Login':"Error: usuario o contraseña incorrecto"})
    else:
        session['username']=user.username
        return jsonify({'Login':"Exito"})
    
@app.route('/logout',methods=['POST'])
def logout():
    session.pop('username',None)
    return jsonify({"logout":"exito"})
    
@app.route('/create_user', methods=['POST'])
def create_user():
    usuario = Usuario()
    username = request.json['username']
    password = request.json['password']
    hash_password = generate_password_hash(password)
    request_username = Usuario.query.filter_by(username=username).first()
    if not request_username:
        usuario.username = username
        usuario.password = hash_password
        app.logger.debug(f"Usuario a registrar -> userame : {username}")
        db.session.add(usuario)
        db.session.commit()
        return jsonify({"Registros Usuario":"Exito"})
    else:
        return jsonify({"Registro usuario":"Fallo, usuario ya existe"})
    

@app.route('/all_registers',methods=['GET'])
def all_registers():
    if 'username' in session:
        personas = Persona.query.all()
        listado_personas = Parse.parse(personas)
        total = Persona.query.count()
        app.logger.debug(f"Listado de personas : {listado_personas}")
        return jsonify({"Total personas":total,"listado Personas":listado_personas})
    else:
        return jsonify({"Usuario":"No esta en session"}),401
    
    
@app.route('/insertar_persona',methods=['POST'])
def insertar_persona():
    if 'username' in session:
        persona = Persona()
        persona.nombre = request.json['name']
        persona.email = request.json['email']
        app.logger.debug(f"persona a insertar: nombre {persona.nombre} - email {persona.email}")

        db.session.add(persona)
        db.session.commit()
        app.logger.debug(f"Usuario {persona} agregado con éxito")
        return Response(jsonify({"Operacion registro":"realizada con exito"}),status=200)
    else:
        return jsonify({"Usuario":"No esta en session"})

@app.route('/persona/<int:id>',methods=['GET', 'POST','DELETE'])
def persona(id):
    persona = Persona.query.filter_by(id=id).first_or_404()
    if request.method == 'GET':
        #parse_persona = Parse.parse(persona)
        app.logger.debug("Se consulta el registro")
        return jsonify({"persona":{"nombre":persona.nombre,"email":persona.email}})
    elif request.method == 'POST':
        persona.nombre = request.json['name']
        persona.email = request.json['email']
        app.logger.debug(f"Persona a actualizar -> {persona}")
        db.session.commit()
        #parse_persona = Parse.parse(persona)
        return jsonify({"usuario actualizado":{"nombre":persona.nombre,"email":persona.email}})
    elif request.method =='DELETE':
        app.logger.debug(f"Deleting {persona}")
        db.session.delete(persona)
        app.logger.debug(f"Commit on db")
        db.session.commit()
        return jsonify({"User deleted":{"nombre":persona.nombre,"email":persona.email}})    
    
@app.route('/login_andGet_jtw',methods=['POST'])
def login_andGet_jtw():
    username = request.json['username']
    password = request.json['password']
    user = Usuario.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password,password):
        return jsonify({"login":"incorrecto"}),401
    else:
        token = create_access_token(identity=user.id)
        return jsonify({"login":"exito","token":token})
    

    