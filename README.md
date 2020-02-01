# KeyCloud
###### Create a Twitter word frequency cloud by scraping tweets

![Screenshot of main screen](/screenshot1.png)

**Note: Twitter API keys are excluded from repository for obvious security reasons.**

## Brief:
This project was created to help me learn about using APIs, data handling, and to experiment with using Python to generate a web-based UI.

Having had some exposure to building websites using static HTML/CSS/JS files, I wanted to see if I could use Python to make something come alive outside of the command-line window. This led to me learning about [Flask](https://www.palletsprojects.com/p/flask/).

## Tech:
Python | Flask | Javascript | HTML/CSS

## Guide:
- Enter a search term on the main screen, then click the big friendly button.
- The Python script will send the query to the [Twitter API](https://developer.twitter.com/en/docs) and pull the 100 most popular tweets containing the search term.
- Each of the tweets will be formatted and cleaned up, removing [stop words](https://en.wikipedia.org/wiki/Stop_words), URLs, Emojis, etc.
- The final list of words will be counted and sorted by frequency, then compiled into a Javascript dictionary.
- Using the [AnyChart](https://www.anychart.com/) package, the site will then form a word cloud.


![Screenshot formed word cloud for the term 'web design'](/screenshot2.png)

## Bugs:
- Overly-aggressive regex filters on input. Found when searching for the term 'København' (Copenhagen). Needs updated to allow additional language support.

## Todo:
- Improve data cleaning process as some Twitter usernames still get through.
- Furter testing on alternative browsers and screen dimensions.

## Credits:
- Background image by [Darius Krause](https://www.pexels.com/@dariuskrs) from [Pexels](https://www.pexels.com).
- Fonts by [Font Library](https://fontlibrary.org).