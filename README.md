# Aiogram Boilerplate

## Before start

### *NOTE*: This template uses **PACKAGE** running approach, and you should locate the Bot into another/parent directory and than run the package command using the venv you prefer
#### * Main idea is to run the project from outside

## Get started

### So, go ahead and create new folder and clone the project after cd into that folder

### Clone the project
~~~bash
git clone https://github.com/mumrbekkk/Aiogram-Boilerplate.git
~~~


### Create <u>.env</u> file
*windows*
~~~bash
echo > .env
~~~

### Add TG_BOT_TOKEN
~~~bash
TG_BOT_TOKEN=your_bot_token
~~~

### Install dependencies
~~~bash
pip install -r requerements.txt
~~~

### *!!! IMPORTANT !!!* 
### Running is a bit complex in python as it uses *packages*

#### NOTE: if you are outside the bot directory, you should clone the bot from the directory and in the parent directory you should use virtual env
#### And then run the following packege command
~~~bash
py -m Bot.main
~~~



