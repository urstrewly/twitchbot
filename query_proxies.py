#!/usr/bin/python
# -*- coding: ascii -*-


'''
            TO DO LIST 


    2. Make proxies connect to url and remain connected
    3. Finish UI (optionally)

'''

import requests
from bs4     import BeautifulSoup
import random
import time


class Bot():
    proxy_list     = ["http://www.httptunnel.ge/ProxyListForFree.aspx"] # proxy site
    fname          = "proxies/proxies.txt" # file name to save proxies
    custom_proxies = "proxies/userscustom/myproxies.txt" # users custom proxies go here
    mydivs         = 0  #  gay shit
    url            = 0  #  url for stream
    arr            = [] # had to do more gay array shit
    http_proxy     = []
    headers        = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
    
    # start.. main function program start is here
    def main(self):  
        while not self.url:

            self.url = raw_input("url -> ")   

        self.start(False)
    # end.. main function program start is here




    # start.. start function. 
    def start(self, ownFile):
        print("starting proxy scan..")

        # -- start.. User chose to use their own proxy list
        if ownFile == True:
            print("Chose option to connect with your own proxies..")
            try:
                with open(self.custom_proxies, 'r') as f:
                    
                    self.arr.append(f.read())
                    
                self.BeginQueue()
                
            except:
                print("Error")
        # -- end.. User chose to use their own proxy list



        

        # -- start.. User chose to use their ezviews proxy list
        else:
            print("Chose option to connect with ezviews proxies..")
            r = requests.get(self.proxy_list[0])

            if (r.status_code == 200):

                html_page = r.text
                soup   = BeautifulSoup(html_page, 'html.parser')            
                mydivs = soup.findAll("a", {"target": "_new"})


                for i in range(len(mydivs)):
                    
                    proxy = mydivs[i]
                    self.arr.append(str(proxy.text))
                      
              
                self.write_to_file(self.arr)
                print(self.arr[1])
                print(len(self.arr))
                self.BeginQueue()
                           
            else:
                print("server down trying custom_proxies.txt..")
                try:
                    with open(self.custom_proxies, 'r') as f:
                    
                        print(f.read())
                    
                except:
                    print("Error")
        # -- end.. User chose to use their ezviews proxy list
    # end.. start function.     



    # -- Start.. Write proxy from internet to file
    def write_to_file(self,ipport):

        try:
            with open(self.fname, 'a+') as f:
                for i in range(len(ipport)):          
                    f.write(ipport[i] + "\n")

        except:
            print("Error")
    # -- end.. Write proxy from internet to file



    # -- Start.. Where proxies connect to url 
    def BeginQueue(self):
        good = 0
        bad = 0
        for i in range(len(self.arr)): 
            self.http_proxy.append("https://" + self.arr[i])
         
            proxies = {
                    "https": self.http_proxy[i]
            }
            
            #2. Make requests with proxies
            
            
            try:
               
                r = requests.get(self.url, headers=self.headers, proxies=proxies)

                if r.status_code == 200:
                    
                    good += 1
            except:
                
                bad += 1

            print("Total of connected: " + str(good) + " : Total Bad of proxies: " + str(bad))
    # -- End.. Where proxies connect to url

    
James = Bot()

James.main()
