# Copyright 2021 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PurchaseRequisition(models.Model):
    _inherit = "purchase.requisition"

    use_remaining_qty = fields.Boolean(
        string="Use Remaining Quantities",
        help="New quotations get the quantity of the agreement that is not yet "
        "proposed in other quotations or orders.",
    )
