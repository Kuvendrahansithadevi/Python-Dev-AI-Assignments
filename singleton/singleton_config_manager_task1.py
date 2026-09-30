from config_manager import ConfigManager


class FileBasedConfigurationManager(ConfigManager):

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FileBasedConfigurationManager, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            super().__init__()
            self._initialized = True

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    @classmethod
    def reset_instance(cls):
        cls._instance = None

    def get_configuration(self, key, value_type=None):
        if key not in self.properties:
            return None

        val = self.properties[key]
        if value_type is None:
            return val

        try:
            return value_type(val)
        except (ValueError, TypeError):
            return val

    def set_configuration(self, key, value):
        self.properties[key] = value

    def remove_configuration(self, key):
        self.properties.pop(key, None)

    def clear(self):
        self.properties.clear()