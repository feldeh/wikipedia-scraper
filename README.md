# Wikipedia Scraper

## Introduction

Wikipedia Scraper is a Python program that fetches, scrapes and saves information about the leaders of different countries.

## Features

- Fetches leaders information, including their Wikipedia page url, from an API.
- Scrapes the first paragraph from each leader's Wikipedia page.
- Sanitizes the text by removing unnecessary characters and formatting.
- Displays a loading animation in the terminal while scraping is in progress.
- Saves the data in a JSON file.

## Requirements

- Python 3

## Installation

1. Clone this repository to your local machine.

```sh
git clone https://github.com/feldeh/wikipedia-scraper
```

2. Navigate to the project directory.

```sh
cd <path-to-directory>
```

3. Install the required Python libraries by running the following command:

```sh
pip install -r requirements.txt
```

## Usage

1. Run the script from the command line using Python.

```sh
python main.py
```

2. The script will scrape data for leaders of different countries and save the data in a JSON file named `leaders.json` in the current directory.

## Timeline

This project took me 2 days to complete and was part of the AI & Data science training at [BeCode.org](https://becode.org/)
