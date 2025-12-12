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
        textsplit = text.lower().split()
        textdotfilter = ["<START>"]
        words = []

        for w in textsplit:
            if "." in w[-1]:
                textdotfilter.append(w[:-1])
                textdotfilter.append("<END>")
                textdotfilter.append("<START>")
            else:
                textdotfilter.append(w)

        for w in textdotfilter:
            if w == "<START>" or w == "<END>":
                words.append(w)
            else:
                words.append(w.strip(string.punctuation))

        trig = [(words[i], words[i + 1], words[i + 2]) for i in range(len(words) - 2)]
        for t in trig:
            self.trig_freq[t] = self.trig_freq.get(t, 0) + 1

        return words

    def vocab_fill(self, text):
        words_list = text.lower().split()
        words = [word.strip(string.punctuation) for word in words_list if word.strip(string.punctuation)]
        self.vocab = sorted(set([w for w in words]))
        return self.vocab


with open(r"C:\Users\sasha\Desktop\alltasks.txt", "r", encoding="utf-8") as f:
    corpus = f.read()

UnigramsModule = WordFrequency()
UnigramsModule.context_unicount = UnigramsModule.freqcounter(corpus)

BigramsModule = FrequentBigrams()
BigramsModule.context_bicount = BigramsModule.bigrams_freq_count(corpus)
BigramsModule.context_unicount = UnigramsModule.context_unicount

TrigramsModule = FrequentTrigrams()
TrigramsModule.trig_freq = TrigramsModule.trig_count(corpus)
TrigramsModule.context_bicount = BigramsModule.context_bicount

Vocabulary = FrequentTrigrams()
Vocabulary.vocab_fill(corpus)

print("Vocabulary:\n", Vocabulary.vocab_fill(corpus))
print("Trigrams:\n", TrigramsModule.trig_freq)
print("Bigrams:\n", BigramsModule.context_bicount)
print("Unigrams:\n", UnigramsModule.context_unicount)
