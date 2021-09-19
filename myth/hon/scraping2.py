#~/.local/bin/pip
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import list_other
import datetime
from tqdm import tqdm
from os.path import join
import pandas as pd
class scrape1():
    def main(self):
        dt_now = datetime.datetime.now()
        year=str(dt_now.year)[-2:]
        if len(str(dt_now.month))==1:
            month="0"+str(dt_now.month)
        else:
            month=str(dt_now.month)
        if len(str(dt_now.day))==1:
            day="0"+str(dt_now.day)
        else:
            day=str(dt_now.day)
        global today
        today=year+month+day
        try:
            os.mkdir("output_{0}".format(today))
        except:
            pass
        global list3
        list3=[]
        # global book2
        # book2=openpyxl.Workbook()
        # global sheet2
        # sheet2=book2.active
        # sheet2.cell(1,3).value="num"
        # sheet2.cell(1,2).value="URL"
        # sheet2.cell(1,3).value="Title"
        # sheet2.cell(1,4).value="Meta Description"
        # sheet2.cell(1,5).value="Meta Keywords"
        # sheet2.cell(1,6).value="source_URL"
        # sheet2.cell(1,7).value="Time"
        global l
        l=2
        global list2
        list2=self.lis()
        global list_u
        list_u={}
        print("https://responsive-jp.com/")
        self.all_web1("https://responsive-jp.com/")
        print("https://www.webdesignclip.com/")
        self.all_web2("https://www.webdesignclip.com/")
        print("https://sp.webdesignclip.com/")
        self.all_web3("https://sp.webdesignclip.com/")
        print("https://lp.webdesignclip.com/")
        self.all_web4("https://lp.webdesignclip.com/")
        print("https://bm.s5-style.com/")
        self.all_web5("https://bm.s5-style.com/")
        print("https://gendaidesign.com/")
        self.all_web6("https://gendaidesign.com/")
        print("https://muuuuu.org/")
        self.all_web7("https://muuuuu.org/") 
        df =\
        df=pd.DataFrame([["num","URL","Title","Meta Description","Meta Keywords","source_URL","Time"]])
        df.to_csv(join("output_"+today,'new_info.csv'), header=False, index=False, encoding='utf_8_sig')
        for one_u in list_u.keys():
            self.webs(one_u)
        # r2=2
        # while True:
        #     if sheet1.cell(r2,2).value==None:
        #         for list2_o in list3:
        #             sheet1.cell(r2,2).value=list2_o
        #             r2+=1
        #         break
        #     r2+=1
        # book2.save(os.path.join("output","new_info.xlsx"))
        
        # with open(os.path.join("output","new_info.csv"), 'w', newline="") as csvfile:
        #     writer = csv.writer(csvfile)
        #     for row in sheet2.rows:
        #         try:
        #             writer.writerow( [cell.value for cell in row] )
        #         except:
        #             pass
        with open('list_other.py', 'w') as f:
            f.write("urls=[\n")
            for d in list2:
                f.write("'%s',\n" % d)
            f.write("]")
    def lis(self):
        # files=glob.glob("重複チェックファイル.xlsx")
        # global book1
        # for file in files:
        #     book1=openpyxl.load_workbook(file)
        #     global sheet1
        #     sheet1=book1['シート1']
        
        list1=list_other.urls
        
        # while True:
        #     list1.append(sheet1.cell(ro,2).value)
        #     ro+=1
        #     if sheet1.cell(ro,2).value==None:
        #         if sheet1.cell(ro+1,2).value==None:
        #             if sheet1.cell(ro+2,2).value==None:
        #                 break
        return list1
        
        
    def all_web1(self,url):
        global mo_url
        mo_url=url
        list_u2=[]
        bar = tqdm(total = 1000)
        while True:
            try:
                req=requests.get(url,timeout=10)
                bs=BeautifulSoup(req.text, 'html.parser')
                list_u2.append(url)
                bar.update(1)
                url_next=bs.find("a",class_="next page-numbers").get("href")
            except:
                pass
            if url!=url_next:
                url=url_next
            else:
                bar.close()
                bar = tqdm(total = len(list_u2))
                break
        for ur in list_u2:
            self.m_web1(ur)
            bar.update(1)
        bar.close()
    def m_web1(self,url1):
        req=requests.get(url1,timeout=10)
        bs=BeautifulSoup(req.text, 'html.parser')
        url_all=bs.find_all("section",class_="indexSection")
        for url_in in url_all:
            try:
                if url_in.div.h2.a.get("href") not in list2:
                    list_u[url_in.div.h2.a.get("href")]=mo_url
            except:
                pass
    
    def all_web2(self,url):
        global mo_url
        mo_url=url
        list_u2=[]
        bar = tqdm(total = 1000)
        while True:
            try:
                req=requests.get(url,timeout=10)
                bs=BeautifulSoup(req.text, 'html.parser')
                list_u2.append(url)
                bar.update(1)
                url_next=bs.find("a",class_="nextpostslink").get("href")
            except:
                pass
            if url!=url_next:
                url=url_next
            else:
                bar.close()
                bar = tqdm(total = len(list_u2))
                break
        for ur in list_u2:
            self.m_web2(ur)
            bar.update(1)
        bar.close()
    def m_web2(self,url1):
        req=requests.get(url1,timeout=10)
        bs=BeautifulSoup(req.text, 'html.parser')
        url_all=bs.find_all("p",class_="post_inner--launch")
        for url_in in url_all:
            try:
                if url_in.a.get("href") not in list2:
                    list_u[url_in.a.get("href")]=mo_url
            except:
                pass
    
    def all_web3(self,url):
        global mo_url
        mo_url=url
        list_u2=[]
        bar = tqdm(total = 1000)
        while True:
            try:
                req=requests.get(url,timeout=10)
                bs=BeautifulSoup(req.text, 'html.parser')
                list_u2.append(url)
                bar.update(1)
                url_next=bs.find("a",class_="nextpostslink").get("href")
            except:
                pass
            if url!=url_next:
                url=url_next
            else:
                bar.close()
                bar = tqdm(total = len(list_u2))
                break
        for ur in list_u2:
            self.m_web3(ur)
            bar.update(1)
        bar.close()
    def m_web3(self,url1):
        req=requests.get(url1,timeout=10)
        bs=BeautifulSoup(req.text, 'html.parser')
        url_all=bs.find_all("p",class_="post_ls_inner--launch")
        for url_in in url_all:
            try:
                if url_in.a.get("href") not in list2:
                    list_u[url_in.a.get("href")]=mo_url
            except:
                pass
            
    def all_web4(self,url):
        global mo_url
        mo_url=url
        list_u2=[]
        bar = tqdm(total = 1000)
        while True:
            try:
                req=requests.get(url,timeout=10)
                bs=BeautifulSoup(req.text, 'html.parser')
                list_u2.append(url)
                bar.update(1)
                url_next=bs.find("a",class_="nextpostslink").get("href")
            except:
                pass
            if url!=url_next:
                url=url_next
            else:
                bar.close()
                bar = tqdm(total = len(list_u2))
                break
        for ur in list_u2:
            self.m_web4(ur)
            bar.update(1)
        bar.close()

    def m_web4(self,url1):
        req=requests.get(url1,timeout=10)
        bs=BeautifulSoup(req.text, 'html.parser')
        url_all=bs.find_all("p",class_="post_ls_inner--launch")
        for url_in in url_all:
            try:
                if url_in.a.get("href") not in list2:
                    list_u[url_in.a.get("href")]=mo_url
            except:
                pass
    
    def all_web5(self,url1):
        m=1
        global mo_url
        mo_url=url1
        bar = tqdm(total = 1000)
        while True:
            
            try:
                req=requests.get(url1+"/page/"+"{0}".format(m),timeout=10)
                print(url1+"/page/"+"{0}".format(m))
                bs=BeautifulSoup(req.text, 'html.parser')
                
                if bs.find("h2",class_="error404 en"):
                    bar.close()
                    break
                url_all=bs.find_all("div",class_="img")
                for url_in in url_all:
                    try:
                        if url_in.a.get("href") not in list2:
                            list_u[url_in.a.get("href")]=mo_url
                    except:
                        bar.close()
                        break
                m+=1
                bar.update(1)
            except:
                bar.close()
                break
            
            
    
    def all_web6(self,url):
        global mo_url
        mo_url=url
        list_u2=[]
        bar = tqdm(total = 1000)
        while True:
            try:
                req=requests.get(url,timeout=10)
                bs=BeautifulSoup(req.text, 'html.parser')
                list_u2.append(url)
                bar.update(1)
                url_next=bs.find("li",class_="current").next_sibling.a.get("href")
            except:
                pass
            
            if url!=url_next:
                url=url_next
            else:
                bar.close()
                bar = tqdm(total = len(list_u2))
                break
        for ur in list_u2:
            self.m_web6(ur)
            bar.update(1)
        bar.close()
            
    def m_web6(self,url1):
        req=requests.get(url1,timeout=10)
        bs=BeautifulSoup(req.text, 'html.parser')
        url_all=bs.find_all("figure",class_="front")
        for url_in in url_all:
            try:
                if url_in.a.get("href") not in list2:
                    list_u[url_in.a.get("href")]=mo_url
            except:
                pass
    
    
    def all_web7(self,url1):
        n=1
        m=1
        global mo_url
        mo_url=url1
        bar = tqdm(total = 1000)
        while True:
            try:
                req=requests.get(url1+"/page/"+"{0}".format(m),timeout=10)
                bs=BeautifulSoup(req.text, 'html.parser')
                
                try:
                    if bs.find("div",class_="about").p.text=="ページが見つかりません。":
                        break
                except:
                    pass
                url_all=bs.find_all("li",class_="item")
                for url_in in url_all:
                    try:
                        if url_in.figure.a.get("href") not in list2:
                            list_u[url_in.figure.a.get("href")]=mo_url
                        n+=1
                    except:
                        break
                m+=1
                bar.update(1)
            except:
                bar.close()
                break
        
    def webs(self,url2):
        print(url2)
        global l
        # sheet2.cell(l,1).value=l
        # sheet2.cell(l,2).value=url2
        try:
            req=requests.get(url2,timeout=10)
            bs=BeautifulSoup(req.text, 'html.parser')
            title=""
            meta_description=""
            meta_keywords=""
            try:
                title=bs.find("title").text
                #sheet2.cell(l,3).value=title
            except:
                title=""
                pass
            try:
                meta_description=bs.find("meta",{"name":"description"})["content"]
                #sheet2.cell(l,4).value=meta_description
            except:
                meta_description=""
                pass
            try:
                meta_keywords=bs.find("meta",{"name":"keywords"})["content"]
                #sheet2.cell(l,5).value=meta_keywords
            except:
                meta_keywords=""
                pass
            try:
                p_url=list_u.get(url2)
                print(p_url)
                #sheet2.cell(l,6).value=p_url
            except:
                p_url=""
                pass
            try:
                d=datetime.datetime.now()
                txt1=d.strftime("%Y-%m-%d %H:%M:")
                txt2=d.strftime("%S")[:2]
                txt=txt1+txt2
                print(txt)
                #sheet2.cell(l,7).value=txt1+txt2
            except:
                txt=""
                pass
            df_add = pd.DataFrame([[l-1,url2,title,meta_description,meta_keywords,p_url,txt]])
            df_add.to_csv(join("output_"+today,'new_info.csv'), mode='a', header=False, index=False, encoding='utf_8_sig')

            # subprocess.run("/usr/local/bin/php write.php {0} {1} {2} {3} {4} {5} {6}".format(l,url2,title,meta_description,meta_keywords,p_url,txt),
            #                shell=True)
        except:
            l-1
        list2.append(url2)
        list3.append(url2)
        l+=1


if __name__=="__main__":
    scrape=scrape1()
    scrape.main()
