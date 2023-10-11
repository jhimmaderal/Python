from bs4 import BeautifulSoup as bs
from requests_html import HTMLSession
import time

def getPage():
  s = HTMLSession()
  url = input(str("Input Talabat URL: ")).lower()
  folder = input(str("Input Company Name: ")).lower()
  category = input(str("Input Category: ")).lower()
  counter = ""
  
  print(f'Collecting Data in {folder.title} Category {category.title}....')
  #url = "https://www.talabat.com/qatar/grocery/679767/al-meera-old-airport/cooking-baking/flour?aid=1672&page={}"
  base_url = url.format(counter)
  r = s.get(base_url.format(counter))
  soup = bs(r.text, 'html.parser')
  test = soup.find('div', class_ = 'sc-f7c070e3-0 jTAyJk')
  
  if test == None: # not paginated
    r3 = s.get(url)
    soup = bs(r3.text, 'html.parser')
    cards = soup.find_all('div', class_ = "col-8 col-sm-4")
    for card in cards:
      with open(f'talabat/{folder}/{category}.txt', 'a+') as f:
        content = card.find('div', class_ = "content mt-2")
        prodName = content.find('div', class_ = 'f-14 mb-2 truncate-grocery-item').text
        prodPrice = content.find('span', class_ = 'currency f-16 f-500').text
        f.write(f"{prodName} ^ {prodPrice} \n")   
    print("Done !")
    
  else: # paginated
    pages = soup.find('ul', class_= 'paginate-wrap')
    for page in pages:
        pageNumber = page.text.strip()
        countPage = pageNumber
        if countPage != "":
          PageCounter = countPage
          newUrl =  (url + f"&page={PageCounter}")
          r2 = s.get(newUrl)
          soup = bs(r2.text, 'html.parser')
          cards = soup.find_all('div', class_ = "col-8 col-sm-4")
          for card in cards:
            with open(f'talabat/{folder}/{category}.txt', 'a+') as f:
              content = card.find('div', class_ = "content mt-2")
              prodName = content.find('div', class_ = 'f-14 mb-2 truncate-grocery-item').text
              prodPrice = content.find('span', class_ = 'currency f-16 f-500').text
              f.write(f"{prodName} ^ {prodPrice} \n")
    print("Done !")
  
  createNew = input('Do you want to create new file ? Y/N: ').lower()
  if createNew == 'y':
    getPage()
  else:
    print('Til next time !')
    exit()     
    
getPage()

