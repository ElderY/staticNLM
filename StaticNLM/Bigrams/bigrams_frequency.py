import string
import matplotlib.pyplot as plt


class FrequentBigrams:


    @staticmethod
    def bigrams_freq_count(text):
        bigrams_freq = {}
        bigrams = []
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

        for i in range(len(words) - 1):
                word_current = words[i]
                word_next = words[i + 1]
                # bigrams = [(words[i], words[i + 1] for i in range(len(words)-1))]
                bigrams.append((word_current, word_next))
        for pair in bigrams:
            bigrams_freq[pair] = bigrams_freq.get(pair , 0) + 1

        # bigrams_topten = sorted(list(bigrams_freq.items()), key= lambda x: (-x[1], x[0]))

        return bigrams_freq



if __name__ == "__main__":
    with open(r"C:\Users\sasha\Desktop\alltasks.txt", "r", encoding="utf-8") as f:
        corpus = f.read()

    print(FrequentBigrams().bigrams_freq_count(corpus))

# if __name__ == "__main__":
#     bigrams_plot = (FrequentBigrams().bigrams_freq_count(corpus))
#     labels = [f"{a} {b}" for (a,b), count in bigrams_plot]
#     counts = [count for (bigram, count) in bigrams_plot]
#
#     plt.figure(figsize=(10,6))
#     plt.bar(labels, counts)
#     plt.xlabel("Bigrams")
#     plt.ylabel("Frequency")
#     plt.title("Top 10 Bigrams")
#     plt.xticks(rotation=20)
#     plt.show()
