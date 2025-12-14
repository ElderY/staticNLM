import string

class WordFrequency():
    @staticmethod
    def freqcounter(text):
        words_freq = {}
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



        for w in words:
            words_freq[w] = words_freq.get(w, 0) + 1
        # word_freq_tuples = sorted(list(word_freq.items()), key= lambda x: (-x[1], x[0]))

        return words_freq




if __name__ == "__main__":
    with open(r"C:\Users\sasha\Desktop\alltasks.txt", "r", encoding="utf-8") as f:
        corpus = f.read()

    print(WordFrequency().freqcounter(corpus))