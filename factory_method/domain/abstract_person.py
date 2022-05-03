from abc import ABC, abstractmethod


class Person(ABC):

    @abstractmethod
    def do_post(self):
        pass
