from .service_catalog import ServiceCatalog
from typing import Callable
from nurse.exceptions import NurseError, ServiceNotFound


def serve[T](
    interface: type[T],
    *,
    factory: Callable[[], T] | None = None,
    singleton: T | None = None,
) -> None:
    """
    Register a service to nurse's catalog.
    """

    if factory is not None:
        service_factory = factory
    elif singleton is not None:
        service_factory = lambda: singleton  # noqa:E731
    else:
        raise NurseError("You must either provide `factory` or `singleton` parameter")

    key = interface.__qualname__
    ServiceCatalog.get_instance().services[key] = service_factory


def clear() -> None:
    """
    Remove all existing registered services
    """
    ServiceCatalog.get_instance().clear()


def get[T](interface: type[T]) -> T:
    """
    Retrieve a service from the service catalog.

    :Example:

    nurse.serve(SSHClient())

    ssh_client = nurse.get(SSHClient)
    """
    key = interface.__qualname__
    service_factory = ServiceCatalog.get_instance().services.get(key)
    if service_factory is None:
        raise ServiceNotFound(f"No service exists for '{interface.__class__}'")
    return service_factory()
