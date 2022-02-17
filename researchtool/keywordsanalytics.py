# https://towardsdatascience.com/keyword-extraction-process-in-python-with-natural-language-processing-nlp-d769a9069d5c
import tkinter as tk
import yake
import helpers


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
