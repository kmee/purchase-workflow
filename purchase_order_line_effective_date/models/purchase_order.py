# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    last_effective_date = fields.Datetime(
        compute="_compute_last_effective_date",
        store=True,
        copy=False,
        help="Completion date of the last receipt of the order.",
    )

    @api.depends("order_line.last_effective_date")
    def _compute_last_effective_date(self):
        for order in self:
            order.last_effective_date = max(
                order.order_line.filtered("last_effective_date").mapped(
                    "last_effective_date"
                ),
                default=False,
            )
