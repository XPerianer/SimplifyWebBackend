# -*- coding: utf-8 -*-

# %%

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from transformers import BartTokenizer, BartForConditionalGeneration

TEST_TEXT = """
Like keyphrase extraction, document summarization aims to identify the essence of a text. The only real difference is that now we are dealing with larger text units—whole sentences instead of words and phrases.
Before getting into the details of some summarization methods, we will mention how summarization systems are typically evaluated. The most common way is using the so-called ROUGE (Recall-Oriented Understudy for Gisting Evaluation) measure. This is a recall-based measure that determines how well a system-generated summary covers the content present in one or more human-generated model summaries known as references. It is recall-based to encourage systems to include all the important topics in the text. Recall can be computed with respect to unigram, bigram, trigram, or 4-gram matching. For example, ROUGE-1 is computed as division of count of unigrams in reference that appear in system and count of unigrams in reference summary.
If there are multiple references, the ROUGE-1 scores are averaged. Because ROUGE is based only on content overlap, it can determine if the same general concepts are discussed between an automatic summary and a reference summary, but it cannot determine if the result is coherent or the sentences flow together in a sensible manner. High-order n-gram ROUGE measures try to judge fluency to some degree. Note that ROUGE is similar to the BLEU measure for machine translation, but BLEU is precision- based, because translation systems favor accuracy.
A promising line in document summarization is adaptive document/text summarization.[12] The idea of adaptive summarization involves preliminary recognition of document/text genre and subsequent application of summarization algorithms optimized for this genre. First summarizes that perform adaptive summarization have been created.[13]
"""

model = BartForConditionalGeneration.from_pretrained('sshleifer/distilbart-cnn-12-6')
tokenizer = BartTokenizer.from_pretrained('sshleifer/distilbart-cnn-12-6')

cache = {}


def summarize(text: str, score: float) -> str:

    print(f"Using score: ${score}")
    if score > 0.5:
        if text in cache:
            return cache[text]
        inputs = tokenizer(text, return_tensors="pt")
        tokens = model.generate(**inputs)

        summary = tokenizer.decode(tokens.squeeze(), skip_special_tokens=True)
        cache[text] = summary
        return summary
    else:
        return text


def test():
    summarized_text = summarize(TEST_TEXT, 51)
    print(summarized_text)


# %%

if __name__ == "__main__":
    test()
