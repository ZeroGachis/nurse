class ServiceCatalog:
    """
	A singleton service catalog.
	"""

    __slots__ = ("services",)
    instance = None

    def __init__(self) -> None:
        self.services = {}

    @classmethod
    def get_instance(cls) -> "Services":
        if cls.instance is None:
            cls.instance = cls()

        return cls.instance
