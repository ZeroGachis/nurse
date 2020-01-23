class ServiceCatalog:
    """
    A singleton service catalog.
    """

    __slots__ = ("services",)
    instance = None

    def __init__(self) -> None:
        self.services = {}

    def clear(self) -> None:
        self.services.clear()

    @classmethod
    def get_instance(cls) -> "ServiceCatalog":
        if cls.instance is None:
            cls.instance = cls()

        return cls.instance
