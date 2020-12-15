class MailComposeInherit(models.TransientModel):
    _inherit = 'mail.compose.message'

    cc_partner_ids = fields.Many2many(
        'res.partner', 'mail_compose_message_cc_res_partner_rel',
        'wizard_id', 'partner_id', 'Recipients (CC)')

    @api.model
    def default_get(self, fields):
        res = super(MailComposeInherit, self).default_get(fields)
        context = self._context
        donor_id = context.get('default_donor_id',False) or context.get('donor_id',False)
        model_name = context.get('default_model') or context.get('model')
        if not donor_id and model_name:
            res_id = context.get('default_res_id') or context.get('res_id')
            if model_name == 'res.partner' and res_id:
                donor_id = res_id
            else:
                try:
                    model_obj = self.env[model_name]
                    if res_id: #should not add if model_obj since it is empty object and would return False
                        record = model_obj.browse(res_id)
                        donor = record and getattr(record,'partner_id',False) or False
                        if donor:
                            donor_id = donor.id or False
                except:
                    donor_id = False
        res['partner_ids'] = [(6, 0, [donor_id])]
        return res
    
    @api.onchange('cc_partner_ids')
    def onchange_cc_partner_ids(self):
        email_to = self.partner_ids
        email_cc = self.cc_partner_ids
        receivers = email_to + email_cc
        print("To :",email_to)
        print("Cc :",email_cc)
        print("Receivers :",receivers)