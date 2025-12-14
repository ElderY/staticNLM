import string

class EndStart:

    def end_start_filter(self,textsplit, wordslist):
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
                wordslist.append(w)
            else:
                wordslist.append(w.strip(string.punctuation))

