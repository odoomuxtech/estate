from datetime import timedelta
from typing import Any, cast

from odoo import api, fields, models
from odoo.tools.translate import _

_GARDEN_ORIENTATION_SELECTION = [
    ('north', 'North'),
    ('south', 'South'),
    ('east', 'East'),
    ('west', 'West'),
]


class RealEstateProperty(models.Model):
    _name = 'real.estate'
    _description = 'Real Estate Property'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    price = fields.Float(string='Price')
    bedrooms = fields.Integer(string='Bedrooms')
    bathrooms = fields.Integer(string='Bathrooms')
    living_area = fields.Float(string='Living Area')
    garden = fields.Boolean(string='Garden')
    garden_area = fields.Float(string='Garden Area')
    garden_orientation = fields.Selection(
        selection=cast(Any, _GARDEN_ORIENTATION_SELECTION),
        string='Garden Orientation',
    )
    date_availability = fields.Date(
        string='Available From',
        copy=False,
        default=lambda self: fields.Date.today() + timedelta(days=90),
    )
    total_area = fields.Float(string='Total Area', compute='_compute_total_area')
    best_price = fields.Float(string='Best Offer', compute='_compute_best_price')
    buyer_id = fields.Many2one('res.partner', string='Buyer', copy=False)
    user_id = fields.Many2one(
        'res.users',
        string='Salesperson',
        default=lambda self: self.env.user,
    )
    property_type_id = fields.Many2one(comodel_name='estate.property.type', string='Property Type')
    offer_ids = fields.One2many(comodel_name='estate.property.offer', inverse_name='property_id', string='Offers')
    tag_ids = fields.Many2many(comodel_name='estate.property.tag', string='Tags')

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(record.offer_ids.mapped('price'), default=0.0)

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False

    @api.onchange('date_availability')
    def _onchange_date_availability(self):
        if self.date_availability and self.date_availability < fields.Date.today():
            return {
                'warning': {
                    'title': _('Incorrect date'),
                    'message': _('The availability date cannot be in the past.'),
                },
            }