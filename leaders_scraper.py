import requests
from bs4 import BeautifulSoup
import re
import json


def sanitize(str):
    """
    Cleans and returns the input string after removing unnecessary characters
    and formatting from Wikipedia such as phonetic alphabet and reference notations.

    @param str: the input string to be cleaned
    @return: the cleaned string
    """
    semicolon_cleanup = re.compile(r"\/(.*);")
    second_cleanup = re.compile(r"(\/(.*?)\/)|(\[(.*?)\])|(Écouter)|(\(listen\))|(uitspraak)|(\(info / uitleg\))")
    parentheses_cleanup = re.compile(r"\(\s*\)")
    last_cleanup = re.compile(r"\s{2,}")

    removed_semi = re.sub(semicolon_cleanup, "", str)
    removed_second = re.sub(second_cleanup, "", removed_semi)
    removed_empty_parentheses = re.sub(parentheses_cleanup, "", removed_second)
    cleaned_string = re.sub(last_cleanup, " ", removed_empty_parentheses)
    return cleaned_string


def get_first_paragraph(wikipedia_url, session):
    """
    Scrapes and returns the first paragraph of the Wikipedia page from the input url.

    @param wikipedia_url: the url of the Wikipedia page.
    @param session: the requests session object for making HTTP requests.
    @return: the first paragraph of the Wikipedia page.
    """
    res = session.get(wikipedia_url)
    content = res.content
    soup = BeautifulSoup(content, 'html.parser')
    paragraphs = []
    for p in soup.find_all("p"):
        if p.find_parent(class_="bandeau-cell") or p.find_parent(class_="plainlist"):
            continue
        p = p.text.strip()
        if p != "":
            paragraphs.append(p)
    return sanitize(paragraphs[0])


def get_leaders():
    """
    Fetches information about world leaders from an API and scrapes the first paragraph
    of each leaders from Wikipedia. Will also set a new cookie from the API if the cookie expires.

    @return: a dictionary with countries as keys and a list of leaders with additional information as values.
    """
    base_url = "https://country-leaders.onrender.com"
    leaders_url = base_url + "/leaders"
    cookie_url = base_url + "/cookie"
    countries_url = base_url + "/countries"
    cookie_res = requests.get(cookie_url)
    cookies = cookie_res.cookies.get_dict()

    countries_list = requests.get(countries_url, cookies=cookies).json()

    leaders_per_country = {}

    for country in countries_list:
        params = "country=" + country
        leaders_res = requests.get(leaders_url, params=params, cookies=cookies)

        if leaders_res.status_code == 403:
            cookie_res = requests.get(cookie_url)
            cookies = cookie_res.cookies.get_dict()
            leaders_res = requests.get(leaders_url, params=params, cookies=cookies)

        leaders = leaders_res.json()
        leaders_per_country[country] = leaders

        with requests.Session() as wiki_session:
            for i in range(len(leaders)):
                leader_url = leaders[i]["wikipedia_url"]
                first_paragraph = get_first_paragraph(leader_url, wiki_session)
                leaders_per_country[country][i]["wikipedia_first_paragraph"] = first_paragraph

    return leaders_per_country


def save(leaders_per_country):
    """
    Saves the data into a JSON file in a readable format.

    @param leaders_per_country: the data to be saved.
    """
    with open("leaders.json", "w", encoding="utf-8") as f:
        json.dump(leaders_per_country, f, ensure_ascii=False, indent=4)

        print('\rLeaders data saved in ' + '\033[32m' + 'leaders.json')
