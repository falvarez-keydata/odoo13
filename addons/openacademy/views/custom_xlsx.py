from odoo import models
# from odoo.addons..addons.report_xlsx.report.report_xlsx import ReportXlsx
# from odoo import ReportXlsx

# from addons.report_xlsx.report.report_xlsx import ReportXlsx

class CustomXLS(models.AbstractModel):
# class CustomXLS(ReportXlsx):
    _name = 'report.openacademy.report_custom_template_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        # print ("lines",lines, data)
        # format1 = workbook.add.format({'font_size':14,'align':'vcenter','bold':True})
        # format2 = workbook.add.format({'font_size':10,'align':'vcenter',})
        # sheet = workbook.add_worksheet('Report Excel prueba')
        workbook.add_worksheet('Excel prueba')
        
        # sheet.write(2, 2, 'Nombre', format1)
        # sheet.write(2, 3, lines., format2)
        # for obj in partners:
        #     report_name = obj.name
            # One sheet by partner
        # sheet = workbook.add_worksheet(report_name[:31])
        # bold = workbook.add_format({'bold': True})
        # sheet.write(0, 0, obj.name, bold)
#CustomXLS('report.openacademy.report_custom_template.xlsx', 'openacademy.session')        
#CustomXLS('report.openacademy.report_custom_template_xlsx','openacademy.report_custom_template_xlsx')