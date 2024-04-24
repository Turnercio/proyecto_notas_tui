


class Alumno:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.nota_matematicas = -1.0
        self.nota_lengua = -1.0

    def calcular_nota_media(self):
        return (self.nota_matematicas + self.nota_lengua) / 2
