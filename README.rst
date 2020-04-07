Nurse
=====

.. image:: https://img.shields.io/badge/license-public%20domain-ff69b4.svg
    :target: https://github.com/ZeroGachis/nurse#license


.. image:: https://img.shields.io/badge/pypi-v0.3.1-blue.svg
    :target: https://pypi.org/project/nurse/


Outline
~~~~~~~

1. `Overview <https://github.com/ZeroGachis/nurse#overview>`_
2. `Installation <https://github.com/ZeroGachis/nurse#installation>`_
3. `Usage <https://github.com/ZeroGachis/nurse#usage>`_
4. `License <https://github.com/ZeroGachis/nurse#license>`_


Overview
~~~~~~~~


**Nurse** is a **dependency injection framework** with a small API that uses
type annotations to manage dependencies in your codebase.


Installation
~~~~~~~~~~~~

**Nurse** is a Python3-only module that you can install via `Poetry <https://github.com/sdispater/poetry>`_

.. code:: sh

    poetry add nurse


It can also be installed with `pip`

.. code:: sh

    pip3 install nurse


Usage
~~~~~

**Nurse** stores the available dependencies into a service catalog, that needs to be
filled-in generally at the startup of your application.

.. code:: python3

    import nurse
    
    # A user defined class that will be used accross your application
    class Player:
        
        @property
        def name(self) -> str:
            return "Leeroy Jenkins"

    # Now, add it to nurse service catalog in order to use it later in your application
    nurse.serve(Player())

By default, dependencies are referenced by their concrete type, but you can also serve them
via one of their parent class.

.. code:: python3

    import nurse

    class Animal:
        pass

    class AngryAnimal(Animal):

        @property
        def roar(self) -> str:
            return "Grrr! 🦁"

    nurse.serve(AngryAnimal(), through=Animal)

Once you filled-in the service catalog with your different components, your can declare them as dependencies
to any of your class.

.. code:: python3

    @nurse.inject("player")
    class Game:
        player: Player
        enemy: Animal

        def welcome_hero(self):
            print(f"Welcome {self.player.name} !")
    
        def summon_monster(self):
            print(self.enemy.roar)

    Game = Game()
    game.welcome_hero()
    # Welcome Leeroy Jenkins !
    game.summon_monster()
    # Grrr! 🦁


Or in any function

.. code:: python3

    @nurse.inject('enemy')
    def summon_monster(enemy: Animal):
        print(enemy.roar)

    summon_monster()
    # Grrr! 🦁


And it works with async function as well !

.. code:: python3

    import asyncio

    @nurse.inject('enemy')
    async def summon_monster(enemy: Animal):
        print(enemy.roar)

    asyncio.run(summon_monster())
    # Grrr! 🦁


Finally, you can also retrieve a service without using a decorator

.. code:: python3

    enemy = nurse.get(Animal)
    print(enemy.roar)
    # Grrr! 🦁


License
~~~~~~~

**Nurse** is released into the Public Domain. 🎉
