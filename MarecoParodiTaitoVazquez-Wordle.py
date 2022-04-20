import time
adivinar = "BROMA"

tiempo = 0
intento = ""
veces = 0
resultado = []
hayLetra= []

dificultad = int(input("Elegí el nivel de dificultad: 1, 2 o 3: "))

if dificultad == 1:
    tiempoElegido = 600
    print("Tenés 10 minutos.")
elif dificultad == 2:
    tiempoElegido = 300
    print("Tenés 5 minutos")
elif dificultad == 3:
    tiempoElegido = 120
    print("Tenés 2 minutos")

print("Referencias:")
print("'=': Letra en posición correcta")
print("'-': Letra en posición incorrecta")
print("'_': Letra incorrecta")

inicio = time.perf_counter()

while veces <= 5:
    while tiempo < tiempoElegido:
        intento = str(input("Ingresá la palabra que quieras probar: "))
        intento = intento.upper()
        posicion = 0
        for letra in intento:
            resultado.append(letra)
            if letra in adivinar:
                if intento[posicion] == adivinar[posicion]:
                    hayLetra.append("=")
                else:
                    hayLetra.append("-")       
            else:
                hayLetra.append("_")
            posicion += 1

        veces += 1
        print(resultado)
        print(hayLetra)
        print("Intentos: ", veces, "de 6")

        if intento == adivinar:
            print("Adivinaste!")
            puntaje = 5 - (veces-1)
            print("Puntaje: ", puntaje, "/ 6")
            veces = 6
            
        intento = ""
        resultado = []
        hayLetra = []

        fin = time.perf_counter()
        tiempo = fin - inicio
        print("Transcurrió: ", tiempo, " segundos.")

        if tiempo > tiempoElegido:
            print("Se acabó el tiempo!")
            veces=6