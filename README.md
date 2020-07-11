# persona
Reto semana 8 de Platzi Master - Catch-up challenge

## Requerimientos.

Crear una clase llamada Persona en donde sus atributos sean:
* nombre
* apellido
* correo

**Realiza las siguientes asignaciones:**

* Los setters y getters para cada uno de los atributos.
* MostrarTodos(): Muestra todos los datos de la persona.
* ValidacionCorreo(): Parámetros: nombre, apellido y el correo. Deberás concatenar los tres datos de la siguiente manera:

`Hola soy José Pérez y mi correo es jose@hotmail.com`

* Crear otra clase que se llame Validaciones y crear los siguientes métodos:
    * ValidacionCorreo(): Parámetros: nombre, apellido y el correo. Deberasconcatenar el nombre y apellido una vez el correo insertado sea válido. (Utiliza expresiones regulares para validarlo).
    * ValidacionCorreo(): Parámetros: nombre y apellido. Debes concatenar ambos datos.
* Finalmente extender esta clase en la clase Persona para utilizar los métodos de validación. (En el constructor añade un ejemplo de ambos métodos con data de prueba)

# Ejecución

* `persona.py` contiene la clase `Persona`, contiene todos los getters y setters de sus atributos, así como el método `MostrarTodos()` que muestra toda la información de la persona.
* `validaciones.py` contiene la clase `Validaciones`, este contiene el método `ValidacionCorreo()`, el cual recibe como parámetro el nombre, apellido y el correo de la persona, si no se ingresa un correo, el programa verifica que tanto el nombre y apellido ingresado sea igual al almacenado en el objeto y los concatena en un saludo, de lo contrario muestra en pantalla `Información errónea`.
* Si en las `Validaciones` se ingresa el correo, por medio de expresiones regulares verificará que el correo sea válido, si lo es mostrará en pantalla `Ingresaste un correo válido...` y verificará el nombre, apellido y correo ingresados y si corresponden al objeto devolverá esta información en un saludo, de lo contrario mostrará `Información errónea`, pero si el correo ingresado no es válido, mostrará en pantalla `No es un correo válido`.