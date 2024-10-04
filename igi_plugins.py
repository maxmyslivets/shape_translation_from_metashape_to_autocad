import webbrowser

from src.common.startup.initialization import ms
from src.installed_plugins import *


TOP_MENU = 'ИГИ'


def about():
    webbrowser.open(
        url='https://github.com/maxmyslivets/shape-translation-from-metashape-to-autocad/blob/main/README.md',
        new=2)


ms.app.addMenuItem(TOP_MENU+'/Помощь', about)