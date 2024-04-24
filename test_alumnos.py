from alumnos import Alumno

def  test_crear_alumno():
    estudiante = Alumno("Peter", "Porker")
    assert estudiante.nombre == "Peter"
    assert estudiante.apellido == "Porker"
    assert estudiante.nota_matematicas == -1.0
    assert estudiante.nota_lengua == -1.0

    assert estudiante.calcular_nota_media() == -1.0
    
def test_calcular_nota_media():
    estudiante = Alumno("Prueba1", "Prueba1.2")
    estudiante.nota_matematicas = 5
    estudiante.nota_lengua = 5

    assert estudiante.calcular_nota_media() == 5