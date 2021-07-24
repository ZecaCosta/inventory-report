from collections.abc import Iterator


class InventoryIterator(Iterator):
    @classmethod
    def __init__(cls, iterable_object):
        cls.iterable_object = iterable_object
        cls.element = 0

    def __next__(cls):
        try:
            data = cls.iterable_object[cls.element]
        except IndexError:
            raise StopIteration()
        else:
            cls.element += 1
            return data
