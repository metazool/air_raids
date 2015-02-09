from bs4 import BeautifulSoup
import json
import urllib2

baseurl = 'http://www.aberdeencity.gov.uk/education_learning/local_history/archives/loc_onlineexhibitionschoollifeairraids'
out = []
copyright = "\u00a9 Aberdeen City and Aberdeenshire Archives"


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
    if m.has_attr('name') is False: continue
    if 'width' in m['content']: continue
    if m['name'] == 'GENERATOR': continue

    meta = {}
    meta[m['name']] = m['content']
    metatags.append(meta)

  return metatags

def extract_logbook_images(soup):
  """Handily all the relevant files are 'LOGBOOK'"""
  entries = []
  
  for para in soup.find_all('td'):
    entry = {}
    i = para.find('img')
    if i is None: continue
    if 'LOGBOOK' not in i['src']: continue

    school = para.h2
    lines = para.find_all('p')

    entry['image'] = i['src']
    entry['text'] = "\n".join([l.text for l in lines])
    # this didn't work?
    entry['text'].replace("\n\n",'')
    entry['copyright'] = copyright
    entries.append(entry)

  return entries

urls = pagelist()  
items = []
for p in urls:
  page = geturl(p)
  soup = BeautifulSoup(page)   
  meta = extract_dc_metadata(soup)
  imgs = extract_logbook_images(soup)
  for i in imgs: 
    items.append(i)

print json.dumps(items)
  
   
