# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.depends('invoice_ids')
    def _compute_overdue_amount(self):
        """"
        Created on : 02/19/2024
        Created By : Deval Jagad
        Purpose : The "amount overdue" used for this calculation should not include
                  any amounts unless they are unpaid past the date required by the payment terms.
        """
        for partner in self:
            overdue_amount = 0.0
            invoices = self.env['account.move'].search([
                ('partner_id', '=', partner.id),
                ('move_type', '=', 'out_invoice'),
                ('state', '=', 'posted'),
                ('payment_state', 'in', ['not_paid', 'partial'])
            ])
            for invoice in invoices:
                if invoice.invoice_date_due and fields.Date.today() > invoice.invoice_date_due:
                    overdue_amount += invoice.amount_residual
            partner.overdue_amount = overdue_amount

    overdue_amount = fields.Monetary(string="Overdue Amount", compute=_compute_overdue_amount, store=True,
                                     currency_field='currency_id')
