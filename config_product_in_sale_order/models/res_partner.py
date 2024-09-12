# -*- coding: utf-8 -*-

from odoo import models, fields, api, tools
from odoo.exceptions import UserError, ValidationError
import logging
logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    git_id_project = fields.Char('Git Project ID')
    git_name_project = fields.Char('Git Project Name')    
       