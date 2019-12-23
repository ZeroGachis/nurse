from unittest import TestCase
import nurse


class SimpleInterface:
    def simple_abc_method(self):
        return 'interface result'


class SimpleDep:
    @staticmethod
    def simple_method():
        return 'simple dep result'


class SimpleDepWithInterface(SimpleInterface):
    def simple_abc_method(self):
        return 'impl result'


@nurse.inject
class MyClass:
    simple_dep: SimpleDep
    simple_dep_int: SimpleInterface


class TestServe(TestCase):
    def setUp(self) -> None:
        nurse.serve(SimpleDep())
        nurse.serve(SimpleDepWithInterface(), name=SimpleInterface)
        self.my_class = MyClass()

    def test_simple_dep_instance(self):
        assert isinstance(self.my_class.simple_dep, SimpleDep)

    def test_dep_inheritance_instance(self):
        assert isinstance(self.my_class.simple_dep_int, SimpleInterface)

    def test_simple_dep_returns_result(self):
        expected = 'simple dep result'
        result = self.my_class.simple_dep.simple_method()
        assert expected == result

    def test_dep_with_interface_returns_impl_result(self):
        expected = 'impl result'
        result = self.my_class.simple_dep_int.simple_abc_method()
        assert expected == result
