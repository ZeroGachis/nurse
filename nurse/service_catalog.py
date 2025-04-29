from typing import Any, Callable, Optional


class ServiceCatalog:
    """
    A singleton service catalog.
    """

    __slots__ = ("services",)
    instance: Optional["ServiceCatalog"] = None

    def __init__(self) -> None:
        self.services = dict[str, Callable[[], Any]]()

    def clear(self) -> None:
        self.services.clear()

    @classmethod
    def get_instance(cls) -> "ServiceCatalog":
        if cls.instance is None:
            cls.instance = cls()

        return cls.instance
