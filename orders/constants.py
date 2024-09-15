class NotificationsConstants:
    """
    Constants cannot be changed at runtime
    """
    LOW_STOCK_LIMIT = 5
    RENOTIFY_AGE_LIMIT = 3

    def __setattr__(self, *args, **kwargs):
        raise Exception('''
            Constant values must NEVER be changed at runtime, as they are
            integral to the structure of notifications
            ''')


NotificationsConstants = NotificationsConstants()  # type: ignore
