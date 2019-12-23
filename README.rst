Nurse
=====

.. image:: https://img.shields.io/badge/license-public%20domain-ff69b4.svg
    :target: https://github.com/ZeroGachis/nurse#license


.. image:: https://img.shields.io/badge/pypi-v0.3-blue.svg
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
        
        def name(self, name) -> str:
            return "John Doe"
    
    # Now, add it to nurse service catalog in order to use it later in your application
    nurse.serve(Player())

**Nurse** allows you to abstract dependencies through an optional name parameter allowing you to refer your class instance
through its interface.

.. code:: python3

    import nurse

    # A user defined class that will be used accross your application
    class Player(User):

        def name(self) -> str:
            return "John Doe"

    # Now, add it to nurse service catalog in order to use it later in your application
    nurse.serve(Player(), name=User)

Once you filled-in the service catalog with your different component, your can declare them as dependencies
to any of your class.

.. code:: python3

    import nurse

    @nurse.inject
    class Game:
        player: Player

        def response(self) -> str:
            return f"Hello {self.player.name()} !"
    

    Game = Game()
    game.response()
    # Hello John Doe !


License
~~~~~~~

**Nurse** is released into the Public Domain. 🎉
