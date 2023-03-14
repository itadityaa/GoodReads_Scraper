# GoodReads_Scraper

Looking for a good book to read this summer but don't know where to start? We've got you covered! Say goodbye to the tedious task of searching for the perfect book and let us do the work for you. Our project involves web-scraping the popular [Goodreads Listopia](https://www.goodreads.com/list) page to bring you the top book recommendations for the season. So sit back, relax, and let's take a journey through the world of literature together!

## About the website:

If you're a book lover looking for a dynamic online community to connect with, then Goodreads.com is the perfect platform for you! With its unique features and vibrant user base, Goodreads has quickly become a leading destination for readers around the world. Whether you're looking to discover new books, track your reading progress, or engage in lively discussions with fellow book enthusiasts, Goodreads has it all. What's more, the site's user-generated content, including reviews, book clubs, and personalized recommendations, ensures that you'll always find something new and exciting to read.

## Requirements:

- [Python](https://www.python.org/downloads/)
- [Optional: Git](https://git-scm.com/downloads)

## Installation:

1. Clone the [repository](https://github.com/itadityaa/GoodReads_Scraper) or download the [source code](https://github.com/itadityaa/GoodReads_Scraper/blob/main/Quick_Scraper.py).
2. Navigate to the project directory in your terminal/command peompt.
3. Create and activate a virtual environment (optional):
   ```
   virtualenv venv
   source venv/bin/activate # for Linux/Mac
   venv\Scripts\activate.bat # for Windows
   ```
4. Install the required packages using pip:
   ```
   pip install -r requirements.txt
   ```
   That is all you need to run the code.

## Usage:

1. Go to [Goodreads Listopia](https://www.goodreads.com/list).
2. Select the list of your choice and copy its URL.
3. Open terminal/command prompt and navigate to the project directory.
4. Run the scraper with the following command:

   ```
   python Quick_Scraper.py <list-url>
   ```

   Replace `<list-url>` with the URL of the list you copied earlier.

5. The program will scape the first page of the list by default and print the results to the console.

## Optional argument(s):

- `-p/--pages`: The number of pages to scrape (default: 1).
  Example command to scrape first five pages of a list:
  ```
  python Quick_Scraper.py <list-url> -p 3
  ```
- `-o/--output`: Where to get the output (default: console).
  Example command to save it to a csv file:
  ```
  python Quick_Scraper.py <list-url> -o csv
  ```
  Note: This will save the whole unordered dataFrame to a csv file (for analysis purpose).
