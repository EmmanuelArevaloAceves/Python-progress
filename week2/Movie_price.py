
def pricing_table_movie (categoria, retraso):
    if categoria == "1":
        total = 2.50 + (retraso * .50)
        print(f"El total a pagar es: ${total:.2f}")
    elif categoria == "2":
        total = 3 + (retraso * .75)
        print(f"El total a pagar es: ${total:.2f}")
    elif categoria == "3":
        total = 3.50 + (retraso * 1)
        print(f"El total a pagar es: ${total:.2f}")
    elif categoria == "4":
        total = 4 + (retraso * 1.50)
        print(f"El total a pagar es: ${total:.2f}")
    else:
        print("Valor invalido ingrese un valor valido")
