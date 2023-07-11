# Find the most used word in a given text file 
file = input('Enter filename: ')
file_handle = open(file)

count_dict = dict()
for line in file_handle:
    words = line.split()

    for word in words:
        count_dict[word] = count_dict.get(word, 0) + 1

# print(count_dict)

bigcount = None 
bigword = None 
for key,value in count_dict.items():
    if bigcount is None or value > bigcount:
        bigword = key 
        bigcount = value

print(bigword, bigcount)