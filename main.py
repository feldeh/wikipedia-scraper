from leaders_scraper import get_leaders, save


def main():
    data = get_leaders()
    save(data)


if __name__ == "__main__":
    main()
