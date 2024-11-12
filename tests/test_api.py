from unittest import TestCase
import nurse
import pytest

from nurse.exceptions import DependencyError
import asyncio


class TestServe(TestCase):
    def tearDown(self):
        super().tearDown()
        nurse.clear()

    def test_can_inject_a_dependency(self):
        class User:
            @property
            def name(self):
                return "Leroy Jenkins"

        nurse.serve(User())

        @nurse.inject("player")
        class Game:
            player: User

        game = Game()
        assert game.player.name == "Leroy Jenkins"

    def test_can_inject_a_dependency_through_an_interface(self):
        class User:
            @property
            def name(self):
                return "Leroy Jenkins"

        class Cheater(User):
            @property
            def name(self):
                return "Igor"

        nurse.serve(Cheater(), through=User)

        @nurse.inject("player")
        class Game:
            player: User

        game = Game()
        assert game.player.name == "Igor"

    def test_cannot_serve_a_dependency_if_it_does_not_subclass_the_provided_interface(
        self,
    ):
        class User:
            @property
            def name(self):
                return "Leroy Jenkins"

        class Animal:
            @property
            def name(self):
                return "Miaouss"

        with pytest.raises(ValueError):
            nurse.serve(Animal(), through=User)


class ServiceDependency:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class TestInjectMethod(TestCase):
    def tearDown(self):
        super().tearDown()
        nurse.clear()

    def test_methods_with_only_dependency_args(self):
        @nurse.inject("service")
        def foo(service: ServiceDependency):
            return service.get_name()

        nurse.serve(ServiceDependency("Leroy Jenkins"))

        assert foo() == "Leroy Jenkins"

    def test_methods_with_dependency_and_value_args(self):
        @nurse.inject("service")
        def foo(prefix, service: ServiceDependency):
            return prefix + service.get_name()

        nurse.serve(ServiceDependency("Leroy Jenkins"))

        assert foo("My name is ") == "My name is Leroy Jenkins"

    def test_methods_with_missing_type(self):
        @nurse.inject("service")
        def foo(service):
            pass

        with pytest.raises(
            DependencyError, match="Args `service` must be typed to be injected."
        ):
            foo()

    def test_methods_with_missing_dependency(self):
        @nurse.inject("service")
        def foo(service: ServiceDependency):
            pass

        with pytest.raises(
            DependencyError,
            match="Dependency `ServiceDependency` for `service` was not found.",
        ):
            foo()

    def test_async_method(self):
        @nurse.inject("service")
        async def foo(service: ServiceDependency):
            return service.get_name()

        nurse.serve(ServiceDependency("Leroy Jenkins"))

        res = asyncio.run(foo())

        assert res == "Leroy Jenkins"


class TestGet(TestCase):
    def tearDown(self):
        super().tearDown()
        nurse.clear()

    def test_retrieve_service(self):
        nurse.serve(ServiceDependency("Leroy Jenkins"))

        service = nurse.get(ServiceDependency)
        assert service.get_name() == "Leroy Jenkins"

    def test_returns_none_if_service_is_not_registered(self):
        service = nurse.get(ServiceDependency)
        assert service is None
