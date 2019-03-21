#!/usr/bin/python
# -*- coding: ascii -*-


'''
            TO DO LIST 


    1. Start timer so proxies can have a queue
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
    headers        = {'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36'}
    
    # start.. main function program start is here
    def main(self):  
        while not self.url:

            self.url = raw_input("url -> ")   

        self.start(True)
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
                    
                self.BeginQueue(False)
                
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
                    self.arr.append(i)  
                    self.arr[i] = str(proxy.text)
                      
              
                self.write_to_file(self.arr)
                print(self.arr[1])
                print(len(self.arr))
                self.BeginQueue(True)
                           
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
    def BeginQueue(self, timer):
      
        for i in range(len(self.arr)): 
            self.http_proxy.append("https://user:pass@" + self.arr[i])

            #1. Create timer random time between 0 and 10 minutes
            value = random.randint(0,10)
            mins  = 0

            if timer == True:
                print(value)
                if value:
                    while mins != 10:
                        time.sleep(value)
                        mins += 1
                print(str(i) + ": " + str(value))

        print("this is: " + str(self.http_proxy[i]))

                  
        proxies = {
                "https": self.http_proxy[i]
        }
            
        #2. Make requests with proxies
            
            
        try:
            print("1")
            r = requests.get(self.url, headers=self.headers, proxies=proxies)
            print(str(self.http_proxy[i]) + "--> good proxy..")
        except:
            print(str(self.http_proxy[i]) + "--> Bad proxy..")
    # -- End.. Where proxies connect to url

    
James = Bot()

James.main()
