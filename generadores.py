def my_gen():
    a = 1
    yield a

    a = 2
    yield a

    a = 3
    yield a


my_list_gen = my_gen()

print(next(my_list_gen))
print(next(my_list_gen))
print(next(my_list_gen))
