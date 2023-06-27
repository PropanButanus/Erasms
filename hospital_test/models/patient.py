# -*- coding: utf-8 -*-
from odoo import api, fields, models

class Hospitalpatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital records"

    name = fields.Char(string='Name', required="true")
    age = fields.Integer(string="Age")
    is_child = fields.Boolean(string="Is child?")
    notes = fields.Text(string="Notes")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string="Gender")