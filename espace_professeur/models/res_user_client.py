from odoo import models, fields, api


class SignupPartner(models.Model):
    _inherit = 'res.users'

    school_name = fields.Char(string="Nom de l'école", store=True)
    city = fields.Char(string="Ville", store=True)

    @api.model
    def create(self, vals):
        """Ajoute automatiquement le groupe 'group_entreprise_connectes' aux nouveaux utilisateurs."""
        user = super(SignupPartner, self).create(vals)
        group = self.env.ref('espace_professeur.group_entreprise_connectes')
        if group:
            user.groups_id = [(4, group.id)]
        return user

