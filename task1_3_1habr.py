# import requests as req
from tokenize import Ignore, String
from turtle import write
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

for page in range (39,50):
    time.sleep(3)
    # url = f"https://career.habr.com/vacancies?page={page}&q=python&type=all"  
    # url = f"https://career.habr.com/vacancies?page={page}&q=%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA%20python&sort=salary_asc&type=all"
    # url = f"https://career.habr.com/vacancies?page={page}&q=python&sort=salary_desc&type=all"
    url = f"https://career.habr.com/vacancies?page={page}&q=%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA%20python&type=all"
    
    resp=req.get(url)

    # print (resp.text)
    soup = BeautifulSoup(resp.text, "lxml")
    tagss = soup.find_all("div", attrs={"class":"vacancy-card__info"})

    for iter in tqdm.tqdm(tagss):
        try:    

            if (iter.find(attrs={"class":"vacancy-card__title-link"}) ):
             tag_title = iter.find(attrs={"class":"vacancy-card__title-link"})                 
            
            if (iter.find(attrs = {"class":"vacancy-card__meta"})) :   
                tag_reg = iter.find(attrs = {"class":"vacancy-card__meta"}) #.find_next(attrs = {"class":"link-comp link-comp--appearance-dark"}) 
           
            if (iter.find(attrs = {"class":"vacancy-card__salary"}).find_next(attrs = {"class":"basic-salary"})):
                tag_pay = iter.find(attrs = {"class":"vacancy-card__salary"}).find_next(attrs = {"class":"basic-salary"})
            
            # tag_pay = iter.find(attrs = {"class":"basic-salary"})       
            if (iter.find(attrs = {"class":"vacancy-card__skills"}).find_next(attrs = {"class":"link-comp link-comp--appearance-dark"}).find_next(attrs = {"class":"link-comp link-comp--appearance-dark"})):
                tag_exp = iter.find(attrs = {"class":"vacancy-card__skills"}).find_next(attrs = {"class":"link-comp link-comp--appearance-dark"}).find_next(attrs = {"class":"link-comp link-comp--appearance-dark"})           
     
        except:
            tag_title.text = ""
            tag_pay.text = ""
            tag_reg.text = ""
            tag_exp.text = ""

        # print('tag_title',tag_title.text)
        # print('tag_pay', tag_pay.text)
        # print('tag_reg', tag_reg.text)
        # print('tag_exp', tag_exp.text)
        finally:          

            data["data"].append({"title":tag_title.text, "work experience":tag_exp.text, "salary":tag_pay.text, "region":tag_reg.text })

            with open("data.json", "w", errors='ignore') as file:
                json.dump(data, file, ensure_ascii = False )
