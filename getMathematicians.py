from bs4 import BeautifulSoup
from mathematicians import simple_get



def get_names():
  
  # Downloads the page where the list of mathemticians is found 
  # and returns a list of strings, one per mathematician
  
  url = 'http://www.fabpedigree.com/james/mathmen.htm'
  response = simple_get(url)
 

  if response is not None:
    html = BeautifulSoup(response, 'html.parser')
    names = set()
    for li in html.select('li'):
      for name in li.text.split('\n'):
        if len(name) > 0:
          names.add(name.strip())
    return list(names)

  # raise an exception if we failed to get any data from the url

  raise Exception('Error retrieving contents at {}'.format(url))

def get_hits_on_name(name):
  
  """
  Accepts a 'name' of a mathematician and returns the number
  of hits that mathematician's Wikipedia page recieved in the last 
  60 days, as an 'int'
  """
  
