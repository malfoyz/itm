class DocumentNotFoundException(Exception):
    """Исключение для случаев, когда документ не найден."""
    pass


class DocumentTextNotFoundException(Exception):
    """Исключение для случаев, когда текст документа не найден."""
    pass