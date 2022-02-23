import logging
import yake
from pytrends.request import TrendReq
from researchtool import helpers

logger = logging.getLogger(__name__)


def extract_keywords(text, wordcount, duplication, max_keywords):
    """
    Extract keywords from a given text and given parameter with

    :param text: inserted text from textbox
    :param wordcount: limit the word count of the extracted keyword, i.e. <= 3
    :param duplication: limit the duplication of words in different keywords. 0.9 allows repetition of words in keywords
    :param max_keywords: determine the count of keywords which are extracted, i.e. <= 20
    :return: list of tuples keywords with scores
    """
    language = helpers.detectlanguage(text, False)
    extractor = yake.KeywordExtractor(
        lan=language,
        n=wordcount,
        dedupLim=duplication,
        top=max_keywords,
        features=None
    )
    keywords = extractor.extract_keywords(text)
    keywords.sort(key=lambda a: a[1])      # Lower Score = the more relevant. For this: Sorting list of tuples of Item 1

    return keywords


def related_keywords(keyword):
    """
    Find related keywords with given keyword via Google Trend API

    :param keyword: Selected Keyword from listbox
    :return list_top_kw: List of top keywords from Google API Call
    """
    trend = TrendReq()
    keyword = [f"{keyword}"]                # Necessary API String Format
    trend.build_payload(kw_list=keyword)    # Google Trend API Call with given parameter
    related_kw = trend.related_topics()
    related_kw.values()
    data_top_kw = list(related_kw.values())[0]["top"]
    list_top_kw = []
    for i in range(len(data_top_kw.values)):
        list_top_kw.append(data_top_kw.values[i][5])

    return list_top_kw


def interest_of_time(keyword_list, timeframe):
    """
    Get dataset of relative interest of selected keywords

    :param keyword_list: Selected keywords (up to 5) from second listbox
    :param timeframe: dropdown menu Item with given timeframe for get time specific data
    :return data: Dataframe with y = Date; x = Keyword relative interest to top keyword
    """
    trend = TrendReq()
    keywords = keyword_list
    trend.build_payload(kw_list=keywords, cat=None, timeframe=timeframe, geo="")
    data = trend.interest_over_time()

    return data
