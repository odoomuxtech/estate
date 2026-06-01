from typing import Any, cast

from odoo import fields, models

_PROPERTY_TYPE_SELECTION = [
    ('house', 'House'),
    ('apartment', 'Apartment'),
]


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
        selection=cast(Any, _PROPERTY_TYPE_SELECTION),
        string='Property Type',
    )