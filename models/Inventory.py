from odoo import models, fields, api, _
from odoo.exceptions import UserError

class InventoryAdjustment(models.Model):
    _name = 'inventory.adjustment'
    _description = 'Ajustement d\'inventaire'

    name = fields.Char('Référence de l\'ajustement', required=True, copy=False, default=lambda self: _('New'))
    product_id = fields.Many2one('product.details', 'Produit', required=True)
    quantity = fields.Float('Quantité', required=True)
    transaction_price = fields.Float('Prix total', required=True)
    date = fields.Datetime('Date', default=fields.Datetime.now)
    adjustment_type = fields.Selection([('in', 'Entrée'), ('out', 'Sortie')], string='Type d\'ajustement', required=True)
    customer_id = fields.Many2one('res.partner', 'Client',  help="Sélectionnez le client pour les sorties")
    reason = fields.Text('Raison', help="Ajouter une description ou une raison pour l\'ajustement")
    
    state = fields.Selection([('draft', 'Brouillon'), ('done', 'Validé')], default='draft')
    invoice_id = fields.Many2one('account.move', 'Facture', readonly=True, help="Facture générée pour cet ajustement")

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('inventory.adjustment') or _('New')
        return super(InventoryAdjustment, self).create(vals)

    def action_validate(self):
        self.state = 'done'
        if self.adjustment_type == 'in':
            self.product_id.stock_quantity += self.quantity
        elif self.adjustment_type == 'out':
            if self.product_id.stock_quantity < self.quantity:
                raise UserError("Stock insuffisant pour cette sortie.")
            self.product_id.stock_quantity -= self.quantity
        self.generate_invoice()
    def generate_invoice(self):
        if not self.customer_id :
            raise UserError("Veuillez sélectionner un client pour la facture.")
        invoice_vals = {
            'move_type':'out_invoice' if self.adjustment_type == 'out' else 'in_invoice',
            'partner_id': self.customer_id.id,
            'invoice_date': fields.Date.today(),
            'invoice_line_ids': [(0, 0, {
                'product_id': self.product_id.id,
                'name': self.product_id.name,
                'quantity': self.quantity,
                'price_unit': self.transaction_price / self.quantity if self.quantity else 0.0,
            })],
        }
        invoice = self.env['account.move'].create(invoice_vals)
        self.invoice_id = invoice.id
