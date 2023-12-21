# Copyright 2023 ForgeFlow S.L. (http://www.forgeflow.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class ProductProduct(models.Model):
    _name = "product.product"
    _inherit = ["product.product", "edi.exchange.consumer.mixin"]

    @api.model_create_multi
    def create(self, vals_list):
        self = self.with_context(skip_on_write_product_product=True)
        res = super().create(vals_list)
        if res:
            self._event("on_create_product_product").notify(res)
        return res

    def write(self, vals):
        res = super().write(vals)
        for product in self:
            if product._should_trigger_on_write_product_product(vals):
                self._event("on_write_product_product").notify(product)
        return res

    def unlink(self):
        self._event("on_unlink_product_product").notify(self)
        return super().unlink()

    def _should_trigger_on_write_product_product(self, vals):
        return (
            not isinstance(self.id, models.NewId)
            and not self._context.get("skip_on_write_product_product", False)
            and any(key in vals for key in self._get_exported_fields())
        )

    def _get_exported_fields(self):
        """
        This method will return the list of the exported fields through EDI flows
        """
        return []
