import matplotlib.pyplot as plt


class Graph:
    def __init__(self, list_of_cmp):
        self.list_of_cmp = list_of_cmp

    def market_cap_graph(self):
        names = []
        values = []
        for cmp in self.list_of_cmp:
            values.append(cmp.market_cap)
            names.append(cmp.symbol)

        plt.bar(names, values, width=0.4)
        plt.xlabel('Companies')
        plt.ylabel('Market Cap')
        plt.title('Market Capitalization(bil.)')
        plt.show()

    def pe_graph(self):
        names = []
        values = []
        for cmp in self.list_of_cmp:
            values.append(cmp.pe)
            names.append(cmp.symbol)

        plt.bar(names, values, width=0.4)
        plt.xlabel('Companies')
        plt.ylabel('PE')
        plt.title('PE')
        plt.show()

    def pb_graph(self):
        names = []
        values = []
        for cmp in self.list_of_cmp:
            values.append(cmp.pb)
            names.append(cmp.symbol)

        plt.bar(names, values, width=0.4)
        plt.xlabel('Companies')
        plt.ylabel('PB')
        plt.title('PB')
        plt.show()

    def ps_graph(self):
        names = []
        values = []
        for cmp in self.list_of_cmp:
            values.append(cmp.ps)
            names.append(cmp.symbol)

        plt.bar(names, values, width=0.4)
        plt.xlabel('Companies')
        plt.ylabel('PS')
        plt.title('PS')
        plt.show()

    def eps_graph(self):
        names = []
        values = []
        for cmp in self.list_of_cmp:
            values.append(cmp.eps)
            names.append(cmp.symbol)

        plt.bar(names, values, width=0.4)
        plt.xlabel('Companies')
        plt.ylabel('EPS')
        plt.title('EPS')
        plt.show()

    def div_yield_graph(self):
        names = []
        values = []
        for cmp in self.list_of_cmp:
            values.append(cmp.div_yield)
            names.append(cmp.symbol)

        plt.bar(names, values, width=0.4)
        plt.xlabel('Companies')
        plt.ylabel('Div_yield')
        plt.title('Dividiend yield(%)')
        plt.show()

