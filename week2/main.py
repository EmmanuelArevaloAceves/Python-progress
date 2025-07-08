from sale import *
from Product_galery import *
from Movie_price import*

def factura(store):
    print("------------- FACTURA -------------")
    while True:
        entrada = input("Ingresa el ID del producto y la cantidad separados por una coma (ej. 1,2): ")

        try:
            product_id_str, quantity_str = entrada.split(",")
            product_id = int(product_id_str.strip())
            quantity = int(quantity_str.strip())
        except ValueError:
            print("Entrada inválida. Intenta de nuevo con el formato correcto.\n")
            continue

        store.sell_product(product_id, quantity)

        valor = input("¿Deseas agregar más productos? SI (S) / NO (N): ").strip().upper()
        if valor != "S":
            sales = store.total_sales
            print(f"\nLa cantidad a pagar es: ${sales:.2f}")
            break


while True:
    print("\n===== Ingrese qué quiere hacer =====")
    print("1. Ejecutar ejercicio 1 (Descuentos)")
    print("2. Ejecutar ejercicio 2 (Punto de venta)")
    print("3. Ejecutar ejercicio 3 (Pendiente)")
    print("4. Salir")

    option = input("Selecciona una opción (1-4): ")

    if option == "1":
        print(
            "\n             -- TABLA DE DESCUENTOS-- \n\n"
            "si el monto es menor a 100 no es aplicable a descuento\n"
            "Bola blanca                   *no aplica a descuento*\n"
            "Bola roja--------------------------*10% de descuento*\n"
            "Bola azul--------------------------*20% de descuento*\n"
            "Bola verde-------------------------*25% de descuento*\n"
            "Bola amarilla----------------------*50% de descuento*\n"
        )
        monto = float(input("Ingresa el monto: "))
        sale(monto)


    elif option == "2":
        store = Store()

        while True:
            print("\n===== PUNTO DE VENTA =====")
            print("1. Agregar producto")
            print("2. Ver productos existentes")
            print("3. Agregar cantidad a productos")
            print("4. Eliminar cantidad a productos")
            print("5. Factura")
            print("6. Regresar al menú principal")

            sub_option = input("Selecciona una opción (1-6): ")

            if sub_option == "1":
                entrada = input("Descripción, precio, cantidad (ej: Pan,25,10): ")
                try:
                    description, price, quantity = entrada.split(",")
                    price = float(price.strip())
                    quantity = int(quantity.strip())
                    store.add_product(description.strip(), price, quantity)
                except ValueError:
                    print("Entrada inválida. Asegúrate de separar con comas.")

            elif sub_option == "2":
                store.show_product()

            elif sub_option == "3":
                entrada = input("ID de producto, cantidad a sumar (ej: 2,5): ")
                try:
                    product_id_str, new_quantity_str = entrada.split(",")
                    product_id = int(product_id_str.strip())
                    new_quantity = int(new_quantity_str.strip())
                    store.add_inventory_product(product_id, new_quantity)
                except ValueError:
                    print("Entrada inválida. Usa el formato correcto, por ejemplo: 1,3")

            elif sub_option == "4":
                entrada = input("ID de producto, cantidad a restar (ej: 2,5): ")
                try:
                    product_id_str, remove_quantity_str = entrada.split(",")
                    product_id = int(product_id_str.strip())
                    remove_quantity = int(remove_quantity_str.strip())
                    store.delete_inventory_product(product_id, remove_quantity)
                except ValueError:
                    print("Entrada inválida. Usa el formato correcto, por ejemplo: 1,3")

            elif sub_option == "5":
                factura(store)

            elif sub_option == "6":
                break

            else:
                print("Opción inválida. Intenta de nuevo.")


    elif option == "3":

           print("CATEGORÍA    |  PRECIO  | CÓDIGO  | RECARGO/DÍA")
           print("Favoritos       $2.50      1         $0.50")
           print("Nuevos          $3.00      2         $0.75")
           print("Estrenos        $3.50      3         $1.00")
           print("SuperEstrenos   $4.00      4         $1.50\n")

           categoria = input("Introduce el código de la categoría (1-4): ")
           try:
                  retraso = int(input("Introduce el número de días de atraso: "))
                  pricing_table_movie(categoria, retraso)

           except ValueError:
                  print("Entrada inválida. El número de días debe ser un entero.")

    elif option == "4":
           print("Gracias por usar el sistema. ¡Hasta luego!")
           break


    else:
           print("Opción inválida. Intenta de nuevo.")





