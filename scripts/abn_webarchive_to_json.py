from bs4 import BeautifulSoup
import simplejson
import urllib2

baseurl = 'http://www.aberdeencity.gov.uk/education_learning/local_history/archives/loc_onlineexhibitionschoollifeairraids'
out = []

def pagelist():
  """List the six pages of air raid logbooks"""
  pages = []
  for suffix in ['',1,2,3,4,5]:
    pages.append(baseurl+str(suffix)+'.asp')
  return pages

def geturl(url):
  return urllib2.urlopen(url).read()

def extract_dc_metadata(soup):
  """Lift and list the relevant Dublin Core meta tags"""
  metatags = [] 

  for m in soup.find_all('meta'):
    
    # Skip over fields we don't like explicitly
    if m.has_key('name') is False: continue
    if 'width' in m['content']: continue
    if m['name'] == 'GENERATOR': continue

    meta = {}
    meta[m['name']] = m['content']
    metatags.append(meta)

  return metatags

def extract_logbook_images(soup):
  """Handily all the relevant files are 'LOGBOOK'"""
  images = []
  
  for i in soup.find_all('img'):
    if 'LOGBOOK' not in i['src']: continue
    print i['src']

urls = pagelist()  
for p in urls:
  print p
  page = geturl(p)
  soup = BeautifulSoup(page)   
  meta = extract_dc_metadata(soup)
  print meta
  imgs = extract_logbook_images(soup)
   
