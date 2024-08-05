def main():
    numeros = input("Ingrese los números separados por espacios: ")
    lista = numeros.split()

    invertir = lista[::-1]
    
    print("Lista invertida:", invertir)

main()