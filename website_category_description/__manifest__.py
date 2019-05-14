# Copyright OnurUgur 2019
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': "Website Category Description",
    'summary': "Add Description to product Category",
    'author': "OnurUgur",
    'website': "https://github.com/onurugur/website",
    'category': 'Website',
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'website','website_sale'
    ],
    'data': [
        'views/product_public_category_views.xml',
        'views/template.xml',
    ],
    'demo': [
        'demo/pages.xml',
    ],
}
