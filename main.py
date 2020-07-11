from persona import Persona

if __name__ == "__main__":
    oscar = Persona('oscar', 'palomino', 'oscar@mail.com')
    oscar.getNombre()
    oscar.setNombre('Oscar')
    oscar.getNombre()
    oscar.getApellido()
    oscar.setApellido('Palomino')
    oscar.getApellido()
    oscar.getCorreo()
    oscar.setCorreo('oscar@palomino.com')
    oscar.getCorreo()
    oscar.MostrarTodos()
    oscar.ValidacionCorreo('Pepito', 'Perez')
    oscar.ValidacionCorreo('Oscar', 'Palomino')
    oscar.ValidacionCorreo("Oscar", "Palomino", "oscar@palomino.com")
    oscar.ValidacionCorreo("Oscar", "Palomino", "os+car@palomino.com")