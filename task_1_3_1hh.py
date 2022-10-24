# import requests as req
from attr import attrs
from bs4 import BeautifulSoup
import json
import tqdm
import time
from requests_tor import RequestsTor

req = RequestsTor()


data = {
    "data":[]
}

for page in range (1,10):
    url = f"https://hh.ru/search/vacancy?text=python+%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA&from=suggest_post&salary=&clusters=true&ored_clusters=true&enable_snippets=true&page={page}&hhtmFrom=vacancy_search_list"
        
    resp=req.get(url)

    soup = BeautifulSoup(resp.text, "lxml")
    tags = soup.find_all(attrs={"data-qa":"serp-item__title"})
    
    for iter in tqdm.tqdm(tags):
        time.sleep(2)
        
        url_o = iter.attrs["href"]
        if url_o:
            resp_o = req.get(url_o)            

            soup_o = BeautifulSoup(resp_o.text, "lxml")
            tag_pay = soup_o.find(attrs = {"data-qa":"vacancy-salary"}).text
            # tag_reg = soup_o.find(attrs = {"data-qa":"vacancy-view-link-location"}).text

            if soup_o.find(attrs = {"data-qa":"vacancy-view-link-location"}):
                tag_reg = soup_o.find(attrs = {"data-qa":"vacancy-view-link-location"}).text
            elif soup_o.find(attrs = {"data-qa":"vacancy-view-raw-address"}):
                tag_reg = soup_o.find(attrs = {"data-qa":"vacancy-view-raw-address"}).text
            else:  
                tag_reg = ""  

            tag_exp = soup_o.find(attrs = {"data-qa":"vacancy-experience"}).text
            
            data["data"].append({"title":iter.text, "work experience":tag_exp, "salary":tag_pay, "region":tag_reg })

            with open("data.json", "w") as file:
                json.dump(data, file, ensure_ascii = True)
    

    