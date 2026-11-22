class QFError(Exception):
    """Errore con una chiave di traduzione al posto del messaggio."""

    def __init__(self, key, **params):
        super().__init__(key)
        self.key = key
        self.params = params
