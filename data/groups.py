# import random
# import string
from model.group import Group

testdata = [
    Group(name="name", header="header", footer="footer"),
    Group(name="name1", header="name2", footer="name3")
]

# Закомичена рандмная генерация
# def random_string(prefix, maxlen):
#    symbols = string.ascii_letters+string.digits+string.punctuation+" "*10
#    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#testdata = [Group(name="", header="", footer="")] + [
#    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
#    for i in range(1)
#]

