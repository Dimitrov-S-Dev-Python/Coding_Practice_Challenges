"""concatenate this files with links into a single text file.
The content of the output file should look like below.

Expected output:
x,y
3,5
4,9
6,10
7,11
8,12
6,10
8,18
12,20
14,22
16,24
"""
import pandas

link_one = "https://pythonhow.com/media/data/sampledata.txt"
link_two ="https://pythonhow.com/media/data/sampledata_x_2.txt"
data_one = pandas.read_csv(link_one)
data_two = pandas.read_csv(link_two)
data_one_and_two = pandas.concat([data_one, data_two])
# data_one_and_two.to_csv("location.txt", index=None)
