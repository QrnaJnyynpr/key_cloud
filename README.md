# KeyCloud
###### Create a Twitter word frequency cloud by scraping tweets
**Unfinished Project** - Will be made into a Flask website where the user can manually enter the keyword string, and have the word cloud automatically generated in the DOM.

**Note: Twitter API keys are excluded from upload for obvious security reasons.**

![Screenshot of word cloud for search term 'programmer'](/screenshot.png)

## Instructions for current format:
- Run the *main.py* script and enter a keyword string.
- The script will call the [Twitter API](https://developer.twitter.com/en/docs) and search for tweets containing the string, then compile a list of whichever words appear most frequently alongside it.
- The data is exported to *data.txt* as a Javascript dictionary.
- Paste the contents of *data.txt* into the marked section in *script.js*.
- Using the [AnyChart](https://www.anychart.com/) package, the Javascript file will form a word cloud.
- View the word cloud by opening *index.html*

## TODO:
- Flask build. Single page operation with no user tinkering to get it to work.
- Improve data cleaning process as some Twitter usernames still get through.
- Expand stop-word list.
- Fix all the bugs that implementing this list will inevitably create.