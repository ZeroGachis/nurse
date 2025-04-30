# Nurse 💉

**Nurse** is a small **dependency injection library**.

### Usage

**Nurse** stores the services into a service catalog that needs to be filled-in
generally at the edge of your application.

To serve a singleton instance of your service:

```python
import nurse

class Animal:
    def make_noise(self) -> str:
        return "..."

class AngryAnimal(Animal):
    def make_noise(self) -> str:
        return "Grrr! 🦁"


nurse.serve(Animal, singleton=AngryAnimal())

animal = nurse.get(Animal)
animal.make_noise()
# "Grrr! 🦁"
```

To serve a new instance of your service each time it's being retrieved:

```python
import nurse

class Animal:
    def make_noise(self) -> str:
        return "..."

class AngryAnimal(Animal):
    def make_noise(self) -> str:
        return "Grrr! 🦁"


nurse.serve(Animal, factory=AngryAnimal)

animal = nurse.get(Animal)
animal.make_noise()
# "Grrr! 🦁"
```
