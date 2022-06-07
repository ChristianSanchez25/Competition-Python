class EmptyFile (Exception):
    """
        Custom Exception para manejar los errores de archivos vacios
    """
    
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

class IncompleteParticipantData (Exception):
    """
        Custom Exception para manejar los errores de datos incompletos
    """
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

