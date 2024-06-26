class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # logger_mqtt.debug('singleton: __call__')
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,
                                        cls).__call__(*args, **kwargs)
        return cls._instances[cls]
