from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    @classmethod
    def __init__(cls, importer):
        cls.data = []
        cls.importer = importer

    def import_data(cls, filepath, report_type):
        list_inventory = cls.importer.import_data(filepath)
        cls.data.extend(list_inventory)
        return cls.select_report_type(cls.data, report_type)

    @classmethod
    def select_report_type(cls, data, report_type):
        if report_type == "completo":
            return CompleteReport.generate(data)
        elif report_type == "simples":
            return SimpleReport.generate(data)

    def __iter__(cls):
        return InventoryIterator(cls.data)
