from sys import stdout as terminal
from time import sleep
from itertools import cycle


def animate(event_flag):
    """
    Adds an animation in the terminal.

    @param event_flag: the threading event flag to control the animation.
    """
    for c in cycle(['|', '/', '-', '\\']):
        if event_flag.is_set():
            break
        terminal.write('\rscraping ' + c)
        terminal.flush()
        sleep(0.1)
    terminal.write('\r')
    terminal.flush()
