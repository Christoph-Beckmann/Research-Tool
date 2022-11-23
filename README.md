<h1 align="center">
    ResearchTool
</h1>
<h5 align="center">
Summarize Text; Identify and Analyze Keywords; Do Research
</h5>
<h6 align="center">
by <a href="https://github.com/ChristophBeckmann">Christoph Beckmann</a> (2022)
</h6>

---

## Table of contents

1. [Description](#💡-description)
2. [How to install it](#⚙️-how-to-install-it)
    1. [Step 1: Install all needed packages](#📦-step-1-install-all-needed-packages)
    2. [Step 2: Run Application](#🏃-step-2-run-application)
3. [Jobs](#🔥-jobs)
    1. [1. Text summarization](#1-text-summarization)
    2. [2. Keyword identification](#2-keywords-identification)
    3. [3. Keyword analytics](#3-keyword-analytics)
    4. [4. Further research](#4-further-research)
4. [Licensing](#©️-licensing)

## 💡 Description

Every day, we are confronted with a huge amount of data digitally. 
Regarding this, it is becoming increasingly important to distinguish
the important from the unimportant. Time is becoming more and more precious
to everyone out there. 
</br></br>
For this reason, the large amount of data must be broken down to its essential components. 
This breaking down of data is achieved by **summarising texts**, as has been done for decades. 
This is the *first* functionality in this program.
</br></br>
But it is also important for us researchers to do further research. 
To do research, we need words that cover a sub-area and can connect knowledge into a network. 
These words represent keywords. 
In every text that conveys knowledge, there are keywords that are typical in their sub-area. 
Therefore, the *next step* is to extract them. This is the job of **keyword identification**.
</br></br>
However, since we do not want to limit ourselves to the keywords used by the author, 
but ideally want to use all the keywords specific to the subject area for our research, 
we have to find related keywords. However, since we do not want to limit ourselves to the 
keywords used by the author, but ideally want to use all the keywords specific
to the subject area for our research, we have to find related keywords. 
In the field of a systematic literature search, as is done in the best case to 
get the best information in a field (but of course cannot always be done due to time constraints),
generic terms, synonyms and sub-terms are searched for. 
Since this is not readily possible, the mass of data from Google is trusted. 
Google also tracks how terms relate to each other and can display related terms. 
I therefore used the Google Trend API to access these related keywords. This *third job* is 
called **keyword analytics**. But this program is also able to plot the interest of time about 
some related keywords.
</br></br>
The last and *fourth job* is to do **research on a specific keyword**.
Here, however, not only scientific literature should be used, 
as articles or blog entries can also be summarised,
but also articles, books and journal articles should be used. 
For this purpose, a web scraper is used to find up to ten entries in 
Google Scholar and to present them in tabular form.

---

## ⚙️ How to install it

### 📦 Step 1: Install all needed packages

This package is working with a lot of other packages. 
Therefore the first step is to install the requirements for my package.
I created a requirements textfile which contains all needed modules (*requirements.txt*).
This makes it easy for a package installer like *pip* to install all modules automatically.

I recommend using a separate python interpreter for this project.
There are several ways to do it:
* [PyCharm Tutorial](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add_new_project_interpreter)
* [Visual Studio](https://docs.microsoft.com/en-us/visualstudio/python/installing-python-interpreters?view=vs-2022)
* Manual, described below

**Manual:**

Firstly, create virtual environment in project folder.
Therefore, use ``cd`` and change current working dir to project folder.
Then create the virtual environment with: 
``python3 -m venv venv_researchtool``
The *venv_researchtool* is the name of the virtual environment and can be
customized to personal preferences. 

Secondly, we have to activate our virtual environment with
``source venv_researchtool/bin/activate``.

Lastly, we are able to install all required packages for our virtual environment.
With our package manager *pip*.
Use therefore ``pip install -r requirements.txt``.
Our package manager will then install all packages automatically.

Well done, you successfully installed all needed packages! 🎉

### 🏃 Step 2: Run application

Before starting the main application make sure you activated the current 
virtual environment 
(as mentioned above with ``source venv_researchtool/bin/activate``).
After that use ``cd gui`` to change current working dir to *gui* and
start the MainForm with ``python3 gui_mainmenu.py``.

Congratulation! You started the application successfully! 🥳

---

## 🔥 Jobs
In following, the in the introduction described jobs are now
presented more precisely. 

### 1. Text summarization

After reading some academic articles on text summarization, 
I came to the conclusion that there were two types of text summarization. 
The extractive approach, and the abstractive approach. 
These approaches differ significantly in their text processing. 

The abstractive approach is much more accurate than the extractive approach 
and more human like. It works not only on a mathematical level, 
but also on a semantic level. There are algorithms that can do this, 
but they are highly complex.

The extractive approach uses the existing words to create a summary 
with mathematical operations. It makes use of metrics such as *cosine similiarty*, 
*matrices* and *network graphs*. I used the following article to familiarise myself 
with the topic: [Sciencedirect](https://www.sciencedirect.com/topics/computer-science/cosine-similarity). 
This approach was used in this project.

To improve its output, it is also important to remove stopwords from the summary.
For this purpose, there are packages to obtain the corresponding *stopwords*.
I used the *Natural Language Package* (*NLP*) for this. 
This package also contains the mathematical functionalities to calculate 
the metric key figures (cosine similarity). 
The summary of text should also be language-independent.
For this purpose, I used a package for language recognition (*languagedetection*). 
This allows the use of language-specific stopwords and thus improves the 
summary function even across different languages. 

Roughly speaking, the first step is to divide the text into its individual parts 
(sentences). Afterwards, the cosine similarity is formed from these vectors 
and the corresponding matrix is formed. In order to be able to rank the sentences, 
the matrix must be converted into a graph using *numpy*. 
The resulting ranking is then the summary. However, only the number of sentences 
that you want to have output are taken. 

### 2. Keywords identification 

There are some algorithms that do keyword extraction using machine learning. 
However, this requires a lot of text to train the algorithm so that it identifies 
the keywords correctly. However, I used an unsupervised approach. 
This extraction has the following functionalities:

1. text pre-processing and candidate term identification; 
2. feature extraction; 
3. computing term score; 
4. n-gram generation and computing candidate keyword score 
5. data deduplication and ranking. 

This was also done with the Natural Language Package (NLP) and *Yake*. 
Which contains the necessary algorithms for the functionalities described above.
The following settings can be made:

* Wordcount:
  * This number represents the number of keywords that are considered as one keyword. 
  * It is always assumed <=. If the number is two, a keyword up to a length of two is included in the calculation.
* Duplication Threshold:
  * This value allows duplicates and can be set on a scale from 0.1 to 0.9. 
  * Duplicates are allowed at 0.9. 
  * This allows the result to be adjusted to the text.
* Max Keywords:
  * This limits the number of keywords to be found and also assumes <=. 

In my program the functionality of 2. and the following 3. are combined into one gui.

### 3. Keyword analytics 

As already described in the introduction, I used the Google API (*Pytrend*) to find relevant terms.
In particular, the trend query, which can be accessed via 
[Google Trend](https://trends.google.com/trends/?geo=US). 
For the keyword that I send and have selected in the list box, 
I receive a DataFrame back with a lot of data about the keyword. 
For me, however, only the related terms to the keyword are interesting.
I process this data frame and only access the top related keywords, 
which I then display in another list box.

Furthermore, it is possible to select *up to five* (!) related keywords
to show the interest of the keyword over time. </br></br>
The results shown have the following meaning:
* A value of 100 is the peak popularity for the term. 
* A value of 50 means that the term is half as popular.
* A score of 0 means that there was not enough data for this term.


### 4. Further research

To find more articles, books or journal articles, I used *Google Scholar*. 
Via web scraping I access the results from the POST command. 
I give this POST command a header to prevent blocking via *web scraping*
(this is very typical in the area of web scraping) and 
the parameters(*search query* and *language*).
Via a WebScraping package (*BeautfilSoup4*) I then access the results 
of the post command and store them in a list of dictionaries. 
Then I display them in a treeview.  
As a last feature, it is possible to open the link I scrape to directly access and sift the source.

Unfortunately, only a result number of ten is possible with this method. 

---

## ©️ Licensing

### MIT License

#### Copyright © (2022) [Christoph Beckmann](https://github.com/ChristophBeckmann)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

*Created with [ChooseLicense](https://choosealicense.com/)*.