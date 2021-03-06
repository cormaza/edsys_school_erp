# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Edsys Asset',
    'version': '1.0',
    'depends': ['account'],
    'author': 'Redbytes Software',
    'description': """
Financial and accounting asset management.
==========================================

This Module manages the assets owned by a company or an individual. It will keep 
track of depreciation's occurred on those assets. And it allows to create Move's 
of the depreciation lines.

    """,
    'website': 'https://www.redbytes.in/',
    'category': 'Accounting & Finance',
    'depends': ['account_asset'],
    'data': [
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

