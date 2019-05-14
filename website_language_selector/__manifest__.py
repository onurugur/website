# Copyright 2019 OnurUGUR
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Website Language Selector',
    'summary': 'This module shows language selector in header',
    'category': 'Website',
    'version': '11.0.1.0.0',
    'author': 'OnurUGur',
    'license': 'AGPL-3',
    'website': 'https://github.com/onurugur/website',
    'depends': [
        'website'
    ],
    'data': [
        'views/res_lang_views.xml',
        'views/website.xml',
    ],
    'qweb': [
        'static/src/xml/website_media_size.xml'
    ],
}
