# web-scraping
Python script to scrape the flights originating from mumbai to delhi airport.
This scrapes the information such as,
- Airline name
- Aircraft type
- Departure time
- Arrival time.

The above mentioned data yield us the,
- Block time (Time includes taxiing time and actual flying time)
- Actual flying time and the
- Difference between block time and actual flying time.

Running the script will export the above mentioned details as csv.

# Requirements
- Python 2.7
- BeautifulSoup Library
- Selenium Library

# Installation
- Clone the repo: `git clone https://github.com/NaveenShanmugavel18/web-scraping.git`
- Install the dependancies mentioned in Requirements section (above)
- Run the script in command line
- On successful completion, you will find the csv exported with data in it.

Note: Make sure you place the chrome driver in the specified path.
