from sys import stdout as terminal
from time import sleep
from itertools import cycle


def animate(event_flag):
    for c in cycle(['|', '/', '-', '\\']):
        if event_flag.is_set():
            break
        terminal.write('\rscraping ' + c)
        terminal.flush()
        sleep(0.1)
    terminal.write('\r')
    terminal.flush()
