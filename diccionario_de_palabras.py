import texto
def palabra_sin_simbolos(palabra):   
    for simbolo in [',',':',';','.','-','_','(',')','"','<','>','0','1','2','3','4','5','6','7','8','9']:
        if simbolo in palabra:
            palabra = palabra.replace(simbolo,"")
    return palabra
            
def texto_lista():
    lista = []
    for oraciones in texto.obtener_texto():
        for palabras in oraciones.split(' '):
            if palabras != '':
                lista.append(palabra_sin_simbolos(palabras).lower())
    return lista
    
def lista_diccionario(lista):
    diccionario = {}
    for palabras2 in lista:
        if palabras2 != '':
            if palabras2 in diccionario:
                diccionario[palabras2] += 1
            else:
                diccionario[palabras2] = 1
    return diccionario

def main():
    dicc=lista_diccionario(texto_lista())
    return sorted(dicc.items(),key = lambda x:x[0])
