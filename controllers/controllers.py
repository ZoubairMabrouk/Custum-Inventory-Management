# -*- coding: utf-8 -*-
# from odoo import http


# class Ex-module(http.Controller):
#     @http.route('/ex-module/ex-module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ex-module/ex-module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ex-module.listing', {
#             'root': '/ex-module/ex-module',
#             'objects': http.request.env['ex-module.ex-module'].search([]),
#         })

#     @http.route('/ex-module/ex-module/objects/<model("ex-module.ex-module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ex-module.object', {
#             'object': obj
#         })
