# Import Libraries
import urllib.request
from bs4 import BeautifulSoup

# Specify the url
Parcel1 = 'http://eringcapture.jccal.org/caportal/CA_PropertyTaxParcelInfo.aspx?ParcelNo=22%2000%2029%203%20029%20015.001%20%20%20%20%20%20%20%20%20%20%20%20'

# query the website and return the html to the variable 'page'
page = urllib.request.urlopen(Parcel1)

# parse the html using beautiful soup and store in variable 'soup'
soup = BeautifulSoup(page, 'html.parser')

#Take out the <tbody> of parcel and get its value
parcel_box = soup.find('b')

# strip() is used to remove starting and trailing
parcel_num = parcel_box.text.strip()
print(parcel_num)

