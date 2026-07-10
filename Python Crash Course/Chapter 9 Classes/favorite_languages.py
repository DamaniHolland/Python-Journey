###############################################################################
#   Damani Holland
#   7/9/2026
#   CS Python
###############################################################################

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages ['edward'] = 'ruby'
favorite_languages['nexus'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite languages is " +
          language.title() + ".")