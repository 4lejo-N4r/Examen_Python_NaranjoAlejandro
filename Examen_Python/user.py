import json


class usuario:
    def __init__(self, documento, nombres, apellidos, numero, direccion ):
        self.documento = documento
        self.nombres = nombres
        self.apellidos = apellidos
        self.numero = numero
        self.direccion = direccion


    def to_dict(self):
        return{
        'documento':self.documento,
        'nombres': self.nombres,
        'apellidos': self.apellidos,
        'numero' : self.numero,
        'direccion': self.direccion
        }
