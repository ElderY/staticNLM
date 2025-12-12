import string

class EndStartFilter:

    def end_start_filter(self,textsplit, words):
        textdotfilter = ["<START>"]
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

