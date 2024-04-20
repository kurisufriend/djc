import time, subprocess, dbus
from core import *

s = setup("/dev/ttyACM0")
state = {}
lastvol = update(s, state)["vol"]

interface = dbus.Interface(dbus.SessionBus().get_object('org.Cinnamon', '/org/Cinnamon'), 'org.Cinnamon')

while True:
    state = update(s, state)
    if abs(state["vol"] - lastvol) >= 10:
        lastvol = state["vol"]
        adjusted = int(state["vol"]/1024*100)
        subprocess.call(f"pactl set-sink-volume @DEFAULT_SINK@ {adjusted}%", shell=True)

        level = ["muted", "low", "medium", "high"][int(state["vol"]/1024*3 + .5)]
        logo = f"audio-volume-{level}-symbolic"
        interface.ShowOSD({"icon": logo, "level": adjusted})

unsetdown(s)