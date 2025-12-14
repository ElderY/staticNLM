import string
from Bigrams.bigrams_frequency import FrequentBigrams
from Unigrams.word_frequency import WordFrequency

class SequenceProbabilityBigrams(FrequentBigrams, WordFrequency):

    @staticmethod
    def bigrams_prob_count(bigramsfreq, unigramsfreq):
        p = {}
        for (w1,w2), n in bigramsfreq.items():
            c = float(n/unigramsfreq.get(w1, 0))
            if w1 not in p:
                p[w1] = {}
            p[w1][w2] = c
        return p

    @staticmethod
    def prob_sum(probs):
        values_list = []
        for w, n in probs.items():
            probs = [p for w, p in n.items()]
            sumprobs = sum(probs)
            values_list.append(f"{w} - {sumprobs}")
        return values_list

with open(r"C:\Users\sasha\Desktop\alltasks.txt", "r", encoding="utf-8") as f:
        corpus = f.read()

if __name__ == "__main__":

    UnigramsModule = SequenceProbabilityBigrams()
    UnigramsModule.words_freq = UnigramsModule.freqcounter(corpus)

    BigramsModule = SequenceProbabilityBigrams()
    BigramsModule.bigrams_freq = BigramsModule.bigrams_freq_count(corpus)
    BigramsProb = SequenceProbabilityBigrams.bigrams_prob_count(BigramsModule.bigrams_freq, UnigramsModule.words_freq)

    print(BigramsProb)

    # print("PROBABILITIES SUM:\n"
    #       ,SequenceProbabilityBigrams.prob_sum(SequenceProbabilityBigrams.bigrams_prob_count(BiCount.bigrams_freq, UniCount.words_freq)))
