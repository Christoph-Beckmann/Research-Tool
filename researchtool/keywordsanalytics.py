# https://towardsdatascience.com/keyword-extraction-process-in-python-with-natural-language-processing-nlp-d769a9069d5c
import logging
import yake
from pytrends.request import TrendReq
from researchtool import helpers
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)


def extract_keywords(text, wordcount, duplication, max_keywords):
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
    trend = TrendReq()
    keyword = [f"{keyword}"]                # Necessary API String Format
    trend.build_payload(kw_list=keyword)
    related_kw = trend.related_topics()
    related_kw.values()
    data_top_kw = list(related_kw.values())[0]["top"]
    list_top_kw = []
    for i in range(len(data_top_kw.values)):
        list_top_kw.append(data_top_kw.values[i][5])

    return list_top_kw


def interest_of_time(keyword_list, timeframe):
    trend = TrendReq()
    keywords = keyword_list
    trend.build_payload(kw_list=keywords, cat=None, timeframe=timeframe, geo="")
    data = trend.interest_over_time()

    return data
