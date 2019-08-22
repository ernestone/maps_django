class MapsRouter:
    """
    A router to control all database operations on models in the
    Maps application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read Maps models go to Db_postgis.
        """
        if model._meta.app_label == 'maps':
            return 'db_postgis'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write maps models go to db_postgis.
        """
        if model._meta.app_label == 'maps':
            return 'db_postgis'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the maps app is involved.
        """
        if obj1._meta.app_label == 'maps' or \
           obj2._meta.app_label == 'maps':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the maps app only appears in the 'db_postgis'
        database.
        """
        if app_label == 'maps':
            return db == 'db_postgis'
        return None