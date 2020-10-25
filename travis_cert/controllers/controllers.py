# -*- coding: utf-8 -*-
# from odoo import http


# class TravisCert(http.Controller):
#     @http.route('/travis_cert/travis_cert/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/travis_cert/travis_cert/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('travis_cert.listing', {
#             'root': '/travis_cert/travis_cert',
#             'objects': http.request.env['travis_cert.travis_cert'].search([]),
#         })

#     @http.route('/travis_cert/travis_cert/objects/<model("travis_cert.travis_cert"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('travis_cert.object', {
#             'object': obj
#         })
