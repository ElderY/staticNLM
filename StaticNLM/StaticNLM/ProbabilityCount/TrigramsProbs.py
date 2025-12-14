import string
from Trigrams.trigrams_frequency import FrequentTrigrams
from BigramsProbs import SequenceProbabilityBigrams

class SequenceProbabilityTrigrams(FrequentTrigrams, SequenceProbabilityBigrams):

    @staticmethod
    def trigrams_prob_count(trigramsfreq, bigramsfreq):
        p = {}
        for (w1,w2,w3), n in trigramsfreq.items():
            m = bigramsfreq.get((w1, w2), 0)
            c = float(n/m)
            if (w1, w2) not in p:
                p[(w1, w2)] = {}
            p[(w1, w2)][w3] = c
        return p

with open(r"C:\Users\sasha\Desktop\alltasks.txt", "r", encoding="utf-8") as f:
    corpus = f.read()

if __name__ == "__main__":

    BigramsModule = SequenceProbabilityBigrams()
    BigramsModule.bigrams_freq = BigramsModule.bigrams_freq_count(corpus)

    TrigramsModule = SequenceProbabilityTrigrams()
    TrigramsModule.trig_freq = TrigramsModule.trig_count(corpus)
    TrigramsProb = SequenceProbabilityTrigrams().trigrams_prob_count(TrigramsModule.trig_freq, BigramsModule.bigrams_freq)

    # print(BigramsModule.bigrams_freq)
    # print(TrigramsModule.trig_freq)
    print(TrigramsProb)
