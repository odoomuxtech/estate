from datetime import date, timedelta
from typing import Any, cast

from odoo import api, fields, models

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
    property_type_id = fields.Many2one(
        related='property_id.property_type_id',
        store=True,
    )
    create_date = fields.Datetime(string='Created on', readonly=True)
    validity = fields.Integer(string='Validity (days)', default=7)
    date_deadline = fields.Date(
        string='Deadline',
        compute='_compute_date_deadline',
        inverse='_inverse_date_deadline',
    )

    def _get_offer_base_date(self) -> date:
        self.ensure_one()
        if self.create_date:
            return self.create_date.date()
        return fields.Date.today()

    @api.depends('create_date', 'validity')
    def _compute_date_deadline(self):
        for offer in self:
            offer.date_deadline = offer._get_offer_base_date() + timedelta(days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            if offer.date_deadline:
                offer.validity = (offer.date_deadline - offer._get_offer_base_date()).days
