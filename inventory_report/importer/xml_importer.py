from inventory_report.inventory.inventory import Inventory
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(file):
        if file.endswith(".xml"):
            return Inventory.read_xml_file(file)
        else:
            raise ValueError("Arquivo inválido")
