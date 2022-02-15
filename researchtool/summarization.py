import nltk                                         # Natural Language Toolkit: https://www.nltk.org/
import ssl                                          # Secure Sockets Layer - Internet Protocol
from nltk.cluster.util import cosine_distance       # Necessary for calculate Cosine similarity
from nltk.corpus import stopwords                   # nltk stopwords files
import numpy as np
import networkx as nx                               # Network analysis
from langdetect import detect                       # Language Detection in ISO639-1
import iso639                                       # Transform ISO639-1 to ISO language name for stopwords file


# Nltk Downloader is broken. There is a workaround to download the required "stopwords" package.
# This code disable the SSL Certificate Verification.
# Found solution on: https://github.com/gunthercox/ChatterBot/issues/930#issuecomment-322111087
def install_stopwords():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context

    nltk.download('stopwords')     # Adapted to download only the required package.


# Automatic detection of the language and conversion from "de" to "Deutsch" using the packages Langdetect and ISO639.
def detectlanguage(text):
    language = iso639.to_name(detect(text))
    return language


# Read Textfile and create sentences
def read(text):
    language = detectlanguage(text)                  # Function detectlanguage get the parameter text
    sentences_split = text.split(". ")               # Sentences are stored as a list with Dot as a Delimiter
    sentences = []
    for sentence in sentences_split:
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop()

    return sentences, language


def sentence_similarity(sentence1, sentence2,  stop_words=None):
    if stop_words is None:
        stop_words = []
    sentence1 = [w.lower() for w in sentence1]
    sentence2 = [w.lower() for w in sentence2]
    all_words = list(set(sentence1+sentence2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
    for w in sentence1:
        if w in stop_words:
            continue
        vector1[all_words.index(w)] += 1
    for w in sentence2:
        if w in stop_words:
            continue
        vector2[all_words.index(w)] += 1
    return 1-cosine_distance(vector1, vector2)


def gen_sim_matrix(sentences, stop_words=None):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2:
                continue
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

        return similarity_matrix


def build_summary(text, top_n=5):
    install_stopwords()
    summarized_text = []
    sentences, language = read(text)
    stop_words = stopwords.words(language)
    sentence_similarity_matrix = gen_sim_matrix(sentences, stop_words)
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)
    ranked_sentence = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    for i in range(top_n):
        summarized_text.append(" ".join(ranked_sentence[i][1]))
    return summarized_text


