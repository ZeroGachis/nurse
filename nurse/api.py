from .service_catalog import ServiceCatalog
from typing import TypeVar
from nurse.exceptions import ServiceNotFound

TDependencyInterface = TypeVar("TDependencyInterface")


def serve(
    service_instance: TDependencyInterface,
    through: type[TDependencyInterface] | None = None,
) -> None:
    """
    Add an instance of a user-defined class to Nurse's services catalog.
    By default, a dependency is registered for its concrete type, but an interface can be provided.

    :param user_class: User-defined class instance
    :param through: An interface used to access the user class
                   (must be a direct or indirect parent class)
    """
    if through is not None:
        _through = through
    else:
        _through = service_instance.__class__

    if not issubclass(service_instance.__class__, _through):
        raise ValueError(
            f"Service instance of type '{service_instance.__class__}' must be a subclass of {_through}."
        )

    ServiceCatalog.get_instance().services[_through] = service_instance


def clear() -> None:
    """
    Remove all existing registered services
    """
    ServiceCatalog.get_instance().clear()


def get(service_instance_class: type[TDependencyInterface]) -> TDependencyInterface:
    """
    Retrieve a service from the service catalog.

    :Example:

    nurse.serve(SSHClient())

    ssh_client = nurse.get(SSHClient)
    """
    service = ServiceCatalog.get_instance().services.get(service_instance_class)
    if service is None:
        raise ServiceNotFound(
            f"No service exists for '{service_instance_class.__class__}'"
        )
    return service
