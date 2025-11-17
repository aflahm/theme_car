
{
    'name': 'AutoCare Pro',
    'category': 'Theme/Corporate',
    'version': '18.0.0.0',
    'sequence': 1,
    'author': 'TECHVEX',
    'summary': '''Theme AutoCare is featured with AutoCare Service and is fully responsive to all devices.''',

    'depends': [
        'website',
        'web_editor',
    ],

    'data': [

        "views/header.xml",
        "views/footer.xml",
        "views/theme_autocare_pro_inherited.xml",
        # homepage
        "views/homepage/ac_home.xml",
        "views/homepage/ac_offer.xml",
        "views/homepage/ac_help.xml",
        "views/homepage/ac_service_detailed.xml",
        "views/homepage/ac_our_service.xml",
        "views/homepage/ac_service_title.xml",
        "views/homepage/ac_y_choose_us.xml",
        "views/homepage/ac_packages.xml",
        "views/homepage/ac_review.xml",
        "views/homepage/about_us.xml",
        "views/homepage/comp_story.xml",
        "views/homepage/team.xml",
        "views/homepage/about_us_state.xml",
        "views/homepage/about_us_contact.xml",
        "views/homepage/contact_header.xml",
        "views/homepage/conatct_info.xml",
        "views/homepage/contact_map_form.xml",
        "views/homepage/contact_emergency.xml",


    ],

    'assets': {
        'web.assets_frontend': [
            'theme_autocare_pro/static/src/css/banner.css',
            
        ],
    },

    'images': [
        'static/description/autocare_cover.jpg',
        'static/description/autocare_screenshot.gif',

    ],

    'support': 'techvex.dev@gmail.com',
    'price': 17.00,
    'currency': 'USD',
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'OPL-1',
}
