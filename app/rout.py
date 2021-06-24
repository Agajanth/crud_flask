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
    