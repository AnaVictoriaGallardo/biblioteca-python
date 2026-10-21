#Definición de catálogo de libros registrados en la biblioteca.
catalogo = [{'Título':'Orgullo y prejuicio',
'Autor':'Jane Austen',
'Género':'Novela Rosa',
'Disponible': True,
'Precio':33999.99 
},
{'Título':'Harry Potter y la Piedra Filosofal',
'Autor':'J.K Rowling',
'Género':'Literatura Fantástica',
'Disponible': True,
'Precio':16500.99  
},
{'Título':'Carrie',
'Autor':'Stephen King',
'Género':'Terror',
'Disponible': False ,
'Precio':44357.99 
}]

#Evitar duplicados
autores_registrados = {'Jane Austen','J.K Rowling','Stephen King'}


#Creación de la función para agregar libros nuevos
def agregar_libro (catalogo):
    catalogo_actualizado = dict(Título = input('Ingrese el título del nuevo libro: '), Autor = input('Ingrese el autor del nuevo libro: '),Género = input('Ingrese el género del nuevo libro: '),Disponible = True, Precio = float(input('Ingrese el precio del nuevo libro: ')))
    #Lo siguiente permite que el catalogo se actualice con el libro nuevo agregado
    catalogo.append(catalogo_actualizado)
    print('Libro agregado correctamente')

#Creación de la función para buscar libros registrados por género
def buscar_por_genero (catalogo):
    busqueda = input('Ingrese el género que busca: ').lower()
    coincidencias = [Libro['Título'] for Libro in catalogo if Libro['Género'].lower()==busqueda]
    print(coincidencias)
    return (coincidencias)

#Creación de la función que permite calcular el valor total del catálogo
def calcular_valor_inventario(catalogo):
    valor_total = sum (Valor['Precio'] for Valor in catalogo)
    print(valor_total)
    return(valor_total)

#Creación de la función que permite buscar libros por nombre del autor
def buscar_por_autor (catalogo):
    busqueda = input('Ingrese el nombre del autor que está buscando: ').lower().strip()
    resultado = [Título['Título'] for Título in catalogo if Título['Autor'].lower().strip() ==busqueda]
    print(f'Los  títulos de este autor son: {list(enumerate(resultado))}')
    return resultado


 # Llamadas a las funciones al final del archivo para probarlas:

print(agregar_libro(catalogo))

print(buscar_por_genero(catalogo))

print(calcular_valor_inventario(catalogo))

print(buscar_por_autor(catalogo))





    










    
    

