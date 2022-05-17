import random 
import string
 
 
def create_shortURL(link):
    chars =string.ascii_lowercase+string.ascii_uppercase+string.digits
    # chars = ['a','c','z']
    short_url = ''.join(random.choice(chars) for i in range(4))
    d={}
    URL = 'https://www.youtube.com/'+short_url
    d[URL] = link
    print("Your URL:",d[URL])
    print("Shorten URL:",URL)
  
         
create_shortURL('https://www.you.com/watch?v=rvPamIeNwUI')