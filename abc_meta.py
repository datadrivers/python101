import abc
# https://www.python.org/dev/peps/pep-3119/



class ParentFoo(abc.ABC):

    def __init__(self):
        self.__my_attr = None

    @abc.abstractmethod
    def dance(self):
        pass

    @property
    @abc.abstractmethod
    def my_attr(self):
        return self.__my_attr

    @my_attr.setter
    @abc.abstractmethod
    def my_attr(self, value):
        self.__my_attr = "foo"


class ChildFoo(ParentFoo):

    @property
    def my_attr(self):
        return

    def dance(self):
        """
        This does something
        :return:
        """
        return 42

    def __repr__(self):
        return "childfoo"

foo = ChildFoo()
foo
issubclass(ChildFoo, abc.ABC)

ChildFoo.__dict__
