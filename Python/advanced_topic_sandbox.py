# Create a list between 0 and 15

my_list = range(16)

print my_list

# Only print numbers that are divisable by 3

print filter(lambda x: x % 3 == 0, my_list)
