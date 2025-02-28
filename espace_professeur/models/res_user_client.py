from odoo import models, fields, api


class SignupPartner(models.Model):
    _inherit = 'res.users'

    school_name = fields.Char(string="Nom de l'école")
    city = fields.Char(string="Ville")

    @api.model
    def _signup_with_values(self, token, values):
        """Ajoute les champs personnalisés lors de l'inscription et assigne le groupe 'Utilisateur Interne'"""

        # Création de l'utilisateur en appelant la méthode parent
        user = super(SignupPartner, self)._signup_with_values(token, values)

        # Ajout des champs personnalisés sur le partenaire lié (res.partner)
        if user.partner_id:
            user.partner_id.write({
                'school_name': values.get('school_name', ''),
                'city': values.get('city', ''),
            })

        # Ajoute l'utilisateur au groupe 'Utilisateur Interne' (base.group_user)
        group_internal = self.env.ref('base.group_user')
        if group_internal:
            user.write({'groups_id': [(4, group_internal.id)]})

        # S'assure que l'utilisateur est actif
        user.write({'active': True})

        return user
