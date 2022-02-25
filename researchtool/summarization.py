import logging
from nltk.cluster.util import cosine_distance       # For calculate Cosine similarity (Similarity of two sentences)
from nltk.corpus import stopwords                   # nltk stopwords files
import numpy as np
import networkx as nx                               # Network analysis: Need for similarity graph
from helpers import detectlanguage                  # helpers: here detectlanguage
from helpers import install_stopwords               # helpers: install stopwords manually

logger = logging.getLogger(__name__)


def read(text):
    """
    Processes the text and separates the sentences from each other. Also detect language of the text.

    :param text: Inserted Text from Textbox
    :return sentences: List of separated sentences
    :return language: Return language in ISO 639 short format for usage of stopwords
    """
    language = detectlanguage(text, True)
    sentences_split = text.split(". ")
    sentences = []
    for sentence in sentences_split:
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop()

    return sentences, language


def sentence_similarity(sentence1, sentence2,  stop_words=None):
    """
    Calculate the similarity of two sentences

    :param sentence1: Sentence 1 which is compared with sentence 2
    :param sentence2: Sentence 2 which is compared with sentence 1
    :param stop_words: List of words which are very common but don't provide useful information for text analysis

    :return cosine_distance: Return calculated cosine similarity of two vectors (sentences)
    """
    if stop_words is None:
        stop_words = []
    sentence1 = [w.lower() for w in sentence1]        # Each word of sentence is parsed. To generalized use lower cases
    sentence2 = [w.lower() for w in sentence2]
    all_words = list(set(sentence1+sentence2))

    vector1 = [0] * len(all_words)                    # Create vectors for sentence 1 and 2
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


def generate_sim_matrix(sentences, stop_words=None):
    """
    Generate the similarity matrix of a text

    :param sentences: Get list of sentences of read-function
    :param stop_words: List of words which are very common but don't provide useful information for text analysis

    :return similarity_matrix: Return
    """
    similarity_matrix = np.zeros((len(sentences), len(sentences)))    # Create two-dimensional empty matrix
    for vector1 in range(len(sentences)):
        for vector2 in range(len(sentences)):
            if vector1 == vector2:
                continue
            similarity_matrix[vector1][vector2] = sentence_similarity(
                sentences[vector1],
                sentences[vector2],
                stop_words
            )

        return similarity_matrix


def build_summary(text, top_n=5):
    """
    Build summary with built functions to generate a similarity matrix and with networkx sentences are ranked.
    With ranked sentences are then used to create the summary with a sort algorithm.

    :param text: Inserted Text from textbox
    :param top_n: maximum length with standard value of 5

    :return: summarized text as a list
    """
    install_stopwords()
    summarized_text = []
    sentences, language = read(text)
    stop_words = stopwords.words(language)
    similarity_matrix = generate_sim_matrix(sentences, stop_words)
    similarity_graph = nx.from_numpy_array(similarity_matrix)  # Create graph from 2D Matrix
    ranks = nx.pagerank(similarity_graph)         # Create ranking of the nodes in the graph
    ranked_sentence = sorted(                                   # Sorting to get top sentences
        (
            (ranks[i], sentences_id) for i, sentences_id in enumerate(sentences)
        ),
        reverse=True)           # to get the top sentences
    for i in range(top_n):
        summarized_text.append(" ".join(ranked_sentence[i][1]))     # Build summary of ranked sentences list

    return summarized_text
