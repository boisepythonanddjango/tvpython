from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu

class TestMenu(Menu):

    def get_nodes(self, request):
        nodes = []
        n = NavigationNode(_('sample root page'), "/", 1)
        n2 = NavigationNode(_('sample settings page'), "/bye/", 2)
        n3 = NavigationNode(_('sample account page'), "/hello/", 3)
        n4 = NavigationNode(_('sample my profile page'), "/hello/world/", 4, 3)
        nodes.append(n)
        nodes.append(n2)
        nodes.append(n3)
        nodes.append(n4)
        return nodes

class TestMenuAttach(CMSAttachMenu):

    name = _("test menu attach")

    def get_nodes(self, request):
        nodes = []
        n = NavigationNode(_('new root page'), "/", 1)
        n2 = NavigationNode(_('attache page bye'), "/bye/", 2)
        n3 = NavigationNode(_('attache page hello'), "/hello/", 3)
        n4 = NavigationNode(_('hello world.'), "/hello/world/", 4, 3)
        nodes.append(n)
        nodes.append(n2)
        nodes.append(n3)
        nodes.append(n4)
        return nodes

menu_pool.register_menu(TestMenuAttach)

menu_pool.register_menu(TestMenu)