import logging
import ssl                                          # Secure Sockets Layer - Internet Protocol
from nltk import download                           # Natural Language Toolkit: https://www.nltk.org/
from langdetect import detect                       # Language Detection in ISO639-1
import iso639                                       # Transform ISO639-1 to ISO language name for stopwords file

logger = logging.getLogger(__name__)


def install_stopwords():
    """
    Nltk Downloader is broken. There is a workaround to download the required "stopwords" package.
    This code disable the SSL Certificate Verification.
    Found solution on: https://github.com/gunthercox/ChatterBot/issues/930#issuecomment-322111087
    """
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context

    download("stopwords")     # Adapted to download only the required package from nltk


def detectlanguage(text, short: bool):
    """ Automatic detection of the language + conversion from "de" to "German" using the packages Langdetect and ISO639.
    :param text: Inserted text from Textbox
    :param short: Should the recognised language be converted to ISO 639 format?
    :type short: Boolean: Yes or No

    :return: Returns language
    """
    if short:                                       # de to German
        language = iso639.to_name(detect(text))
    else:
        language = detect(text)                     # de
    return language
