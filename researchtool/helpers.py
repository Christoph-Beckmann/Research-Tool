from langdetect import detect                       # Language Detection in ISO639-1
import iso639                                       # Transform ISO639-1 to ISO language name for stopwords file


# Automatic detection of the language and conversion from "de" to "Deutsch" using the packages Langdetect and ISO639.
def detectlanguage(text, short: bool):
    if short:                                       # Deutsch to de
        language = iso639.to_name(detect(text))
    else:
        language = detect(text)                     # Deutsch
    return language
