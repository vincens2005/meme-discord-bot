#!/bin/python3
import markovify

filename = "kansas.txt"

file = open(filename)
text = file.read()

model = markovify.Text(text, state_size=1)

top_text = model.make_short_sentence(50)
bottom_text = model.make_short_sentence(50)

print("top text: ", top_text)
print("bottom text: ", bottom_text)
