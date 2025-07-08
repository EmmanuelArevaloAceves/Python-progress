from fabrica import DocumentFactory
from contador import DocumentCounter

def main():
    while True:
        print("\n===== MENÚ DE DOCUMENTOS =====")
        print("1. Crear documento")
        print("2. Ver número de documentos creados")
        print("3. Salir")

        option = input("Selecciona una opción (1-3): ")

        if option == "1":
            tipo = input("Ingresa tipo de documento (pdf, word, text): ").strip().lower()
            try:
                documento = DocumentFactory.create_document(tipo)
                print(documento.leer())
            except ValueError as e:
                print(e)
        elif option == "2":
            contador = DocumentCounter()
            print(f" Total de documentos creados: {contador.getcounter()}")
        elif option == "3":
            print("¡Gracias por usar el sistema de documentos!")
            break
        else:
            print("Opcion no valida ingrese una opcion valida")

if __name__ == "__main__":
    main()