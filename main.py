from leaders_scraper import get_leaders, save
from loading_animation import animate
from threading import Thread, Event


def main():
    """
    The main function controlling the animation, the scraping and saving processes.
    The animation is running on a separate thread and is controlled by an Event flag
    which stops the thread when set to True.
    """
    event_flag = Event()
    t = Thread(target=animate, args=(event_flag,))
    t.start()
    data = get_leaders()
    event_flag.set()
    save(data)


if __name__ == "__main__":
    main()
