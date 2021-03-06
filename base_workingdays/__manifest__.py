# -*- coding: utf-8 -*-
##############################################################################
#
#    base_workingdays module for OpenERP, Manage working days
#    Copyright (C) 2012 SYLEAM Info Services (<http://www.syleam.fr/>)
#              Sebastien LANGE <sebastien.lange@syleam.fr>
#
#    This file is a part of base_workingdays
#
#    base_workingdays is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    base_workingdays is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Working Days',
    'version': '1.0',
    'category': 'Hidden/Dependency',
    'complexity': "easy",
    'description': """
It let you to configure the working days in your company.
After set, OpenERP compute the good date depending working days and days not worked (depending country)
Just France is set for the days not worked.
    """,
    'author': 'Edsys',
    'website': 'http://www.redbytes.in/',
    'depends': [
        'base', 'hr_public_holidays',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/res_company.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'active': False,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
