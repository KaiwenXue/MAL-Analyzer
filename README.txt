The project was completed using the Pycharm IDE and Bash for Ubuntu on Windows. You will have to install the following to run all of my scripts.

pip
metapy
nltk
beautifulsoup
requests
punkt
vader_lexicon

Overview of Functions.

Scripts:
#1 MALScraper.py

scrapeMal()
An implement of a basic web scraper and parser to create the reviews that are used in the next steps. The website XML data is extracted using the requests module in python, and the data is parsed using the BeautifulSoup package, I extracted the reviews themselves and then the text portions of the reviews only, then I generate a new file for each review.

apiMalRequest()
This function was aimed at using the MAL Api provided by the website, ultimately it was too elementary to retrieve all the data that I needed, it did not provide any reviews in the returned calls.

#2 topic_model.py
Code was taken from MP3 of CS410, please refer to documentation from the official course gitlab for this portion.

#3 nlp_analysis.py
This script lets us take the reviews that we have dowloaded and perform sentinment analysis using the vader package. Files are read in and tokenized by sentence, then each sentence is read independely and analyzed using the polarity_score function. 

To run the program in its entirety, please execute the following order in the given directory.

1. Run the MALScraper.py script
2. Run the topic_model.py script
3. Run the nlp_analysis.py script 