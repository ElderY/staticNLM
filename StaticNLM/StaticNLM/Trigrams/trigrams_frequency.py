import string
from Bigrams.bigrams_frequency import FrequentBigrams
from Unigrams.word_frequency import WordFrequency
from EndStartFilter import EndStart


class FrequentTrigrams:

    @staticmethod
    def trig_count(text):
        textsplit = text.lower().split()
        words = []
        trig_freq = {}
        wordsobj = EndStart()
        wordsobj.end_start_filter(textsplit, words)
        trig = [(words[i], words[i + 1], words[i + 2]) for i in range(len(words) - 2)]
        for t in trig:
            trig_freq[t] = trig_freq.get(t, 0) + 1
        return trig_freq

    @staticmethod
    def vocab_fill(text):
        words_list = text.lower().split()
        words = [word.strip(string.punctuation) for word in words_list if word.strip(string.punctuation)]
        vocab = sorted(set([w for w in words]))
        return vocab

if __name__ == "__main__":

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

    # print("Vocabulary:\n", Vocabulary.vocab_fill(corpus))
    print("Trigrams:\n", TrigramsModule.trig_freq)
    # print("Bigrams:\n", BigramsModule.context_bicount)
    # print("Unigrams:\n", UnigramsModule.context_unicount)