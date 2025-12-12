import string
from Bigrams.bigrams_frequency import FrequentBigrams
from Unigrams.word_frequency import WordFrequency


class FrequentTrigrams:
    def __init__(self):
        self.trig_freq = {}
        self.context_bicount = {}
        self.context_unicount = {}
        self.vocab = []

    def trig_count(self, text):
        words_list = text.lower().split()
        words = [word.strip(string.punctuation) for word in words_list if word.strip(string.punctuation)]

        trig = [(words[i], words[i+1], words[i+2]) for i in range(len(words)-2)]
        for t in trig:
            self.trig_freq[t] = self.trig_freq.get(t, 0)+1

        return self.trig_freq

    def vocab_fill(self, text):
        words_list = text.lower().split()
        words = [word.strip(string.punctuation) for word in words_list if word.strip(string.punctuation)]
        self.vocab = sorted(set([w for w in words]))
        return self.vocab



with open(r"C:\Users\sasha\Desktop\alltasks.txt", "r", encoding= "utf-8") as f:
    corpus = f.read()


TrigramsModule = FrequentTrigrams()
TrigramsModule.trig_freq = TrigramsModule.trig_count(corpus)

BigramsModule = FrequentBigrams()
BigramsModule.context_bicount = BigramsModule.bigrams_freq_count(corpus)

UnigramsModule = WordFrequency()
UnigramsModule.context_unicount = UnigramsModule.freqcounter(corpus)

Vocabulary = FrequentTrigrams()
Vocabulary.vocab_fill(corpus)

print("Vocabulary:\n", Vocabulary.vocab_fill(corpus))
print("Trigrams:\n", TrigramsModule.trig_freq)
print("Bigrams:\n", BigramsModule.context_bicount)
print("Unigrams:\n", UnigramsModule.context_unicount)