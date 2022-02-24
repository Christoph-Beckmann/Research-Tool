import logging
from bs4 import BeautifulSoup
import requests

logger = logging.getLogger(__name__)


def scrape(query, language):
    """
    Web Scraping Function with BeautifulSoup as a Package

    :param query: Search Query -> Keyword which is searched on Google Scholar
    :param language: in which language?
    :return data: List of Dictionaries with search results
    """
    # Header for POST-Call
    header = {
        "User-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " +
            "Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }
    # Search parameter for POST-Call
    params = {
        "q": query,
        "hl": language,
    }

    html = requests.get("https://scholar.google.com/scholar", headers=header, params=params).text   # HTML Post Query

    soup = BeautifulSoup(html, "lxml")     # BeautifulSoup for web scraping

    # empty list
    data = []

    # Container in which all the important information 
    for result in soup.select('.gs_ri'):
        title = result.select_one('.gs_rt').text
        title_link = result.select_one('.gs_rt a')['href']
        publication_info = result.select_one('.gs_a').text
        snippet = result.select_one('.gs_rs').text

        data.append({
            'title': title,
            'publication_info': publication_info,
            'snippet': snippet,
            'title_link': title_link,
        })

    return data
