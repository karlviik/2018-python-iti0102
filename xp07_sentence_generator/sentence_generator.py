class Generator:
    def __init__(self, name, yields):
        self.name = name
        self.yields = yields

    def addsome(self, yields):
        self.yields += yields

    def gen(self):
        while True:
            if self.yields == [self.name]:
                yield "???"
            else:
                while True:
                    for thing in self.yields:
                        yield thing


class SentenceGenerator:

    def __init__(self, rules_string):
        self.gennames = []
        self.tempgens = []
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

            if line[0][0] in self.gennames:
                self.tempgens[self.gennames.index(line[0][0])].addsome(newyields)
            else:
                gen = Generator(line[0], newyields)
                self.gennames.append(line[0][0])
                self.tempgens.append(gen)
        self.gens = []
        for gen in self.tempgens:
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


if __name__ == '__main__':
    rules = """
    a = a | 2 | 3
    """
    g = SentenceGenerator(rules)
    gg = g.sentence_generator("a")
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))