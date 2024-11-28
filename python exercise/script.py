with open('results.txt', 'w') as file:
    numerosPrimos=[]
    # Se itera entre el 2 y el 250
    # no se considera el 1 porque la definición de número primo es que
    # cualquier número que tenga 2 divisores es un número primo
    # el 1 solo tiene como divisor el 1, así que no se considera primo.
    
    for i in range(1, 251):
        esPrimo=True

        #Se buscan los divisores de i hasta la raíz cuadrada de i
        #Si un numero no es primo, se puede expresar en 2 factores: i = a*b
        #Si ambos fueran mayores que la raíz cuadrada de i, el producto excedería a i
        #Por eso es que al menos un factor (a o b) debe ser menor o igual a la raíz cuadrada de i
        
        for j in range (2, int(i**0.5)+1):
            if i%j==0:
                esPrimo=False
                break
        if esPrimo:
            numerosPrimos.append(i)

    # Escribir los resultados en un archivo
    file.write('\n'.join(map(str, numerosPrimos)))
    print("Resultados traspasados al archivo: 'results.txt'.")