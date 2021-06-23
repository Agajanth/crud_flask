from app import app
from app.database import *
from flask import jsonify, Response,request
from app.utils.parser import Parse

@app.route('/all_registers',methods=['GET'])
def all_registers():
    personas = Persona.query.all()
    listado_personas = Parse.parse(personas)
    total = Persona.query.count()
    app.logger.debug(f"Listado de personas : {listado_personas}")
    return jsonify({"Total personas":total,"listado Personas":listado_personas})

@app.route('/insertar_persona',methods=['POST'])
def insertar_persona():
    persona = Persona()
    persona.nombre = request.json['name']
    persona.email = request.json['email']
    app.logger.debug(f"persona a insertar: nombre {persona.nombre} - email {persona.email}")

    db.session.add(persona)
    db.session.commit()
    app.logger.debug(f"Usuario {persona} agregado con éxito")
    return Response(jsonify({"Operacion registro":"realizada con exito"}),status=200)
    
    