from odoo import models, fields, api
import requests

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    custom_field = fields.Char(string='Custom Field')

    @api.onchange('custom_field')
    def _onchange_custom_field(self):
        if self.custom_field:
            self.call_external_api()

    def call_external_api(self):
        endpoint_url = 'https://api.example.com'
        data = {
            'product_id': self.id,
            'custom_field_value': self.custom_field,
            # Otros datos que quieras enviar
        }

        response = requests.post(endpoint_url, json=data)

        if response.status_code == 200:
            self.env.user.message_post(body="Llamada a la API externa exitosa.")
        else:
            self.env.user.message_post(body="Error al llamar a la API externa.")