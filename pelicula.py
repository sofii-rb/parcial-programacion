class Pelicula:
    def __init__(self, codigo=0, titulo="", duracion=0, director="", prestada=False):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__duracion = duracion
        self.__director = director
        self.__prestada = prestada

    #Get & Set
    def get_codigo(self):
        return self.__codigo

    def get_titulo(self):
        return self.__titulo
    
    def get_duración(self):
        return self.__duracion
    
    def get_director(self):
        return self.__director
    
    def get_prestada(self):
        return self.__prestada
    
    #______________________________

    def set_codigo(self, codigo):
        self.__codigo = codigo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_duracion(self, duracion):
        self.__duracion = duracion

    def set_director(self, director):
        self.__director = director

    def set_alquilada(self, prestada):
        self.__prestada = prestada

    #METODOS

    def prestar(self):
        if not self.__prestada:
            self.__prestada = True
            return f"La película {self.__titulo} ha sido prestada."
        else:
            return f"La pelicula {self.__titulo} ya estaba prestada."
        
    def devolver(self):
        if not self.__prestada:
            self.__prestada = False
            return f"La pelicula {self.__titulo} ha sido devuelta"
        else:
            return f"La pelicula {self.__titulo} no habia sido prestada"
        
    def costo_reproduccion (self, costo_por_minuto):
        costo_total = self.__duracion * costo_por_minuto
        return f"El costo de reproducir la película es: ${costo_total:.2f}"

    #_________________________________

    def __str__(self):
        estado = "está prestado" if self.__prestada else "no está prestada"
        return (f"La película {self.__codigo} con titulo {self.__titulo} y autor {self.__director} "
                f"Dura {self.__duracion} min y {estado}")
    
    def __eq__(self, otra_pelicula):
        if isinstance(otra_pelicula, Pelicula):
            return self.__codigo == otra_pelicula.get_codigo()
        return False


