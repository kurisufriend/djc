import time, os
from core import *

s = setup("/dev/ttyACM0")
state = {}
lastvol = update(s, state)["vol"]

while True:
    state = update(s, state)
    if abs(state["vol"] - lastvol) >= 10:
        os.system("amixer -D pulse sset Master "+str(state["vol"]/1024*100)+"%")
        print("changed", str(state["vol"]/1024*100))
        print("changed", str(state["vol"]))
        lastvol = state["vol"]

unsetdown(s)