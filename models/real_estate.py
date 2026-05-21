from odoo import fields, models


class RealEstateProperty(models.Model):
    _name = 'real.estate'
    _description = 'Real Estate Property'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price')
    bedrooms = fields.Integer(string='Bedrooms')
    bathrooms = fields.Integer(string='Bathrooms')
    area = fields.Float(string='Area')
    property_type = fields.Selection(
        selection=[('house', 'House'), ('apartment', 'Apartment')],
        string='Property Type',
    )