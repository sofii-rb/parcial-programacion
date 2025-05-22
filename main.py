from pelicula import Pelicula

if __name__ == "__main__":
    pelicula1 = Pelicula(123, "No Country For Old Men", 122, " Ethan Coen, Joel Coen")
    pelicula2 = Pelicula(456, "Memorias de una Geisha", 145, "Rob Marshall")
    pelicula3 = Pelicula(123, "Ex Machina", 88, "Alex Garland")

    print(pelicula1)
    print(pelicula2)
    print(pelicula3)

    print(pelicula1.prestar())  
    print(pelicula1.prestar())  
    print(pelicula1.devolver())  

    print(pelicula2.costo_reproduccion(25)) 

    print("¿pelicula1 y pelicula3 tienen el mismo codigo?", pelicula1 == pelicula3) 


