# -*- encoding: utf-8 -*-
import os

from wafer.settings import *

try:
    from localsettings import *
except ImportError:
    pass

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

pyconzadir = os.path.dirname(__file__)


STATICFILES_DIRS = (
    os.path.join(pyconzadir, 'static'),
    os.path.join(pyconzadir, 'bower_components'),
)

TEMPLATES[0]['DIRS'] = (
    os.path.join(pyconzadir, 'templates'),
) + TEMPLATES[0]['DIRS']


WAFER_MENUS += (
    {"menu": "about", "label": _("About"),
     "items": []},
    {"name": "venue", "label": _("Venue"),
     "url": reverse_lazy("wafer_page", args=("venue",))},
    {"menu": "sponsors", "label": _("Sponsors"),
     "items": [
         {"name": "Takealot", "label": _(u"» Takealot ★"),
          "url": reverse_lazy("wafer_sponsor", args=(1,))},
         {"name": "Oracle", "label": _(u"» Oracle ★"),
          "url": reverse_lazy("wafer_sponsor", args=(2,))},
         {"name": "Google", "label": _(u"» Google ★"),
          "url": reverse_lazy("wafer_sponsor", args=(5,))},
         {"name": "JUMO", "label": _(u"» JUMO ☆"),
          "url": reverse_lazy("wafer_sponsor", args=(9,))},
         {"name": "Praekelt.org", "label": _(u"» Praekelt.org ☆"),
          "url": reverse_lazy("wafer_sponsor", args=(10,))},
         {"name": "PSF", "label": _(u"» PSF"),
          "url": reverse_lazy("wafer_sponsor", args=(3,))},
         {"name": "OfferZen", "label": _(u"» OfferZen"),
          "url": reverse_lazy("wafer_sponsor", args=(6,))},
         {"name": "Amazon", "label": _(u"» Amazon"),
          "url": reverse_lazy("wafer_sponsor", args=(7,))},
         {"name": "VOSS", "label": _(u"» VOSS"),
          "url": reverse_lazy("wafer_sponsor", args=(8,))},
         {"name": "CHPC", "label": _(u"» CHPC"),
          "url": reverse_lazy("wafer_sponsor", args=(11,))},
         {"name": "sponsors", "label": _("Our sponsors"),
          "url": reverse_lazy("wafer_sponsors")},
         {"name": "packages", "label": _("Sponsorship packages"),
          "url": reverse_lazy("wafer_sponsorship_packages")},
         ]},
    {"menu": "talks", "label": _("Talks"),
     "items": [
         {"name": "schedule", "label": _("Schedule"),
          "url": reverse_lazy("wafer_full_schedule")},
         {"name": "accepted-talks", "label": _("Accepted Talks"),
          "url": reverse_lazy("wafer_users_talks")},
         {"name": "speakers", "label": _("Speakers"),
          "url": reverse_lazy("wafer_talks_speakers")},
        ]},
    {"menu": "news", "label": _("News"),
     "items": []},
    {"menu": "previous-pycons", "label": _("Past PyConZAs"),
     "items": [
         {"name": "pyconza2012", "label": _("PyConZA 2012"),
          "url": "http://2012.za.pycon.org/"},
         {"name": "pyconza2013", "label": _("PyConZA 2013"),
          "url": "http://2013.za.pycon.org/"},
         {"name": "pyconza2014", "label": _("PyConZA 2014"),
          "url": "http://2014.za.pycon.org/"},
         {"name": "pyconza2015", "label": _("PyConZA 2015"),
          "url": "http://2015.za.pycon.org/"},
         ]},
    {"name": "twitter", "label": "Twitter",
     "image": "/static/img/twitter.png",
     "url": "https://twitter.com/pyconza"},
    {"name": "googleplus", "label": "Google+",
     "image": "/static/img/googleplus.png",
     "url": "https://plus.google.com/events/ccqgtdbrk712n64ruc66s4tpsms"},
    {"name": "facebook", "label": "Facebook",
     "image": "/static/img/facebook.png",
     "url": "https://www.facebook.com/pyconza"},
)


CRISPY_TEMPLATE_PACK = 'bootstrap3'
MARKITUP_FILTER = ('markdown.markdown', {
    'safe_mode': False,
    'extensions': [
        'outline',
        'attr_list',
        'attr_cols',
        'markdown.extensions.tables',
    ],
})
# Use HTTPS jquery URL so it's accessible on HTTPS pages (e.g. editing a talk)
JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.0.3/jquery.min.js'

WAFER_TALKS_OPEN = False
