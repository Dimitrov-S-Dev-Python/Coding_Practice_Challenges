"""
Multiply the values of the text file in the URL by two and
export the output to a new file
"""
import pandas

URL = "https://pythonhow.com/media/data/sampledata.txt"
df = pandas.read_csv(URL)
result = df * 2
result.to_csv("new_data.txt", index=None)
