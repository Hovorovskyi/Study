class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class Singleton1(object):
    _instance = 1

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


class Singleton2(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton2, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Object(metaclass=Singleton2):
    pass


if __name__ == '__main__':
    x = Object()
    y = Object()

    print(x is y)