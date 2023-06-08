class WorkedHours:
    # esto se llama cuando se crea una instancia del objeto, es decir, haces WorkedHours(...)
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    # esto se llama cuando usas la función repr. Esto también es llamado por la función str cuando el método __str__ no está implementado.
    def __repr__(self):
        return ":".join((str(self.hours), str(self.minutes).zfill(2), str(self.seconds).zfill(2)))