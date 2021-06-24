#!/bin/python3
import os
import random
import markovify
from PIL import Image, ImageDraw, ImageFont
import textwrap


filename = "kansas.txt"

file = open(filename)
text = file.read()

model = markovify.Text(text, state_size=1)


def make_meme():
    top_text = model.make_short_sentence(50)
    bottom_text = model.make_short_sentence(50)
    print("top text: ", top_text)
    print("bottom text: ", bottom_text)
    reactions_dir = "./reactions/"
    reaction_image = random.choice(os.listdir(reactions_dir))
    print(reaction_image)

    reaction_image = Image.open(reactions_dir + reaction_image)

    draw = ImageDraw.Draw(reaction_image)
    image_width, image_height = reaction_image.size
    font = ImageFont.truetype(font="./impact.ttf", size=int(image_height/8))

    # top_text = top_text.upper()
    # bottom_text = bottom_text.upper()

    char_width, char_height = font.getsize("A")
    chars_per_line = round(image_width / char_width)
    
    top_lines = textwrap.wrap(top_text, width=chars_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)

    y = 10
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width)/2
        draw.text((x, y), line, fill='white', font=font)
        y += line_height
        
    y = image_height - char_height * len(bottom_lines) - 15
    for line in bottom_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width)/2
        draw.text((x, y), line, fill='white', font=font)
        y += line_height
        
    reaction_image.save("meme.jpg")

make_meme()
