import wx
import wx.adv
from wallchanger import setup_manager
from log import setup_global_logger

TRAY_TOOLTIP = 'Wallchanger 0.2a'
TRAY_ICON = 'icon.png'


def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item


class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self, manager):
        wx.adv.TaskBarIcon.__init__(self)
        self.set_icon(TRAY_ICON)
        self.Bind(wx.EVT_RIGHT_DOWN, self.on_right_down)
        self.manager = manager
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        minTime = min(self.manager.settings['changeInterval'], self.manager.settings['downloadInterval'])
        self.timer.Start(milliseconds=minTime * 333)

    def on_timer(self, event):
        self.manager.run_pending()

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'Next', self.on_next)
        menu.AppendSeparator()
        create_menu_item(menu, 'Delete', self.on_delete)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def set_icon(self, path):
        icon = wx.Icon(path, type=wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon, TRAY_TOOLTIP)

    def on_next(self, event):
        self.manager.next()

    def on_right_down(self, event):
        event.Skip()

    def on_delete(self, event):
        self.manager.delete()

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)


def main():
    app = wx.App()
    setup_global_logger()
    manager = setup_manager()
    TaskBarIcon(manager)
    manager.run_all()
    app.MainLoop()


if __name__ == '__main__':
    main()
