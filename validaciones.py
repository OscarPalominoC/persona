import re

class Validaciones:
    def __init__(self, nombre, apellido, correo):
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
    
    
    def ValidacionCorreo(self, nombre, apellido, correo=None):
        "Verifica la validez de la información de la persona"
        if correo == None:
            if self._nombre == nombre:
                if self._apellido == apellido:
                    print(f'Hola soy {nombre} {apellido}.')
                else:
                    print('Información errónea')
            else:
                print('Información errónea')
        else:
            if re.search('[\w\._\-]{4,30}\+?[\w]{0,10}@[\w\.-]{3,}?\.\w{2,5}$', correo):
                print('Ingresaste un correo válido...')
                if self._nombre == nombre:
                    if self._apellido == apellido:
                        if self._correo == correo:
                            print(f'Hola soy {nombre} {apellido} y mi correo es {correo}')
                        else:
                            print('Información errónea')
                    else:
                        print('Información errónea')
                else:
                    print('Información errónea')
            else:
                print('No es un correo válido')

def tests():
    valid = Validaciones("Oscar", "Palomino", "oscar@mail.com")
    valid.ValidacionCorreo("Oscar", "Palomino")
    valid.ValidacionCorreo("Pepito", "Perez")
    valid.ValidacionCorreo("Oscar", "Palomino", "oscar@mail.com")
    valid.ValidacionCorreo("Oscar", "Palomino", "oscar@mail2.com")