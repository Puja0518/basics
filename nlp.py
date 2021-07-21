
class Nlp:

    def __init__(self, sentence, target):
        self.sentence = sentence
        self.target = target

    def str_replace(self, target2):
        #self.target2 = target2
        return self.sentence.replace(self.target , target2)

    def split(self):
        return self.sentence.split()

    def index_range(self):
        result = self.sentence.index(self.target)
        return f" range {result}: {result+len(self.target)}"

    def str_prefix(self, total_no, prifix):
        return self.sentence.rjust(total_no, prifix)

    def split_based_on_target(self, target):
        return self.sentence.split(target)



temp = Nlp("ritul saini is bad boy ", "bad")
print(temp.index_range())

print(temp.str_replace("good"))

print(temp.split())

exp = Nlp( "tudu" , 'hambira')
t = exp.str_prefix(5,'h')
print(f"dante{t}")

test = Nlp("hambira@shital", "shital")
print(test.split_based_on_target("@"))