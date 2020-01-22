import inspect

from nurse.exceptions import DependencyError
from .service_catalog import ServiceCatalog


def inject(*decorator_args):
    """
    A decorator that injects dependencies into every instances of a user-defined class or method

    :Example:

    class SSHClient:

        def connect(self):
            pass

    @nurse.inject
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

    def inject_class(class_to_inject):
        def init_decorator(self, *args, **kwargs):
            dependencies = class_to_inject.__annotations__

            for service_name, service_type in dependencies.items():
                setattr(self, service_name, service_catalog.services[service_type])

            return init_decorator.decorated_init(self, *args, **kwargs)

        init_decorator.decorated_init = class_to_inject.__init__
        class_to_inject.__init__ = init_decorator

        return class_to_inject

    def inject_method(decorated_func):
        def decorator(*args, **kwargs):
            injected_args = {}
            for param_to_inject in args_to_inject:
                service = get_service(param_to_inject, service_catalog)
                injected_args.setdefault(param_to_inject, service)

            return decorated_func(*args, **injected_args, **kwargs)

        def get_service(param_to_inject, service_catalog):
            service_type = decorated_func.__annotations__.get(param_to_inject, None)
            if not service_type:
                raise DependencyError(f'Args `{param_to_inject}` must be typed to be injected.')
            service = service_catalog.services.get(service_type, None)
            if not service:
                raise DependencyError(f"Dependency `{service_type}` for `{param_to_inject}` was not found.")
            return service

        return decorator

    service_catalog = ServiceCatalog.get_instance()
    if isinstance(decorator_args[0], str):
        args_to_inject = decorator_args
        return inject_method
    else:
        decorated_class = decorator_args[0]
        return inject_class(decorated_class)


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
