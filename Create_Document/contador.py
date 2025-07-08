class DocumentCounter:
    _instance = None
    counter = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.counter = 0
        return cls._instance

    def increment(self):
        self.counter += 1

    def getcounter(self):
        return self.counter