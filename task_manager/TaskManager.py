from Task import *

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)
        print(f"Tarea agregada con ID {new_task.id}: '{new_task.description}'")

    def mark_complete(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_complete()
                print(f"Tarea {task_id} marcada como completada.")
                return
        print("No se encontró la tarea con ese ID.")

    def view_tasks(self):
        if not self.tasks:
            print("No hay tareas registradas.")
            return

        print("\n--- Lista de tareas ---")
        for task in self.tasks:
            print(task)

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print(f"Tarea con ID {task_id} eliminada.")
                return
        print("No se encontró la tarea con ese ID.")