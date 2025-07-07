class Task:

    id_counter = 1
    def __init__(self, description):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.completed = False
        self.description = description

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "[✔]" if self.completed else "[ ]"
        return f"{status} {self.id} - {self.description}"



