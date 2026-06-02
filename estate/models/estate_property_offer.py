from typing import Any, cast

from odoo import fields, models

_OFFER_STATUS_SELECTION = [
    ('accepted', 'Accepted'),
    ('refused', 'Refused'),
]


class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offer'

    price = fields.Float(string='Price')
    status = fields.Selection(
        selection=cast(Any, _OFFER_STATUS_SELECTION),
        string='Status',
        copy=False,
    )
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('real.estate', string='Property', required=True)
