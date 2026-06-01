from typing import Any, cast

from odoo import fields, models

_PROPERTY_TYPE_SELECTION = [
    ('house', 'House'),
    ('apartment', 'Apartment'),
]


class EstatePropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    property_type = fields.Selection(
        string='Property Type',
        selection=cast(Any, _PROPERTY_TYPE_SELECTION),
    )
