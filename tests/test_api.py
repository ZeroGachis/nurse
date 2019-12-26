import nurse
import pytest


class TestServe:

    def test_can_inject_a_dependency(self):
        class User:
            @property
            def name(self):
                return "Leroy Jenkins"

        nurse.serve(User())

        @nurse.inject
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

        @nurse.inject
        class Game:
            player: User

        game = Game()
        assert game.player.name == "Igor"

    def test_cannot_serve_a_dependency_if_it_does_not_subclass_the_provided_interface(self):
        class User:
            @property
            def name(self):
                return "Leroy Jenkins"

        class Animal:
            @property
            def name(self):
                return "Miaouss"

        with pytest.raises(ValueError) as ctx:
            nurse.serve(Animal(), through=User)
