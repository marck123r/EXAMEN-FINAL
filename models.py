

class Producto:
    def __init__(self,codigo,nombre,detalle,precio):
        self.codigo=codigo
        self.nombre=nombre
        self.detalle=detalle
        self.precio=precio

    def __str__(self) -> str:
        return "{};{};{};{}\n". format(
            self.codigo, self.nombre, self.detalle, self.precio
        )

class Usuario:
    def __init__(self,dni,pasword,tipo,nombre_apellido,dirrecion,gmail):
        self.dni=dni
        self.pasword=pasword
        self.tipo=tipo
        self.nombre_apellido=nombre_apellido
        self.dirreccion=dirrecion
        self.gamil=gmail

    def __str__(self) -> str:
        return "{};{};{};{};{};{} \n". format(
            self.dni,self.pasword,self.tipo, self.nombre_apellido, self.dirreccion, self.gamil
        )