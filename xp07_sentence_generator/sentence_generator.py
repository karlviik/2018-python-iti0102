class Generator:
    def __init__(self, name, yields):
        self.name = name
        self.yields = yields

    def add(self, yields):
        self.yields += yields

    def gen(self):
        if self.yields == [self.name]:
            return "???"
        else:
            while True:
                for thing in self.yields:
                    yield thing


class SentenceGenerator:

    def __init__(self, rules_string):
        self.gennames = []
        self.gens = []
        for line in rules_string.splitlines():
            if not len(line.strip()):
                continue
            line = line.split("=")
            line[0] = line[0].split()

            yields = line[1].split("|")
            newyields = []
            for yi in yields:
                yi = yi.strip().split()
                newyields.append(yi)
            gen = Generator(line[0], newyields)
            self.gennames.append(line[0][0])
            self.gens.append(gen.gen())

    def generator(self, syntax):
        while True:
            sentence = []
            if type(syntax) is str:
                syntax = syntax.split()
            for word in syntax:
                while True:
                    if word not in self.gennames:
                        sentence.append(word)
                        break
                    else:
                        index = self.gennames.index(word)
                        x = next(self.gens[index])
                        sentence += next(self.generator(x))
                        break
            yield sentence

    def sentence_generator(self, syntax):
        while True:
            x = " ".join(next(self.generator(syntax)))
            yield x
        """
        while True:
            sentence = []
            if type(syntax) is str:
                syntax = syntax.split()
            for word in syntax:
                while True:
                    if word not in self.gennames:
                        sentence.append(word)
                        break
                    else:
                        index = self.gennames.index(word)
                        x = next(self.gens[index])
                        sentence += next(self.sentence_generator(x))
                        break
            yield sentence"""


if __name__ == '__main__':
    rules = """
    noun = koer | porgand | madis | kurk | tomat
    target = koera | porgandit | madist | kurki | tomatit
    verb = sööb | lööb | jagab | tahab | ei taha
    adjective = ilus | kole | pahane | magus | sinu
    targetadjective = ilusat | koledat | pahast | magusat | sinu
    sentence = noun verb target .
    beautifulsentence = adjective noun verb targetadjective target .
    twosentences = sentence sentence
    """

    g = SentenceGenerator(rules)
    gg = g.sentence_generator("beautifulsentence noun")
    print("wat")
    print(next(gg))
