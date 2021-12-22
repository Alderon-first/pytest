class Group:

    def __init__(self, name=None, header=None, footer=None, id_group=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id_group = id_group

    def __repr__(self):
        return "%s:%s" % (self.id_group, self.name)
        # это про вывод информации на консоль

    def __eq__(self, other):
        return self.id_group == other.id_group and self.name == other.name
        # это про логическое сравнение параметров (чтобы сравнивалось значение, а не значение+расположение информации)

