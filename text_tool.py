
class TextTool:

    def __init__(self, str1, target):
        self.str1 = str1
        self.target = target

    def str_length(self):
        return len(self.str1)

    def str_concat(self, str2):
        return self.str1+ " "+str2
    
    def convert_lowercase(self):
        return self.str1.lower()

    def convert_uppercase(self):
        return self.str1.upper()

    def convert_titlecase(self):
        return self.str1.title()
    
    def str_strip(self):
        return self.str1.strip()

    def str_rstrip(self):
        return self.str1.rstrip()

    def str_lstrip(self):
        return self.str1.lstrip()

    def str_startwith(self):
        return self.str1.startswith(self.target)

    # find letter in a given string with index
    def find_target_str(self):
        index = 0
        for i in self.str1:
            if i == self.target:
                print(i)
                print(index)
            index = index+1
        
    # find word in a given string 
    def find_word(self):
        if self.target in self.str1:
            print(f"{self.target} present.")

    #find vowel word in a given string
    def find_vowel_word(self):
        vlists = ["a","e","i","o","u"]
        targets = self.str1.split()
        for target in targets:
            if target.lower()[0] in vlists:
                print(f"{target.lower()[0]} : {target}")
        return targets

    

        