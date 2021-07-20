from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @classmethod
    def import_data(cls, filepath, report_type):
        if(filepath.endswith('.csv')):
            product_list = cls.read_csv_file(filepath)
        elif(filepath.endswith('.json')):
            product_list = cls.read_json_file(filepath)
        # elif(filepath.endswith('.xml')):
            # product_list = cls.read_xml_file(filepath)
        return cls.select_report_type(product_list, report_type)

    @classmethod
    def select_report_type(cls, product_list, report_type):
        if report_type == "completo":
            return CompleteReport.generate(product_list)
        elif report_type == "simples":
            return SimpleReport.generate(product_list)

    @classmethod
    def read_json_file(cls, filepath):
        with open(filepath, 'r') as file:
            return json.load(file)

    @classmethod
    def read_csv_file(cls, filepath):
        product_list = []
        with open(filepath, 'r') as file:
            csvReader = csv.DictReader(file)
            for rows in csvReader:
                product_list.append(rows)
        return product_list

    # @classmethod
    # def read_xml_file(cls, filepath):
