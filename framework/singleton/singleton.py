class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]

    @staticmethod
    def clear_all(*args, **kwargs):
        """Очищает все экземпляры классов-Singleton"""
        Singleton.__instances = {}

    def clear_instance(cls):
        """Очищает экземпляр определённого класса-Singleton"""
        _ = cls.__instances.pop(cls, None)
