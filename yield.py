import random

limit = 11              # define the limit
test_data = []
def create_ref_data():
    for x in range(1,limit):
        test_data.append(x)
    return test_data

def yield_print():
    test_data = create_ref_data()
    a = random.randint(0,len(test_data)-1)
    yield a

def generate_no():
    test_data = create_ref_data()
    for check in range(0,len(test_data)):
        data = yield_print()

        for i in data:
            print(test_data[i])
            test_data.remove(test_data[i])

    
generate_no()
