class NoneException(Exception):
    def __init__(self, message="Erro ao recuperar valor do dólar!."):
        super().__init__(message)
