from TaskManager import TaskManager

task_manager = TaskManager()

while True:
    print("\n===== ADMINISTRADOR DE TAREAS =====")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

    option = input("Selecciona una opción (1-5): ")

    if option == "1":
        desc = input("Descripción de la tarea: ")
        task_manager.add_task(desc)
    elif option == "2":
        task_manager.view_tasks()
    elif option == "3":
        task_id = int(input("ID de la tarea a completar: "))
        task_manager.mark_complete(task_id)
    elif option == "4":
        task_id = int(input("ID de la tarea a eliminar: "))
        task_manager.delete_task(task_id)
    elif option == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")