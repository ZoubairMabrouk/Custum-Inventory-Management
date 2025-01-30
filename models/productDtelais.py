from odoo import models, fields,api

class ProductDetails(models.Model):
    _name = 'product.details'
    _description = 'Product Details'
    
    name = fields.Char(string="Product Name", required=True)
    description = fields.Text(string="Product Description")
    product_id = fields.Many2one('product.product', string="Related Product", required=True)
    stock_quantity = fields.Float(string="Stock Quantity", default=0.0)
    warehouse_location = fields.Char(string="Warehouse Location")
    price = fields.Float(string="Price")
     # Use @api.multi to handle multiple records if needed
    def button_product_details_save(self):
        for record in self:
            if record.price <= 0:
                raise ValueError("Le prix doit être supérieur à zéro.")
            if record.stock_quantity < 0:
                raise ValueError("La quantité en stock ne peut pas être négative.")

            product = record.product_id
            product.write({
                'qty_available': record.stock_quantity, 
                'standard_price': record.price
            })
        
        return True
