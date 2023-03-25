
class ComputedProperty:
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.getter(instance)