#!/usr/bin/env python3
import dbus
import dbus.mainloop.glib
from gi.repository import GLib
import subprocess


def on_notify(namespace, keys, tag):
    # namespace is the first argument of the signal, i.e., the dconf path
    if "engines-order" in str(namespace):
        print("Layout changed, running command...")
        subprocess.Popen(
            ["/bin/zsh", "-c", "(source /home/tilc/.config/.zshrc) >/dev/null 2>&1"],
            stdout=None,
        )


dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SessionBus()

bus.add_signal_receiver(
    on_notify,
    signal_name="Notify",
    dbus_interface="ca.desrt.dconf.Writer",
    bus_name="ca.desrt.dconf",
    path="/ca/desrt/dconf/Writer/user",  # Key point: the object path of the dconf Writer
    path_keyword=None,
)

GLib.MainLoop().run()
