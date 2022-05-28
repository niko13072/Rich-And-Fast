from Producto import Producto
from Usuario import Usuario
from Pedido import Pedido
from Cliente import Cliente


producto1 = Producto('Hamburguesa',13000)
producto2 =Producto('Gaseosa',5000)

usuario1=Usuario(10,'abc123')
usuario1.Nombre='nicolas'

usuario2=Usuario(11,'abc1234')
usuario2.Nombre='ana'

usuario3=Usuario(12,'abc12345')
usuario3.Nombre='Laura'

Pedido1 = Pedido(producto1,usuario1)