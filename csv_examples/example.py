class WizardIrasExportCsv(models.TransientModel):
    _name = 'wizard.iras.export.csv'
    _description = 'Download IRAS CSV Report'
    
    file = fields.Binary('Click To Download CSV File', readonly = True)
    name = fields.Char('Name', default='iras_export.csv')
    
def action_export(self):
#        csv_data = io.BytesIO()
    with open('iras_report.csv', 'w+') as csv_writer_file:
        writer = csv.writer(csv_writer_file, delimiter=',')
        writer.writerow(['1', '2', '3', '4', '5'])
        writer.writerow(['a', 'b', 'c', 'd', 'e'])

    csv_reader_file = open('iras_report.csv', 'rb')
    csv_reader_file.seek(0)
    data = csv_reader_file.read()
    res = base64.encodestring(data)
#        csv_data.close()
    module_rec = self.env['wizard.iras.export.csv'].create({'name': 'IRAS Report.csv', 'file' : res})
    return {
      'name': _('IRAS Export to CSV'),
      'res_id' : module_rec.id,
      'view_type': 'form',
      "view_mode": 'form',
      'res_model': 'wizard.iras.export.csv',
      'type': 'ir.actions.act_window',
      'target': 'new',
      }