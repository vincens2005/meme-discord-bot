# Meme generator discord bot

## add it to your server [here](https://discord.com/oauth2/authorize?client_id=857661821552295946&scope=bot&permissions=67648)

## customizing


you can add more reactions by putting images in the `reactions/` directory

you can train your markov chain on whatever text you want. the default filename for this text is `kansas.txt` and you can put whatever here.

For more advanced customization, you need to change to way the model is generated
this can be done by changing the function `create_model` in `index.py`. more info can be found at the [markovify docs](https://pypi.org/project/markovify/)


## running the bot yourself

1. run `setup.py` (preferably with root privlieges (but only if you wanna))

2. make a .env file with your bot token in it
    `TOKEN=my_bot_token`

3. run `index.py`
