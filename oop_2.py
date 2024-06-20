class Watu:
    def __init__(self, jina, miaka):
        self.jina = jina
        self.miaka = miaka

    def display(self):
        print(self.jina, self.miaka)

my_watu = Watu(jina='John:', miaka='25')
my_watu.display()
my_watu2 = Watu(jina='Jack:', miaka='23')
my_watu2.display()
my_watu3 = Watu(jina='Zebedee:', miaka='22')
my_watu3.display()
