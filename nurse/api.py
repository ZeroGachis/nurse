from .service_catalog import ServiceCatalog


def inject(user_class):
    """
    A decorator that injects dependencies into every instances of a user-defined class.

    :Example:

    class SSHClient:

        def connect(self):
            pass

    @nurse.inject
    class Server:
        ssh_client: SSHClient

    server = Server()
    server.ssh_client.connect()
    """

    def constructor_with_dependency_injection(self, *args, **kwargs):
        service_catalog = ServiceCatalog.get_instance()
        dependencies = constructor_with_dependency_injection.user_class.__annotations__

        for service_name, service_type in dependencies.items():
            if service_type in service_catalog.services:
                instance = service_catalog.services[service_type]
            else:
                instance = service_type.__bases__[0]
            setattr(self, service_name, instance)

        return constructor_with_dependency_injection.user_init(self, *args, **kwargs)

    constructor_with_dependency_injection.user_class = user_class
    constructor_with_dependency_injection.user_init = user_class.__init__

    user_class.__init__ = constructor_with_dependency_injection

    return user_class


def serve(user_class, name=None) -> None:
    """
    Add an instance of a user-defined class to Nurse's services catalog.
    Given user_class is registered in the catalogue with its class name as key by default.

    :param user_class: User-defined class instance
    :param name: Optional name to define specific access key for given user_class
    """
    name = name or user_class.__class__
    ServiceCatalog.get_instance().services[name] = user_class
