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
from Tkinter import *
import ttk


class Bot():
    proxy_list     = ["http://www.httptunnel.ge/ProxyListForFree.aspx"]
    fname          = "proxies/proxies.txt"
    custom_proxies = "proxies/userscustom/myproxies.txt"
    mydivs         = 0
    url            = 0
    arr            = []
    
    def main(self):  
        while not self.url:

            self.url = raw_input("url -> ")   

        self.proxy_scan(False)
    
    def proxy_scan(self, ownFile):
        print("starting proxy scan..")

        if ownFile == True:
            print("Chose option to connect with your own proxies..")
            try:
                with open(self.custom_proxies, 'r') as f:
                    
                    print(f.read())
                    
            except:
                print("Error")
                
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
                
                           
            else:
                print("server down trying custom_proxies.txt..")
                try:
                    with open(self.custom_proxies, 'r') as f:
                    
                        print(f.read())
                    
                except:
                    print("Error")


    def write_to_file(self,ipport):

        try:
            with open(self.fname, 'a+') as f:
                for i in range(len(ipport)):          
                    f.write(ipport[i] + "\n")

        except:
            print("Error")

    def LoadMenu(self):
        root = Tk()

        root.title("tbot")

        root.geometry("500x500") #You want the size of the app to be 500x500
        root.resizable(0, 0) #Don't allow resizing in the x or y direction
        
        l =ttk.Label(root, text="Starting...")
        l.grid()

        frame1 = Frame(root)
        frame1.pack(side="bottom", fill="both", expand = True)
        frame1.grid_rowconfigure(0, weight=1)
        frame1.grid_columnconfigure(0, weight=1)
        
        button = ttk.Button(frame1, text="Hello", command="buttonpressed")
        button.grid()
        

        button.bind('<Button-1>', lambda e: proxy_scan())
        button.bind('<Enter>', lambda e: l.configure(text='Moved mouse inside'))
        button.bind('<Leave>', lambda e: l.configure(text='Moved mouse outside'))


        
        l.bind('<1>', lambda e: l.configure(text='Clicked lefouse button'))
        l.bind('<Double-1>', lambda e: l.configure(text='Double clicked'))
        l.bind('<B3-Motion>', lambda e: l.configure(text='right button drag to %d,%d' % (e.x, e.y)))

        root.mainloop()


James = Bot()

James.main()
