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