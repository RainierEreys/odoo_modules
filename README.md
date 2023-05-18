# odoo_modules
Modulos Odoo

Estos son algunos modulos de Odoo

asignacion_equipos: Es un módulo en el cual se crea un modelo para registrar equipos, este modulo aparecera en la interfaz inicial de odoo como una aplicacion una vez esté instalado.

odoo_framework: Es un módulo donde se hereda el modelo Contactos 'res.partner' para agregarle el campo "fecha de cumpleaños", "sexo", "numero de pasaporte" y "edad" este ultimo campo, es un campo computado que depende de una funcion que calcula la edad en base a la fecha de nacimiento ingresada, tambien se agregó una funcion para validar que la fecha de nacimiento 
ingresada sea válidad y la edad no de un resultado negativo. Toda esta informacion aparecerá en la ficha del contacto ubicada en el modulo de "Contactos", especificamente en una pestaña 
denominada "Datos adicionales"

product_snippet_english: Es un módulo creado para llamar datos de la base de datos desde el controlador, especificamente de las tablas 'product.template' que corresponde a la tabla de 
productos, y la tabla 'res.partner' que corresponde a la tabla de contactos; una vez solicitados estos registros se reciben con un javascript mediante una funcion 'rpc' para 
asi organizarlos en un widget, que aparecera en el panel de Snippets en el sitio web de odoo, de manera que este se pueda arrastrar y soltar al sitio web y muestre la información suministrada.

report_invoice: Este modulo es un modulo para generar reportes de una factura de pago, en dicho modulo se crea el tipo de papel de ticket y se le da formato al ticket a imprimir en el sistema, de manera que al abrir cualquier factura y darle al boton "opcones" se pueda elegir la opción "imprimir ticket" en la cual el sistema procederá a imprimir el ticket con la información que se incluyó en su formato. De igual manera se generó otro reporte en formato A4 para su impresión.