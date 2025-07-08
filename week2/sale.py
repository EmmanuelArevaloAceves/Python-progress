import random

def sale(monto):
    if monto < 100:
        return print("El monto no aplica a descuento")
    else :
        bola = random.randint(1, 5)
        if bola == 1:
            print("Bola blanca")
        elif bola == 2:
            total = monto * .90
            print("Bola roja")
            print(f"Total a pagar: ${total:.2f}")
        elif bola == 3:
            total = monto * .80
            print("Bola azul")
            print(f"Total a pagar: ${total:.2f}")
        elif bola == 4:
            total = monto * .75
            print("Bola verde")
            print(f"Total a pagar: ${total:.2f}")
        elif bola == 5:
            total = monto * .50
            print("Bola amarilla")
            print(f"Total a pagar: ${total:.2f}")



