def es_palindromo(cadena):
    cadena_limpia = ''.join(cadena.split()).lower()
    return cadena_limpia == cadena_limpia[::-1]

def main():
    texto = input("Introduce una cadena de texto: ")
    
    if es_palindromo(texto):
        print("La cadena es un palíndromo.")
    else:
        print("La cadena no es un palíndromo.")

main()
