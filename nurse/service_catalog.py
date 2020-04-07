class ServiceCatalog:
    """
    A singleton service catalog.
    """

    __slots__ = ("_services",)
    instance = None

    def __init__(self) -> None:
        self._services = {}

    def clear(self) -> None:
        self._services.clear()

    @classmethod
    def get_instance(cls) -> "ServiceCatalog":
        if cls.instance is None:
            cls.instance = cls()

        return cls.instance
