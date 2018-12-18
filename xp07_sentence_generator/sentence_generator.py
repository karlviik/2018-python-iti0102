"""Do generating."""

class Generator:
    """Generator for just one list of outputs."""

    def __init__(self, name, yields):
        """Save name and yields."""
        self.name = name
        self.yields = yields

    def addsome(self, yields):
        """Add yields to yields."""
        self.yields += yields

    def gen(self):
        """Yield an output."""
        while True:
            if self.yields == [self.name]:
                yield "???"
            else:
                while True:
                    for thing in self.yields:
                        yield thing


class SentenceGenerator:
    """Generator for whole more complex thingsies."""

    def __init__(self, rules_string):
        """Construct smaller generators based on rules and save them and their names."""
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
        """Actual generator loop."""
        while True:
            sentence = []
            if type(syntax) is str:
                syntax = syntax.split()
            for word in syntax:
                symbol = ""
                for letter in word[::-1]:
                    if letter in ['.', ',', '!', '?']:
                        symbol = letter + symbol
                        word = word[:-1]
                    else:
                        break
                if word not in self.gennames:
                    sentence.append(word + symbol)
                else:
                    index = self.gennames.index(word)
                    x = next(self.gens[index])
                    list = next(self.generator(x))
                    list[-1] = list[-1] + symbol
                    sentence += list
            yield sentence

    def sentence_generator(self, syntax):
        """Run the generator and make returned list into proper sentence."""
        while True:
            x = " ".join(next(self.generator(syntax)))
            yield x


if __name__ == '__main__':
    rules = """
    a = tere | tulemast
    b = a
    c = b. b?
    """
    g = SentenceGenerator(rules)
    gg = g.sentence_generator("a  g")
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
    print(next(gg))
