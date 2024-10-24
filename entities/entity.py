from utils.asset_manager import AssetManager


class Entity:
    def __init__(self):
        self.components = {}
        self.asset_manager = AssetManager()

    def add_component(self, component_type, component):
        self.components[component_type] = component

    def get_component(self, component_type):
        return self.components.get(component_type, None)
