# https://towardsdatascience.com/keyword-extraction-process-in-python-with-natural-language-processing-nlp-d769a9069d5c
import tkinter as tk
import yake
from pytrends.request import TrendReq
from researchtool import helpers


def extract_keywords(text, wordcount, duplication, max_keywords, listbox: tk.Listbox):
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

    s = 0
    for i in keywords:
        listbox.insert(s, i[0])
        s += 1


def related_keywords(keyword):
    trend = TrendReq()
    keyword = [f'{keyword}']                # Necessary API String Format
    trend.build_payload(kw_list=keyword)

    related_kw = trend.related_topics()
    related_kw.values()

    data_top_kw = list(related_kw.values())[0]['top']

    list_top_kw = []
    for i in range(len(data_top_kw.values)):
        list_top_kw.append(data_top_kw.values[i][5])

    return list_top_kw


