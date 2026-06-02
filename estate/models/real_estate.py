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
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    user_id = fields.Many2one(
        'res.users',
        string='Salesperson',
        default=lambda self: self.env.user,
    )
    property_type_id = fields.Many2one(comodel_name='estate.property.type', string='Property Type')
    offer_ids = fields.One2many(comodel_name='estate.property.offer', inverse_name='property_id', string='Offers')
    tag_ids = fields.Many2many(comodel_name='estate.property.tag', string='Tags')