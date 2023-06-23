from leaders_scraper import get_leaders, save
from loading_animation import animate
from threading import Thread, Event


def main():
    event_flag = Event()
    t = Thread(target=animate, args=(event_flag,))
    t.start()

    data = get_leaders()

    event_flag.set()
    save(data)


if __name__ == "__main__":
    main()
