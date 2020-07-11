from validaciones import Validaciones

class Persona(Validaciones):
    def __init__(self, nombre, apellido, correo):
        # Invocando al método constructor de Validaciones
        Validaciones.__init__(self, nombre, apellido, correo)
        # Definiendo las propiedades de persona
        self._nombre = nombre
        self._apellido = apellido
        self._correo = correo
    
    # Definiendo los Getters
    def getNombre(self):
        "Devuelve el nombre del usuario."
        print(f'El nombre es {self._nombre}')
        return self._nombre

    def getApellido(self):
        "Devuelve el apellido del usuario."
        print(f'El apellido es {self._apellido}')
        return self._apellido

    def getCorreo(self):
        "Devuelve el correo del usuario."
        print(f'El correo es {self._correo}')
        return self._correo

    # Definiendo los Setters
    def setNombre(self, nombre):
        "Modifica el nombre del usuario"
        self._nombre = nombre
        print(f'El nombre se ha modificado por: {nombre}')

    def setApellido(self, apellido):
        "Modifica el nombre del usuario"
        self._apellido = apellido
        print(f'El apellido se ha modificado por: {self._apellido}')
    
    def setCorreo(self, correo):
        "Modifica el correo del usuario"
        self._correo = correo
        print(f'El correo se ha modificado por: {self._correo}')

    def MostrarTodos(self):
        "Muestra toda la información de la persona"
        print(f"""Los datos de la persona son:
        Nombre: {self._nombre}
        Apellido: {self._apellido}
        Correo: {self._correo}""")
    
    # def ValidacionCorreo(self, nombre, apellido, correo):
    #     "Verifica la validez de la información de la persona"
    #     if self._nombre == nombre:
    #         if self._apellido == apellido:
    #             if self._correo == correo:
    #                 print(f'Hola soy {nombre} {apellido} y mi correo es {correo}')
    #             else:
    #                 print('Información errónea')
    #         else:
    #             print('Información errónea')
    #     else:
    #         print('Información errónea')