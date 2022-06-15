## Library Generator for Telegram API
I was thinking about writing my own Python librarty for Telegram bot API. 
Looking through [Telegram bot API documentation website](https://core.telegram.org/bots/api) I've noticed it has very tidy and readable html code. 
So instead of manually writing code for every described function and object I've decided to try and parse it. That's how this project was born.


This program parses through documentation's html, generates code for a programming language using templates and Writer objects, writes that code to a file 
and automatically formats/beautyfies it. It does **not** create a full working library, but rather a library "skeleton" with all boring repetitive tasks taken care of. 


It currently only generates python code, but by adding new template files and your own custom Writer objects to the hierarchy you can make it write code 
for any other programming language.


### Requirements:
`pip install beautifulsoup4`

`pip install requests`

`pip install black`


### LOC Generated
Python: ~6000 lines

Example:

![example](https://user-images.githubusercontent.com/98107123/173823838-44f3f275-0f30-450d-8727-95362d836bdc.jpg)
