def order(sentence):
    return " ".join(sorted(sentence.split(), key=min))