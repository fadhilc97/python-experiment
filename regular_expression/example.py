# in res.partner

@api.constrains('identity_no', 'identity_no_type_id')
def check_identity_id_field(self):
    prefix = self.identity_no[0]
    check_digit = self.identity_no[-1]
    validation_error_msg = ''

    if re.search('[^A-Za-z0-9]',self.identity_no):
        validation_error_msg += '- Identity No. must be valid both alphabets or numbers\n'
    if len(self.identity_no) > 12:
        validation_error_msg += '- Identity No. must be maximum 12 characters length\n'

    if re.search('[0-9]', check_digit):
        validation_error_msg += '- Check digit in \'Identity No.\' field must be in alphabet letters\n'
    if re.search('[a-z]', check_digit):
        validation_error_msg += '- Check digit in \'Identity No.\' must be in uppercase\n'

    if self.identity_no_type_id.iras_code in [1, 2, 8]:
        numeric = self.identity_no[1:len(self.identity_no)-1]
        if re.search('[a-z]', prefix):
            validation_error_msg += '- Prefix in \'Identity No.\' must be in uppercase\n'
        if re.search('[^0-9]', numeric):
            validation_error_msg += '- Numeric in \'Identity No.\' must be in number\n'
        if self.identity_no_type_id.iras_code == 1 and prefix not in ['S', 'N']:
            validation_error_msg += '- NRIC in \'Identity No.\' must be prefix with S or N\n'
        if self.identity_no_type_id.iras_code == 2 and prefix not in ['G', 'F']:
            validation_error_msg += '- FIN in \'Identity No.\' must be prefix with G or F\n'
        if self.identity_no_type_id.iras_code == 8 and prefix not in ['A']:
            validation_error_msg += '- ASGD in \'Identity No.\' must be prefix with A\n'

    if self.identity_no_type_id.iras_code in [5, 10]:
        numeric = self.identity_no[:len(self.identity_no)-1]
        if re.search('[^0-9]', prefix) or re.search('[^0-9]', numeric):
            validation_error_msg += '- Invalid Identity Number Format\n'

    if self.identity_no_type_id.iras_code == 6:
        year_of_issuance = self.identity_no[:4]
        numeric = self.identity_no[4:len(self.identity_no)-1]
        if re.search('[^0-9]', year_of_issuance):
            validation_error_msg += '- Year of issuance in \'Identity No.\' must be in number\n'
        if re.search('[^0-9]', numeric):
            validation_error_msg += '- Numeric in \'Identity No.\' must be in number\n'

    if self.identity_no_type_id.iras_code == 35:
        year_of_issuance = self.identity_no[1:3]
        numeric = self.identity_no[5:len(self.identity_no)-1]
        if prefix not in ['T', 'S', 'R']:
            validation_error_msg += '- UEN-Others in \'Identity No.\' must be prefix with T, S, or R\n'
        if re.search('[^0-9]', year_of_issuance):
            validation_error_msg += '- Year of issuance in \'Identity No.\' must be in number\n'
        if self.identity_no[3] != 'P':
            validation_error_msg += '- 4th Character in \'Identity No.\' in UEN-Others must be letter P\n'
        if self.identity_no[4] != 'Q':
            validation_error_msg += '- 5th Character in \'Identity No.\' in UEN-Others must be letter Q\n'
        if re.search('[^0-9]', numeric):
            validation_error_msg += '- Numeric in \'Identity No.\' must be in number\n'

    if validation_error_msg != '':
       raise ValidationError(_(validation_error_msg))

@api.constrains('name')
def check_name_field(self):
    name = self.name
    split_name = self.name.split(' ')
    first_name = split_name[0]
    last_name = ' '.join(split_name[1:len(split_name)])
    validation_error_msg = ''

    if len(first_name) > 40:
        validation_error_msg += '- First name in \'Name\' field must be maximum 40 characters length\n'
    if len(last_name) > 40:
        validation_error_msg += '- Last name in \'Name\' field must be maximum 40 characters length\n'
    if re.search(',', name):
        validation_error_msg += '- Comma(s) in \'Name\' field are not allowed. Please remove from this particular field\n'
    if re.search('[^A-Za-z]', name):
        validation_error_msg += '- Name must be alphabet\n'

    if validation_error_msg != '':
        raise ValidationError(_(validation_error_msg))

@api.constrains('street', 'street2', 'city', 'zip')
def check_address_field(self):
    full_address = '{} {} {} {}'.format(self.street, self.street2, self.city, self.zip)
    validation_error_msg = ''

    if len(self.street) > 30:
        validation_error_msg += '- Address line 1 in \'Address\' field must be maximum 30 characters length\n'
    if len(self.street2) > 30:
        validation_error_msg += '- Address line 2 in \'Address\' field must be maximum 30 characters length\n'
    if len(self.city) > 30:
        validation_error_msg += '- City in \'Address\' field must be maximum 30 characters length\n'
    if len(self.zip) > 6:
        validation_error_msg += '- ZIP/Postal Code in \'Address\' field must be maximum 6 characters length\n'
    if re.search('[^0-9]', self.zip):
        validation_error_msg += '- ZIP/Postal Code in \'Address\' field must be valid with numeric\n'
    if re.search(',', full_address):
        validation_error_msg += '- Comma(s) in \'Address\' are not allowed. Please remove from this particular field\n'

    if validation_error_msg != '':
        raise ValidationError(_(validation_error_msg))
