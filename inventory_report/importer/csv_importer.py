from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(file):
        if file.endswith(".csv"):
            return Inventory.read_csv_file(file)
        else:
            raise ValueError("Arquivo inválido")
