from model.contact import Contact
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+string.punctuation+" "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_numb(prefix, maxlen):
    symbols = string.digits+string.punctuation+" "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata =  [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 10), mobile=random_numb("", 10), work_telephone=random_numb("", 10),
            home_telephone=random_numb("", 10), email=random_string("email", 10), email2=random_string("email2", 10),
            address=random_string("address", 10), id_contact=None)
    for i in range(1)
]

# [Contact(firstname="", middlename="", lastname="",
                    # mobile="", work_telephone="", home_telephone="",
                    # email="", email2="", address="", id_contact=None)]+
#