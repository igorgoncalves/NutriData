
class Singleton(type):
    def __init__(cls, name, bases, notifications):
        super(Singleton, cls).__init__(name, bases, notifications)
        cls.instance = None 

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance


class NotificationServiceHelper(object):
    __metaclass__ = Singleton
    _notification_poll = []

    def add(self, notification):
        self._notification_poll.append(notification)
        return self._notification_poll
    
    def clear(self, notification):
        self._notification_poll = []
        return self._notification_poll


class Notification(object):
    key = ''
    value = {}

    def __init__(self, key: str, value: dict):
        self.key = key
        self.value = value
