from unittest import TestCase
import nurse
import pytest


class TestNurse(TestCase):
    def tearDown(self):
        super().tearDown()
        nurse.clear()

    def test_singleton_dependency(self):
        class User:
            @property
            def name(self):
                return "Leroy Jenkins"

        nurse.serve(User, singleton=User())

        user1 = nurse.get(User)
        user2 = nurse.get(User)
        assert user1.name == "Leroy Jenkins"
        assert user2.name == "Leroy Jenkins"
        assert user1 is user2

    def test_singleton_subclass_dependency(self):
        class User:
            @property
            def name(self) -> str:
                return "Leroy Jenkins"

        class Cheater(User):
            @property
            def name(self) -> str:
                return "Igor"

        nurse.serve(User, singleton=Cheater())

        user1 = nurse.get(User)
        user2 = nurse.get(User)
        assert user1.name == "Igor"
        assert user2.name == "Igor"
        assert user1 is user2

    def test_factory(self):
        class User:
            @property
            def name(self) -> str:
                return "Leroy Jenkins"

        nurse.serve(User, factory=User)

        user1 = nurse.get(User)
        user2 = nurse.get(User)
        assert user1.name == "Leroy Jenkins"
        assert user2.name == "Leroy Jenkins"
        assert user1 is not user2

    def test_factory_with_subclass(self):
        class User:
            @property
            def name(self) -> str:
                return "Leroy Jenkins"

        class Cheater(User):
            @property
            def name(self) -> str:
                return "Igor"

        nurse.serve(User, factory=Cheater)

        user1 = nurse.get(User)
        user2 = nurse.get(User)
        assert user1.name == "Igor"
        assert user2.name == "Igor"
        assert user1 is not user2

    def test_raise_error_when_service_is_not_registered(self):
        class User:
            @property
            def name(self) -> str:
                return "Leroy Jenkins"

        with pytest.raises(nurse.ServiceNotFound):
            nurse.get(User)

    def test_must_serve_either_a_singleton_or_a_factory(self):
        class User:
            @property
            def name(self):
                return "Leroy Jenkins"

        with pytest.raises(nurse.NurseError):
            nurse.serve(User, singleton=None, factory=None)
