dir(str)
help(str.replace)

a = 'hello'

new_a = a.replace('l','p')
print(new_a)

help(dict.values)
help(dict.keys)

print(isinstance("abc", str))

help(max)

def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))
