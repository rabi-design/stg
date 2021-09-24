from twit import twit
from time import sleep
from bs4 import BeautifulSoup

a, b = twit("https://twitter.com/tiny_motion")
senset = []

for i in range(5):

    sleep(5)
    html = a.page_source.encode('utf-8')
    bs = BeautifulSoup(html, "html.parser")
    e = bs.find("div", class_="css-1dbjc4n")
    c = e.find_all("div",
                   class_="css-901oao r-18jsvk2 r-1tl8opc r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0")
    a.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    a.implicitly_wait
    for d in c:
        if d.text not in senset:
            print(d.text)
            senset.append(d.text)

a.close()
a.quit()  # test
