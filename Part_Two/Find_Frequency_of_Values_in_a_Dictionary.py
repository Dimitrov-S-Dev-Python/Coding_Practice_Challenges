"""
Write a program that counts the frequency of each value in a dictionary.
The program should create a new dictionary to map each value in the
original dictionary to its frequency (how many times it occurs).
If the dictionary is empty, print an empty dictionary.
"""
my_dict ={
    "a":4,
    "b":4,
    "c":2,
    "d":7,
    "e":4,
    "f":2,
    "g":7,
    "h":7
}

if my_dict:
    freq_dict = {}
    for v in my_dict.values():
        if v not in freq_dict:
            freq_dict[v] = 0
        freq_dict[v] += 1
    print(freq_dict)
else:
    print("Empty")