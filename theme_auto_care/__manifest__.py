
{
    'name': 'Theme AutoCare Pro',
    'category': 'Theme/Corporate',
    'version': '18.0.0.0',
    'sequence': 1,
    'author': 'ZAPP',
    'summary': '''Theme AutoCare is featured with Service functionalities and is fully responsive to all devices.''',

    'depends': [
        'website',
        'web_editor',
        'website_sale',
    ],

    'data': [

        "views/header.xml",
        "views/footer.xml",
        "views/theme_auto_care_inherited.xml",
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
        'web._assets_primary_variables': [
            ('before', 'website/static/src/scss/options/colors/user_color_palette.scss',
             '/theme_auto_care/static/src/scss/user_color_palette.scss'),
            ('before', 'website/static/src/scss/options/user_values.scss',
             '/theme_auto_care/static/src/scss/user_values.scss'),
        ],
    },

    'assets': {
        'web.assets_frontend': [
            'theme_auto_care/static/src/css/banner.css',
            'theme_auto_care/static/src/css/normalise.css',
            'theme_auto_care/static/src/css/vendor.css',
            
        ],
    },

    'images': [
        'static/description/autocare_cover.jpg',
        'static/description/autocare_screenshot.gif',

    ],

    'installable': True,
    'auto_install': False,
    'application': False,
    'license': 'OPL-1',
}
