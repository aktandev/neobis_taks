class Dictionary():

    def __init__(self):
        self.my_dict = {}

    def newentry(self, word, definition):
        self.my_dict[word] = definition


    def look(self, key):
        if key in self.my_dict:
            return self.my_dict[key]
        else: return f"Can't find entry for {key}"


d = Dictionary()
print(d.newentry('apple', 'its phone'))
print(d.look('apple'))