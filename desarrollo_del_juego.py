import diccionario_de_palabras
import random
def solicitar_long_palabra():
    '''Solicita la longitud de la palabra, menor a 5 caracteres y devuelve una palabra del texto con esa longitud'''
    dicc = diccionario_de_palabras.lista_diccionario(diccionario_de_palabras.texto_lista())
    long_palabra = 0
    lista_igual_longitud=[]
    while long_palabra < 5 or long_palabra > diccionario_de_palabras.long_max_palabras():
        long_palabra = int(input('Ingrese la longitud de la palabra, no puede ser menor a 5 caracteres :'))
    for palabra in dicc.keys():
        if len(palabra) == long_palabra:
            lista_igual_longitud.append(palabra)
    return random.choice(lista_igual_longitud)            
        
    
    