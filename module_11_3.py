import inspect
from pprint import pprint


class ClassA:
    ATTR_A_0: str = 'String'

    def __init__(self):
        self.attr_a_1 = 1
        self.attr_a_2 = None

    def method_a_1(self):
        return self

    def introspection_info(self):
        info = {'type': type(self),
                'methods': [method for method in dir(self) if callable(getattr(self, method))],
                'attributes': [attr for attr in dir(self) if not callable(getattr(self, attr))],
                'module': inspect.getmodule(self) if inspect.getmodule(self) else None}
        return info


class ClassB(ClassA):
    def __init__(self):
        super().__init__()
        self.attr_b_1 = 1.1

    def method_b_1(self):
        return self


class ClassC(ClassB):
    def __init__(self):
        super().__init__()
        self.attr_c_1 = [1, 'two', 3]

    def method_c_1(self):
        return self


a = ClassA()
b = ClassB()
c = ClassC()
d = 0
e = 1.08
f = 'string'

object_info = ClassA.introspection_info(c)
pprint(object_info, sort_dicts=False)
