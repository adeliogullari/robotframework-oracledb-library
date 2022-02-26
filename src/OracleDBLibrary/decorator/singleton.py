from threading import Lock


class Singleton:

    def __init__(self, cls):
        self.cls = cls
        self.lock = Lock()
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            with self.lock:
                if self.instance is None:
                    self.instance = self.cls(*args, **kwargs)
        return self.instance
