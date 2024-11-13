from dataclasses import dataclass
from unittest import TestCase
import nurse
import pytest


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

        @dataclass
        class Game:
            player: User

        user = nurse.get(User)
        game = Game(user)
        assert game.player.name == "Leroy Jenkins"

    def test_can_inject_a_dependency_through_an_interface(self):
        class User:
            @property
            def name(self) -> str:
                return "Leroy Jenkins"

        class Cheater(User):
            @property
            def name(self) -> str:
                return "Igor"

        nurse.serve(Cheater(), through=User)

        @dataclass
        class Game:
            player: User

        user = nurse.get(User)
        game = Game(user)
        assert game.player.name == "Igor"

    def test_cannot_serve_a_dependency_if_it_does_not_subclass_the_provided_interface(
        self,
    ):
        class User:
            @property
            def name(self) -> str:
                return "Leroy Jenkins"

        class Animal:
            @property
            def name(self) -> str:
                return "Miaouss"

        with pytest.raises(ValueError):
            nurse.serve(Animal(), through=User)


class ServiceDependency:
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name


class TestGet(TestCase):
    def tearDown(self):
        super().tearDown()
        nurse.clear()

    def test_retrieve_service(self):
        nurse.serve(ServiceDependency("Leroy Jenkins"))

        service = nurse.get(ServiceDependency)
        assert service is not None
        assert service.get_name() == "Leroy Jenkins"

    def test_returns_none_if_service_is_not_registered(self):
        with pytest.raises(nurse.ServiceNotFound):
            nurse.get(ServiceDependency)
