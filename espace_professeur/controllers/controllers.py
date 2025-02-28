# -*- coding: utf-8 -*-
# from odoo import http


# class EspaceProfesseur(http.Controller):
#     @http.route('/espace_professeur/espace_professeur', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/espace_professeur/espace_professeur/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('espace_professeur.listing', {
#             'root': '/espace_professeur/espace_professeur',
#             'objects': http.request.env['espace_professeur.espace_professeur'].search([]),
#         })

#     @http.route('/espace_professeur/espace_professeur/objects/<model("espace_professeur.espace_professeur"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('espace_professeur.object', {
#             'object': obj
#         })

