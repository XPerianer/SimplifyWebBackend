# -*- coding: utf-8 -*-

#%%

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import nltk
# uncomment and run this the first time to install
# nltk.download('punkt')

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"

TEST_TEXT = """
Like keyphrase extraction, document summarization aims to identify the essence of a text. The only real difference is that now we are dealing with larger text units—whole sentences instead of words and phrases.
Before getting into the details of some summarization methods, we will mention how summarization systems are typically evaluated. The most common way is using the so-called ROUGE (Recall-Oriented Understudy for Gisting Evaluation) measure. This is a recall-based measure that determines how well a system-generated summary covers the content present in one or more human-generated model summaries known as references. It is recall-based to encourage systems to include all the important topics in the text. Recall can be computed with respect to unigram, bigram, trigram, or 4-gram matching. For example, ROUGE-1 is computed as division of count of unigrams in reference that appear in system and count of unigrams in reference summary.
If there are multiple references, the ROUGE-1 scores are averaged. Because ROUGE is based only on content overlap, it can determine if the same general concepts are discussed between an automatic summary and a reference summary, but it cannot determine if the result is coherent or the sentences flow together in a sensible manner. High-order n-gram ROUGE measures try to judge fluency to some degree. Note that ROUGE is similar to the BLEU measure for machine translation, but BLEU is precision- based, because translation systems favor accuracy.
A promising line in document summarization is adaptive document/text summarization.[12] The idea of adaptive summarization involves preliminary recognition of document/text genre and subsequent application of summarization algorithms optimized for this genre. First summarizes that perform adaptive summarization have been created.[13]
"""

#%%

def summarize(text: str, score: float) -> str:

    tokenizer = Tokenizer(LANGUAGE)
    parser = PlaintextParser.from_string(text, tokenizer)
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    document = parser.document

    summary = summarizer(document, int(score * len(document.sentences)))
    summary_sentences = list(str(s) for s in summary)

    summary_string = " ".join(summary_sentences)
    return summary_string

def test():
    summarized_text = summarize(TEST_TEXT, 0.2)

    for sentence in summarized_text:
        print(sentence)

#%%

if __name__ == "__main__":
    test()
