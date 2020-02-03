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
  
  # using the xtools api, use an enpoint to grab statistics of a page
  """ 
  This gives the base url for gathering statistics from wikipedia, it's still missing a piece at the end however.
  Need to format it so that it'll take the data from the previous get names function and adds that to the end 
  of this api endpoint to automatically go through and scrape the wikipedia names for statistics of each the scientists.
  """
  url = 'https://xtools.wmflabs.org/api/page/prose/en.wikipedia.org/'
  
  # This is where we will format to automatically insert the names at the end of the api endpoint
  response = simple_get(url_root.format(name))
  
  if response is not None:
    html = BeautifulSoup(response, 'html.parser')
    
    hit_link = [a for a in html.select('a')
                if a ['href'].find('latest-60') > -1]
    
    if len(hit_link) > 0:
      # stip commas
      link_text = hit_link[0].text.replace(',','')
      try:
        # Convert to integer
        return int(link_text)
      except:
        log_error("couldn't parse{} as an `int `".format(link_text))
        
  log_error('No pageviews found for{}'.format(name))
  return None

if __name__ == '__main__':
  print('Getting the list of names.....')
  names = get_names()
  print('...done.\n')
  
  results = []
  
  print('Getting stats for each name .....')
  
  for name in names:
    try:
      hits = get_hits_on_name(name)
      if hits is None:
        hits = -1
      results.append((-1, name))
      log_error('error encountered while processing'
                '{}, skipping'.format(name))
  
  print('....done.\n')
  
  results.sort()
  results.reverse()
  
  
  if len(results) > 5:
    top_marks = results[:5]
  else:
    top_marks = results
    
  print('\nThe most popular mathematicians are: \n')
  for (mark, mathematician) in top_marks:
    print('{} with {} pageviews'.format(mathematician, mark))
    
  no_results = len([res for res in results if res[0] == -1])
  print ('\nBut we did not find results for ' 
         '{} mathematicians on the list'.format(no_results))
      