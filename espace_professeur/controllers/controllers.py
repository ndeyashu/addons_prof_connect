import logging
from odoo import http, _
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.exceptions import UserError  # Correction de l'import

_logger = logging.getLogger(__name__)

class AuthSignupCustom(AuthSignupHome):

    def do_signup(self, qcontext):
        """Ajoute les champs 'city' et 'school_name' à la création d'un utilisateur."""
        values = {key: (qcontext.get(key, '').strip() or '') for key in ('login', 'name', 'password', 'city', 'school_name')}

        if not values.get('login'):
            raise UserError(_("Un email est requis pour s'inscrire."))

        _logger.info(f"Création d'un nouvel utilisateur : {values['login']}")

        # Création du partenaire associé
        partner = request.env['res.partner'].sudo().create({
            'name': values['name'],
            'email': values['login'],
            'city': values['city'],
            'school_name': values['school_name'],
        })

        # Création de l'utilisateur
        user = request.env['res.users'].sudo().create({
            'name': values['name'],
            'login': values['login'],
            'password': values['password'],
            'partner_id': partner.id,
        })

        _logger.info(f"Utilisateur {values['login']} créé avec succès (ID: {user.id})")

        return user
