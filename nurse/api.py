from typing import List

from nurse.exceptions import DependencyError
from .service_catalog import ServiceCatalog


def inject(*items_to_inject: List[str]):
    """
    A decorator that injects dependencies into every instances of a user-defined class or method

    :Example:

    class SSHClient:

        def connect(self):
            pass

    @nurse.inject('ssh_client')
    class Server:
        ssh_client: SSHClient

    server = Server()
    server.ssh_client.connect()

    @nurse.inject('client')
    def send(client: SSHClient):
        client.send("Hello World !")

    nurse.serve(SSHClient())
    send()
    """

    def decorator(decorated):
        service_catalog = ServiceCatalog.get_instance()
        if isinstance(decorated, type):
            return inject_class(decorated, service_catalog, items_to_inject)
        elif callable(decorated):
            return inject_method(decorated, service_catalog, items_to_inject)

        raise NotImplementedError('user-defined class or method can be injected.')

    return decorator


def inject_class(decorated_class, service_catalog, field_to_inject):
    def init_decorator(self, *args, **kwargs):
        for param_to_inject in field_to_inject:
            service = get_service(service_catalog, decorated_class, param_to_inject)
            setattr(self, param_to_inject, service)

        return init_decorator.decorated_init(self, *args, **kwargs)

    init_decorator.decorated_init = decorated_class.__init__
    decorated_class.__init__ = init_decorator

    return decorated_class


def inject_method(decorated_func, service_catalog, args_to_inject):
    def decorator(*args, **kwargs):
        injected_args = {}
        for param_to_inject in args_to_inject:
            service = get_service(service_catalog, decorated_func, param_to_inject)
            injected_args.setdefault(param_to_inject, service)

        return decorated_func(*args, **injected_args, **kwargs)

    return decorator


def get_service(service_catalog: ServiceCatalog, decorated_obj: any, param_to_inject: str) -> any:
    service_type = decorated_obj.__annotations__.get(param_to_inject, None)
    if not service_type:
        raise DependencyError(f'Args `{param_to_inject}` must be typed to be injected.')

    service = service_catalog.services.get(service_type, None)
    if not service:
        raise DependencyError(f"Dependency `{service_type}` for `{param_to_inject}` was not found.")

    return service


def serve(user_class, through=None) -> None:
    """
    Add an instance of a user-defined class to Nurse's services catalog.
    By default, a dependency is registered for its concrete type, but an interface can be provided.

    :param user_class: User-defined class instance
    :param through: An interface used to access the user class
                   (must be a direct or indirect parent class)
    """

    through = through or user_class.__class__

    if not issubclass(user_class.__class__, through):
        raise ValueError(f"Class {user_class} must be a subclass of {through}.")

    ServiceCatalog.get_instance().services[through] = user_class


def clear() -> None:
    """
    Remove all existing registered services
    """
    ServiceCatalog.get_instance().clear()
