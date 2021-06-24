class Parse():
    
    @classmethod
    def parse(cls,personas:list)->dict:
        listado_personas={}
        count=0
        for persona in personas:
            count+=1
            listado_personas[f"Persona {count}"] = {"Nombre":persona.nombre,"email":persona.email,"id":persona.id}
        return listado_personas