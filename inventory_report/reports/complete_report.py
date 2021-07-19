from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, report):
        simple_report = super().generate(report)

        companies = Counter(
            product["nome_da_empresa"] for product in report)

        format = "Produtos estocados por empresa: \n"

        for company in companies:
            format += f"- {company}: {companies[company]}\n"

        return (
            f"{simple_report}\n"
            f"{format}"
        )
