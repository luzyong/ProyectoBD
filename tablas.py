from conexion import Conexion

Conexion.Insert(tabla='Productos',campos='(idProducto,descripcion)',valores='()')
Conexion.Insert(tabla='Transportista',campos='(idTransportista,NombreTransportista)',valores='()')
Conexion.Insert(tabla='Aduana',campos='(idAduana,NombreAduana)',valores='()')
Conexion.Insert(tabla='Requisitor',campos='(idRequisitor,puesto,nombre,correo_electronico)',valores='()')
Conexion.Insert(tabla='TipoAutorizacion',campos='(idTipoAutorizacion,descripcionAutorizacion)',valores='()')
Conexion.Insert(tabla='Autorizacion',campos='(idAutorizacion,idTipoAutorizacion,compras,dirPlanta,planta)',valores='()')