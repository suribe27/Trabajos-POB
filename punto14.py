def main():
    entrada = input("Ingrese números separados por espacios: ")
    
    numeros = list(map(float, entrada.split()))
    
    if numeros:  
        suma = sum(numeros)
        cantidad = len(numeros)
        media = suma / cantidad
    else:
        media = 0
    
    print("La media aritmética es:", media)
main()
