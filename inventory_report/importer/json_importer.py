from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(file):
        if file.endswith(".json"):
            return Inventory.read_json_file(file)
        else:
            raise ValueError("Arquivo inválido")
