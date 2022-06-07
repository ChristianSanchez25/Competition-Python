
class WrongOption (Exception):
    """
        Custom Exception para manejar los errores de opcion equivocada
    """
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message

