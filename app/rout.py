from app import app
from app.database import *
from flask import jsonify
from app.utils.parser import Parse
@app.route('/all_registers',methods=['GET'])
def all_registers():
    personas = Persona.query.all()
    listado_personas = Parse.parse(personas)
    total = Persona.query.count()
    app.logger.debug(f"Listado de personas : {listado_personas}")
    return jsonify({"Total personas":total,"listado Personas":listado_personas})
    
    