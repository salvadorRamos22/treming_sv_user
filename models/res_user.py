from odoo import fields, models

class CvResUser(models.Model):
    _inherit = "res.users"

    stock_warehouse_id = fields.Many2one(comodel_name="stock.warehouse", string="Sucursal", required=False)
