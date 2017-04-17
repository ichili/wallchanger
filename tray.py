import wx
import wx.adv

TRAY_TOOLTIP = 'Wallchanger 0.1a'
TRAY_ICON = 'icon.png'


def create_menu_item(menu, label, func):
    item = wx.MenuItem(menu, -1, label)
    menu.Bind(wx.EVT_MENU, func, id=item.GetId())
    menu.Append(item)
    return item


class TaskBarIcon(wx.adv.TaskBarIcon):
    def __init__(self):
        wx.adv.TaskBarIcon.__init__(self)
        self.set_icon(TRAY_ICON)
        self.Bind(wx.EVT_RIGHT_DOWN, self.on_right_down)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        create_menu_item(menu, 'Next', self.on_next)
        menu.AppendSeparator()
        create_menu_item(menu, 'Delete', self.on_delete)
        menu.AppendSeparator()
        create_menu_item(menu, 'Exit', self.on_exit)
        return menu

    def set_icon(self, path):
        icon = wx.Icon(TRAY_ICON, type=wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon, TRAY_TOOLTIP)

    def on_next(self, event):
        pass

    def on_right_down(self, event):
        event.Skip()

    def on_next(self, event):
        pass

    def on_delete(self, event):
        pass

    def on_exit(self, event):
        wx.CallAfter(self.Destroy)


def main():
    app = wx.App()
    TaskBarIcon()
    app.MainLoop()


if __name__ == '__main__':
    main()
