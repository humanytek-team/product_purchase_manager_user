# -*- coding: utf-8 -*-
# Copyright 2018 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from openerp import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    env_user_is_purchase_manager = fields.Boolean(
        string='Is a purchase manager?',
        compute='_compute_is_purchase_manager',
        search='_search_env_user_is_purchase_manager')

    def _compute_is_purchase_manager(self):
        """ Computes value of field env_user_is_purchase_manager """

        for pr in self:
            pr.env_user_is_purchase_manager = self.user_has_groups(
                'purchase.group_purchase_manager')

    def _search_env_user_is_purchase_manager(self, operator, value):
        """ Computes the search operation in field 
        env_user_is_purchase_manager"""

        product_ids = list()
        env_user_is_purchase_manager = self.user_has_groups(
            'purchase.group_purchase_manager')
        if env_user_is_purchase_manager:
            product_ids = self.search([]).mapped('id')
        return [('id', 'in', product_ids)]
