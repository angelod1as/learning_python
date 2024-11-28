import pickle
from pathlib import Path

curr_dir = Path(__file__).parent

# Saving

my_list = [0, 1, 2]
my_dict = {'a': 1, 'b': 2}

with open(curr_dir / 'pickles' / 'my_list.pickle', 'wb') as file:  # writes in BYTES
    pickle.dump(my_list, file)

with open(curr_dir / 'pickles' / 'my_dict.pickle', 'wb') as file:
    pickle.dump(my_dict, file)

# Reading

with open(curr_dir / 'pickles' / 'my_list.pickle', 'rb') as file:
    my_read_list = pickle.load(file)

with open(curr_dir / 'pickles' / 'my_dict.pickle', 'rb') as file:
    my_dict_list = pickle.load(file)

# Saving a class instance


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def who_am_i(self):
        print(f'I am {self.name}, {self.age} years old')


inst_joao = Person('Joao', 30)

with open(curr_dir / 'pickles' / 'inst_joao.pickle', 'wb') as file:
    pickle.dump(inst_joao, file)


# Reading
with open(curr_dir / 'pickles' / 'inst_joao.pickle', 'rb') as file:
    inst_joao_read = pickle.load(file)

inst_joao_read.who_am_i()
