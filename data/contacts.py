from model.contact import Contact
import random
import string

# закомичен рандомайзер
testdata = [Contact(firstname="firstname", middlename="middlename", lastname="lastname",
                    mobile="888", work_telephone="999", home_telephone="222",
                    email="test@test.ru", email2="test1@test.ru", address="test2@test.ru", id_contact=None)]

# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters+string.digits+string.punctuation+" "*10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# def random_numb(prefix, maxlen):
#     symbols = string.digits+string.punctuation+" "*10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# testdata =  [Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
#            lastname=random_string("lastname", 10), mobile=random_numb("", 10), work_telephone=random_numb("", 10),
 #           home_telephone=random_numb("", 10), email=random_string("email", 10), email2=random_string("email2", 10),
 #           address=random_string("address", 10), id_contact=None)
#    for i in range(1)
#]



