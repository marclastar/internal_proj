# -*- encoding: utf-8 -*-

{
    'name': 'CZ Management for AGRITEC',
    'version': '1.0',
    'author': 'Africa Performances',
    'category': 'Others',
    'website': 'http://www.africaperformances-ci.com/',
    'description': """
* CZ Management for AGRITEC
Users Access
Payement customers and suppliers
Warehouse management for CZ
""",
    'depends': ['base','account','sale_stock','stock_picking_wave','stock'],
    'data': ['cz_management.xml','cz_management_view.xml','security/user_group.xml','security/read_only_user_group.xml',],
	'auto_install': False,
    'installable': True,
    'active': False,
    'application': False,	
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: