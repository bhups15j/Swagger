limit = 100
prime_list = []

def check_counter(i):
    counter = 1
    if i % 2 != 0:
        for j in range(1,i):
            if i % j == 0:
                counter += 1
                if counter > 2:
                    break
    return counter

def verify_prime(limit):
    for i in range(1,limit+1):
        counter_value = check_counter(i)
        if counter_value == 2:
            prime_list.append(i)

verify_prime(limit)
print(prime_list)
