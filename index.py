#!/bin/python3
import os
import random
import markovify
from PIL import Image, ImageDraw, ImageFont
import textwrap
import re
import discord
from dotenv import dotenv_values

env = dotenv_values(".env")


def create_model():
    print("generating model...")
    filename_1 = "kansas.txt"

    file_1 = open(filename_1)
    text_1 = file_1.read()

    model_1 = markovify.Text(text_1, state_size=1)

    file_2 = open("shrek.txt")
    text_2 = file_2.read()
    model_2 = markovify.Text(text_2, state_size=1)

    file_3 = open("bee_movie.txt")
    text_3 = file_3.read()
    model_3 = markovify.Text(text_3, state_size=1)

    file_4 = open("comedy.txt")
    text_4 = file_4.read()
    model_4 = markovify.Text(text_4, state_size=1)

    model = markovify.combine([model_1, model_2, model_3, model_4], [0.4, 2.3, 2.2, 3.6])
    return model


model = create_model()


def make_meme():
    top_text = model.make_short_sentence(50)
    bottom_text = model.make_short_sentence(50)

    if top_text is None:
        top_text = ""
    if bottom_text is None:
        bottom_text = ""

    print("top text: ", top_text)
    print("bottom text: ", bottom_text)
    reactions_dir = "./reactions/"
    reaction_image = random.choice(os.listdir(reactions_dir))
    print(reaction_image)

    reaction_image = Image.open(reactions_dir + reaction_image)

    draw = ImageDraw.Draw(reaction_image)
    image_width, image_height = reaction_image.size
    font = ImageFont.truetype(font="./impact.ttf", size=int(image_height/10))

    top_text = top_text.upper()
    bottom_text = bottom_text.upper()
    top_text = re.sub(r'[^\w\s]', '', top_text)
    bottom_text = re.sub(r'[^\w\s]', '', bottom_text)

    char_width, char_height = font.getsize("Y")
    chars_per_line = round(image_width / char_width)

    top_lines = textwrap.wrap(top_text, width=chars_per_line)
    bottom_lines = textwrap.wrap(bottom_text, width=chars_per_line)

    y = 10
    for line in top_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width)/2
        draw.text((x, y), line, fill="white", font=font, stroke_width=3, stroke_fill="black")
        y += line_height

    y = image_height - char_height * len(bottom_lines) - 15
    for line in bottom_lines:
        line_width, line_height = font.getsize(line)
        x = (image_width - line_width)/2
        draw.text((x, y), line, fill="white", font=font, stroke_width=3, stroke_fill="black")
        y += line_height

    print(reaction_image)
    return reaction_image


def convert_image(image):
    image_filename = "tmp_" + str(random.randint(0, 100000)) + ".jpg"
    image.save(image_filename)
    image_file = open("./" + image_filename, "rb")
    return {
      "filename": image_filename,
      "file": image_file
    }


client = discord.Client()


@client.event
async def on_ready():
    print("logged in!")


@client.event
async def on_message(message):
    # if message.user == client.user:
    #     return

    if message.content.lower().startswith("!meme"):
        meme = make_meme()
        meme = convert_image(meme)

        file = discord.File(meme["file"], filename=meme["filename"])
        await message.channel.send(file=file)
        os.remove("./" + meme["filename"])

client.run(env["TOKEN"])
