lista_diccionarios = []
def extraer_pregunta(pregunta: str)-> dict:
    partes = pregunta.split("|")

    preguntas = partes[0]
    lista = partes[1:]
    verdadera = lista[0]
    opciones = lista[0:]
    return {
        "pregunta": preguntas,
        "correcta": verdadera,
        "opciones": opciones,
    }

preguntas_txt = [
"¿Cuál es la capital de España?|Madrid|Barcelona|Sevilla|Toledo",
"¿Cuántos continentes hay?|5|7|6|3",
"¿Qué lenguaje se usa para programar en Arcade?|Python|Java|JavaScript|C",
"¿La tortilla de patata lleva cebolla?|Jamás|Si|No con excepciones|Tal vez",
]

for linea in preguntas_txt:
    resultado = extraer_pregunta(linea)
    lista_diccionarios.append(resultado)  

tope = len(lista_diccionarios)
contador = 0
#print(lista_diccionarios)
#print(lista_diccionarios[0]["opciones"])

while contador < tope:
    print(lista_diccionarios[contador]["pregunta"])
    print(lista_diccionarios[contador]["opciones"])
    input(("Tu respuesta: "))
    
    contador += 1