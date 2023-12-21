This module intends to create a base to be extended by local edi rules
for product.

In order to add a new integration, you need to create a listener:

.. code-block:: python

    class MyEventListener1(Component):
        _name = "product.template.event.listener.demo"
        _inherit = "base.event.listener"
        _apply_on = ["product.template"]

        def on_create_product_template(self, products):
            """Add your code here"""

        def on_write_product_template(self, products):
            """Add your code here"""

        def on_unlink_product_template(self, products):
            """Add your code here"""

.. code-block:: python

    class MyEventListener2(Component):
        _name = "product.product.event.listener.demo"
        _inherit = "base.event.listener"
        _apply_on = ["product.product"]

        def on_create_product_product(self, products):
            """Add your code here"""

        def on_write_product_product(self, products):
            """Add your code here"""

        def on_unlink_product_product(self, products):
            """Add your code here"""
