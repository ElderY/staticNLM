import string
from Unigrams.word_frequency import WordFrequency

class SequenceProbabilityUnigrams(WordFrequency):

    @staticmethod
    def unigrams_prob_count(unigramsfreq, text):
        p = {}
        textsplit = text.lower().split()
        textclear = [n.strip(string.punctuation) for n in textsplit if n.strip(string.punctuation)]
        t = len(textclear)
        for w, n in unigramsfreq.items():
            p[w] = float(n/t)
        return p


with open(r"C:\Users\sasha\Desktop\alltasks.txt", "r", encoding="utf-8") as f:
    corpus = f.read()

if __name__ == "__main__":

    UnigramsModule = WordFrequency.freqcounter(corpus)
    UnigramsProb = SequenceProbabilityUnigrams().unigrams_prob_count(UnigramsModule ,corpus)

    print(UnigramsProb)