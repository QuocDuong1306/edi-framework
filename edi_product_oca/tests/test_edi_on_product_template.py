# Copyright 2023
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import _
from odoo.tests.common import tagged

from odoo.addons.component.core import Component
from odoo.addons.component.tests.common import TransactionComponentRegistryCase
from odoo.addons.product.tests.common import TestProductCommon


@tagged("-at_install", "post_install")
class EDIBackendTestCase2(TestProductCommon, TransactionComponentRegistryCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._setup_registry(cls)
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))

        class ProductTemplateEventListenerDemo(Component):
            _name = "product.template.event.listener.demo"
            _inherit = "base.event.listener"
            _apply_on = ["product.template"]

            def on_create_product_template(self, product):
                raise Warning(_("on_create_product_template method is triggered!"))

            def on_write_product_template(self, product):
                raise Warning(_("on_write_product_template method is triggered!"))

            def on_unlink_product_template(self, product):
                raise Warning(_("on_unlink_product_template method is triggered!"))

        ProductTemplateEventListenerDemo._build_component(cls.comp_registry)
        cls.comp_registry._cache.clear()

    def test_create_product_template(self):
        with self.assertRaisesRegex(
            Warning, "on_create_product_template method is triggered!"
        ):
            self.env["product.template"].create(
                [
                    {
                        "name": "Product",
                    }
                ]
            )

    def test_on_write_product_template(self):
        with self.assertRaisesRegex(
            Warning, "on_write_product_template method is triggered!"
        ):
            self.product_1.write({"name": "Test"})

    def test_unlink_product_template(self):
        with self.assertRaisesRegex(
            Warning, "on_unlink_product_template method is triggered!"
        ):
            self.product_1.unlink()
