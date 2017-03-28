# event.py (simple)
class Event(object):
    def __init__(self):
        self.handlers = []
    def add(self, handler):
        self.handlers.append(handler)
        return self
    def remove(self, handler):
        self.handlers.remove(handler)
        return self
    def fire(self, sender, earg=None):
        for handler in self.handlers:
            handler(sender, earg)
    __iadd__ = add
    __isub__ = remove
    __call__ = fire
    
class Event0(object):
    def __init__(self):
        self.handlers = []
    def add(self, handler):
        self.handlers.append(handler)
        return self
    def remove(self, handler):
        self.handlers.remove(handler)
        return self
    def fire(self, sender, earg=None):
        for handler in self.handlers:
            handler(sender, 0)
    __iadd__ = add
    __isub__ = remove
    __call__ = fire
    
class Event1(object):
    def __init__(self):
        self.handlers = []
    def add(self, handler):
        self.handlers.append(handler)
        return self
    def remove(self, handler):
        self.handlers.remove(handler)
        return self
    def fire(self, sender, earg=None):
        for handler in self.handlers:
            handler(sender, 1)
    __iadd__ = add
    __isub__ = remove
    __call__ = fire
    
class Event2(object):
    def __init__(self):
        self.handlers = []
    def add(self, handler):
        self.handlers.append(handler)
        return self
    def remove(self, handler):
        self.handlers.remove(handler)
        return self
    def fire(self, sender, earg=None):
        for handler in self.handlers:
            handler(sender, 2)
    __iadd__ = add
    __isub__ = remove
    __call__ = fire

class Event3(object):
    def __init__(self):
        self.handlers = []
    def add(self, handler):
        self.handlers.append(handler)
        return self
    def remove(self, handler):
        self.handlers.remove(handler)
        return self
    def fire(self, sender, earg=None):
        for handler in self.handlers:
            handler(sender, 3)
    __iadd__ = add
    __isub__ = remove
    __call__ = fire

class Event4(object):
    def __init__(self):
        self.handlers = []
    def add(self, handler):
        self.handlers.append(handler)
        return self
    def remove(self, handler):
        self.handlers.remove(handler)
        return self
    def fire(self, sender, earg=None):
        for handler in self.handlers:
            handler(sender, 4)
    __iadd__ = add
    __isub__ = remove
    __call__ = fire

class Event5(object):
    def __init__(self):
        self.handlers = []
    def add(self, handler):
        self.handlers.append(handler)
        return self
    def remove(self, handler):
        self.handlers.remove(handler)
        return self
    def fire(self, sender, earg=None):
        for handler in self.handlers:
            handler(sender, 5)
    __iadd__ = add
    __isub__ = remove
    __call__ = fire