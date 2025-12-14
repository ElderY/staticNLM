from ProbabilityCount.UnigramsProbs import SequenceProbabilityUnigrams
from ProbabilityCount.BigramsProbs import SequenceProbabilityBigrams, corpus
from ProbabilityCount.TrigramsProbs import SequenceProbabilityTrigrams
from Unigrams.word_frequency import WordFrequency


class Generator(SequenceProbabilityUnigrams, SequenceProbabilityBigrams, SequenceProbabilityTrigrams, WordFrequency):

    @staticmethod
    def generate_text(triprobs, biprobs, uniprobs, wordfreq):
       pass

    with open(r"C:\Users\sasha\Desktop\alltasks.txt", "r", encoding="utf-8") as f:
        corpus = f.read()


UnigramsModule = Generator()
UnigramsModule.words_freq = UnigramsModule.freqcounter(corpus)
UnigramsProb = SequenceProbabilityUnigrams.unigrams_prob_count(UnigramsModule.words_freq, corpus)

BigramsModule = Generator()
BigramsModule.bigrams_freq = BigramsModule.bigrams_freq_count(corpus)
BigramsProb = SequenceProbabilityBigrams.bigrams_prob_count(BigramsModule.bigrams_freq, UnigramsModule.words_freq)

TrigramsModule = Generator()
TrigramsModule.trig_freq = TrigramsModule.trig_count(corpus)
TrigramsProb = SequenceProbabilityTrigrams().trigrams_prob_count(TrigramsModule.trig_freq, BigramsModule.bigrams_freq)

print(TrigramsProb)