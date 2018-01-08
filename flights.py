# import libraries
import csv
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import datetime, timedelta
reload(sys)
sys.setdefaultencoding('utf-8')

# Web driver
browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('http://uk.flightaware.com/live/findflight?origin=VABB&destination=VIDP')

# Parse html
soup = BeautifulSoup(browser.page_source, "html.parser")

# Get airline name
airLine = [] 
for td in soup.find_all('td', {'class': 'ffinder-results-airline'}):
	airLine.append(td.text.strip())

# Get aircraft model number
airCraft = []
for td in soup.find_all('td', {'class': 'ffinder-results-aircraft'}):
	airCraft.append(td.text.strip())

# Get Departure time
departure =[]
for td in soup.find_all('div', {'class': 'ffinder-results-schedule-departure'}):
	departure.append(td.text.strip()[4:9])

# Get Arrival time
arrival = []
for td in soup.find_all('div', {'class': 'ffinder-results-schedule-arrival'}):
	arrival.append(td.text.strip()[:5])

# Difference between arrival and depature time
block = []
actual = []
diff = []
for d, a in zip(departure, arrival):
	t1 = datetime.strptime(a, '%H:%M')
	t2 = datetime.strptime(d, '%H:%M')
	td = t1 - t2
	td.total_seconds()
	if td.total_seconds() >= 0:
		bt = td
		block.append(str(td))
		td = td - timedelta(seconds=1800)
		actual.append(str(td))
		dt = bt - td
		diff.append(str(dt))

final = zip(airLine, airCraft, departure, arrival, block, actual, diff)

# Export as csv
with open("flights.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(['Airline', 'Aircraft', 'Departure', 'Arrival', 'Block Time', 'Actual Flying Time', 'Difference'])
    for row in final:
        writer.writerow(row)