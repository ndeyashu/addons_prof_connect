# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
import logging

_logger = logging.getLogger(__name__)

TYPE_PROFIL=[
    ('professeur', 'Professeur'),
    ('particulier', 'Particulier'),
]
STATES_PROFESSEUR = [
    ('brouillon', 'Brouillon'),
    ('valider','Valider'),
    ('annuler','Annuler'),
]

class Partner(models.Model):
    _inherit = 'res.partner'
    _description = 'espace_professeur.espace_professeur'

    type_profil = fields.Selection(TYPE_PROFIL, string="Profil", store=True)
    specialite = fields.Char(string='Spécialité')
    cv = fields.Binary(string='CV')
    cv_filename = fields.Char(string='CV Filename', compute='_compute_cv_filename', store=True)
    state = fields.Selection(STATES_PROFESSEUR, index=True, string='State', default='brouillon')
    experience = fields.Integer(string="Nombre d'années d'expérience")
    school_name = fields.Char(string="Nom de l'école")
    city = fields.Char(string="Ville")

    @api.depends('cv')
    def _compute_cv_filename(self):
        for record in self:
            record.cv_filename = 'CV' if record.cv else False

    def action_brouillon(self):
        self.state = 'brouillon'

    def action_annuler(self):
        self.state = 'annuler'

    def action_confirm(self):
        self.state = 'valider'
        template = self.env.ref('espace_professeur.email_alerte_professeur_confirm')
        if self.ids:
            self.env['mail.template'].browse(template.id).sudo().send_mail(self.ids[0], force_send=True)
            _logger.warning(f"Pas d'email défini pour {self.email}")

