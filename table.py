class Presentation(object):
    def __init__(self):
        self.headers = []
        self.rows = []
        self.footers = []

    def add_titles(self, titles):
        self.titles = titles

    def add_headers(self, headers):
        self.headers += headers
        print(self.headers)

    def add_rows(self, rows):
        self.rows.append(rows)
    
    def add_footers(self, footer):
        self.footers.append(footer)
    
    def clear_rows(self):
        self.rows = []

    @property
    def separator(self):
        return str("+"+"-"*60+"+\n")

    def __repr__(self):
        table = ""
        table += self.separator
        for title in list(self.titles):
            table += f"{title:<40}{self.titles[title]:^20}\n"
            table += self.separator
            for header in self.headers:
                for cell in header:
                    table += f"{cell:^20}"
                table += "\n"
                for row in self.rows:
                    for cell in row:
                        table += f"{cell:^20}"
                    table += "\n"
                table += self.separator
        for footer in self.footers:
            table += f"{footer:^60}\n"
        table += self.separator
        return table


if __name__ == "__main__":
    p = Presentation()
    p.add_titles({"Texte a encoder :": "0101", "Binaire encodé :": "1010"})
    p.add_headers([["Lettre", "Binaire", "Hamming"],
                   ["Binaire", "Hamming", "Lettre"]])
    p.add_rows(["aaa", "bbb", "ccc"])
    p.add_rows(["aaa2", "bbb", "ccc"])
    p.add_rows(["aaa3", "bbb", "ccc"])
    p.add_footers("test")
    p.add_footers("test2")
    print(p)
