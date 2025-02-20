# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        """"
        Created on : 02/19/2024
        Created By : Deval Jagad
        Purpose : Avoid Customer confirm of sale order if the customer has passed their credit limit.
        """
        for order in self:
            partner = order.partner_id
            if partner.credit_limit and partner.credit + partner.overdue_amount > partner.credit_limit:
                raise exceptions.UserError(
                    "Credit limit exceeded! Cannot confirm the sale order.\n"
                    f"Customer: {partner.name}\n"
                    f"Credit Limit: {partner.credit_limit}\n"
                    f"Current Credit: {partner.credit}\n"
                    f"Overdue Amount: {partner.overdue_amount}"
                )
        return super(SaleOrder, self).action_confirm()