class EmptyException(Exception):
    def __init__(self, message="Erro ao recuperar valores do select!."):
        super().__init__(message)
