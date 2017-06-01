# -*- coding: utf-8 -*-
import tkinter as t
import csv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np

class Page(t.Frame):
    def __init__(self, *args, **kwargs):
        t.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class PageOne(Page):
    def __init__(self):
        Page.__init__(self)
        
        titel = ("Personal visualization of Semantic Memory")
        
        message2 = t.Message(self, text = titel)
        message2.config(font = ('calibri', 40, 'bold'), borderwidth = 2, justify = 'center', width=1000, anchor = 'center')
        message2.pack(pady = 50)

        welkomtekst = ("With this app you will gain knowledge on Optimal Foraging" 
        "Theory(OFT) for human semantic memory by your own experience. You will have " 
        "to participate in a verbal fluency task where you will be asked to name 50" 
        "objects from a specific category. We will try to visualize the retrieval" 
        "process underlying your responses to give you an idea of OFT based on your"  
        "own responses.""")

        message = t.Message(self, text = welkomtekst, justify = 'center')
        message.config(justify = 'left', font=('calibri light', 20), width = 1000)
        message.pack(pady = 50)
        
class PageTwo(Page):
    def __init__ (self):
        Page.__init__(self)
        
        titel2 = ("Name 50 different animals")
        
        message_titel2 = t.Label(self, text = titel2)
        message_titel2.config(font = ('calibri', 40, 'bold'), justify = 'left')
        message_titel2.grid(row = 0, column = 0, columnspan = 5)
        
        opdracht = ("Please try to spell the animal names correctly. \n" 
        "Do not use other sources to come up with the animal names.")
        
        message_opdracht = t.Label(self, text = opdracht)
        message_opdracht.config(justify = 'left', font=('calibri light', 20))
        message_opdracht.grid(row = 1, rowspan = 4, column = 0, columnspan= 5, pady = 10)

        counter = 0
        self.entries_animals = []
        for c in range(5):
            for n in range(6,10):
            # create entries list
                self.entries_animals.append(t.Entry(self, width = 25, font = (20), bg = '#BDD7EE'))
            # grid layout the entries
                self.entries_animals[counter].grid(row=n, column=c, pady = 3, padx =3)
                counter += 1      
                
        submit = t.Button(self, text = "Submit Animals", command = self.transfer) #hier moet een command als writetofile achter
        submit.config(bg = '#F8CBAD', font = ('calibri light', 20))
        submit.grid(row = 11, column = 2)  
        
        opdracht2 = ("Now categorize your responses in the same order")
        message_opdracht2 = t.Label(self, text = opdracht2)
        message_opdracht2.config(justify = 'left', font = ('calibri light', 20))
        message_opdracht2.grid(row = 12, column =0, columnspan =5, pady =10)
        
        counter = 0
        self.entries_categories = []
        for c in range(5):
            for n in range(13,17):
            # create entries list
                self.entries_categories.append(t.Entry(self, width = 25, font = (20), bg = '#BDD7EE'))
            # grid layout the entries
                self.entries_categories[counter].grid(row=n, column=c, pady = 3, padx =3)
                counter += 1  
                
        submit2 = t.Button(self, text = "Submit Categories", command = self.transfer2) #hier moet een command als writetofile achter
        submit2.config(bg = '#F8CBAD', font = ('calibri light', 20))
        submit2.grid(row = 18, column = 2)  
        
    def transfer(self):
        global animals
        
        animals = []
        
        for i in range(49):
            animals.append(self.entries_animals[i].get())  
            
            f = open(r'C:\Users\Zenab\Documents\VerbalFluencyData.csv', 'w')
            w=csv.writer(f, delimiter=',',quoting=csv.QUOTE_ALL)
            w.writerow([animals])
            f.close()
            
    def transfer2(self):
        global categories
        
        categories = []
        
        for i in range(49):
            categories.append(self.entries_categories[i].get())  
            
            f = open(r'C:\Users\Zenab\Documents\Categories.csv', 'w')
            w=csv.writer(f, delimiter=',',quoting=csv.QUOTE_ALL)
            w.writerow([categories])
            f.close()
                
#class PageThree(Page):
#    def __init__ (self):
#        Page.__init__(self)
#        
#        titel3 = ("Spell Check")
#        
#        message_titel3 = t.Label(self, text = titel3)
#        message_titel3.config(font = ('calibri', 35, 'bold'))
#        message_titel3.place(anchor = 'e', relx = .5 , rely = .2)
#        
##        catbut = t.Button (self, text = "Categorize My Response", command = self.showinput1)
##        catbut.place(anchor = 'e', relx= .5, rely = .7)
#        
##    def showinput1(self):
##        
###        tekstje = input[0]
###        ttt = t.Label(self, text = tekstje)
###        ttt.config(font = ('calibiri', 20, 'bold'))
###        ttt.place(anchor = 'e', relx = .5, rely = .8)
##        
###        t.Label(self, text = input[1])  
##        
##        var = t.StringVar()
##        var.set(input[0])
##        choices = ['a', 'b']
##        option = t.OptionMenu(self, var, *choices, command = self.showinput2)
##        option.place(anchor = 'e', relx = .5, rely = .7)
##
##    def showinput2(self):
##        
###        tekstje = input[0]
###        ttt = t.Label(self, text = tekstje)
###        ttt.config(font = ('calibiri', 20, 'bold'))
###        ttt.place(anchor = 'e', relx = .5, rely = .8)
##        
###        t.Label(self, text = input[1])  
##        
##        var = t.StringVar()
##        var.set(input[1])
##        choices = ['a', 'b']
##        option = t.OptionMenu(self, var, *choices)
##        option.place(anchor = 'e', relx = .5, rely = .7)
#        
#        vraag1 = ('You typed "harig". Did you mean "haring" ? ')
#        
#        message_vraag1 = t.Label(self, text = vraag1)
#        message_vraag1.config(font=('times', 24, 'italic'))
#        message_vraag1.place(anchor = 'center', relx = .425 , rely = .3)
#        
#        v = t.StringVar()
#        
#        yesbutton = t.Radiobutton(self, text = "Yes", variable = v, value = 1, indicatoron = 0, width = 10)
#        yesbutton.config(font = ('times', 20, 'italic'), bg = 'light steel blue')
#        yesbutton.place(anchor = 'center', relx = .425, rely = .5)
#        
#        nobutton = t.Radiobutton(self, text = "No", variable = v, value = 0, indicatoron = 0, width = 10)
#        nobutton.config(font = ('times', 20, 'italic'), bg = 'light steel blue')
#        nobutton.place(anchor = 'center', relx = .425, rely = .6)
#        nobutton.deselect()
#        
class PageThree(Page):
    def __init__ (self):
        Page.__init__(self)
        
        titel4 = ("Your Personal Semantic Memory Network")
        
        message_titel4 = t.Label(self, text = titel4)
        message_titel4.config(font = ('calibri', 35, 'bold'))
        message_titel4.place(anchor = 'center', relx = .45 , rely = .1)
        
        network_button = t.Button(self, text = "Make My Network", command = self.network)
        network_button.config(bg = '#F8B0AE', font = ('calibri light', 20))
        network_button.place(anchor ='center', relx = .45, rely = .5)
        
        ##################
        #Specifying Edges
#        data = np.array([["Hond", 'Pet'],
#                ["Kat", "Pet"],
#                ["muis", 'knaagdier'],
#                ["cavia", "knaagdier"],
#                ["Gorilla", "Africa"]])
#        
#
#        df = pd.DataFrame(data=data)

    def network(self):
        global edges
        df = pd.DataFrame(data = [animals, categories])
        df = df.transpose()

        edges = []
        for st in range(len(df.index)-1):
                for comp in range(len(df.index)-1):
                    if df.iloc[st][1] == df.iloc[comp][1]:
                        edge = (df.iloc[st][0],df.iloc[comp][0])
                        edges.append(edge)
                        
        for sw_edge_st in range(0, len(df.index)-1):
            if df.iloc[sw_edge_st][1] != df.iloc[sw_edge_st+1][1]:
                edge = (df.iloc[sw_edge_st][0],df.iloc[sw_edge_st+1][0])
                edges.append(edge)            
        
        
        ## NETWORK PLOTTING
        graph = edges
        
        f = plt.figure(figsize=(8,5))
        a = f.add_subplot(111)
        plt.axis('off')
        
        ###NETWORK
        # the networkx part
#        G=nx.complete_graph(5)
#        nx.draw_networkx(G,pos=nx.spring_layout(G),ax=a)
            # extract nodes from graph
            
        nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

        # create networkx graph
        G=nx.Graph()

        # add nodes
        for node in nodes:
            G.add_node(node)

        # add edges
        for edge in graph:
            G.add_edge(edge[0], edge[1])

        # draw graph
        pos = nx.spring_layout(G)
        nx.draw(G, pos, node_color = '#F8CBAD', node_size = 2000, with_labels = True)

        # a tk.DrawingArea
        canvas = FigureCanvasTkAgg(f, master=self)
        canvas.show()
        canvas.get_tk_widget().pack(pady = 120, padx = 210, anchor = 'w')
#
#        def next_graph():
#            if G.order():
#                a.cla()
#                G.remove_node(G.nodes()[-1])
#                nx.draw(G, pos=nx.circular_layout(G), ax=a)
#                canvas.draw()
        
class PageFour(t.Frame):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        titel4 = ("Optimal Foreaging Theory for Semantic Memory")
        
        message_titel4 = t.Label(self, text = titel4)
        message_titel4.config(font = ('calibri', 35, 'bold'))
        message_titel4.place(anchor = 'center', relx = .45 , rely = .1)
        
        
        
#        welkomtekst = ("With this app you will gain knowledge on Optimal Foraging" 
#        "Theory(OFT) for human semantic memory by your own experience. You will have " 
#        "to participate in a verbal fluency task where you will be asked to name 50" 
#        "objects from a specific category. We will try to visualize the retrieval" 
#        "process underlying your responses to give you an idea of OFT based on your"  
#        "own responses.""")
#
#        message = t.Message(self, text = welkomtekst, justify = 'center')
#        message.config(justify = 'left', font=('calibri light', 20), width = 500)
#        message.pack(pady = 50, padx = 500)
#        
#        
#        network_button = t.Button(self, text = "Make My Network", command = self.network)
#        network_button.place(anchor ='center', relx = .3, rely = .5)
#        
#        
#        ##################
#        #Specifying Edges
##        data = np.array([["Hond", 'Pet'],
##                ["Kat", "Pet"],
##                ["muis", 'knaagdier'],
##                ["cavia", "knaagdier"],
##                ["Gorilla", "Africa"]])
##        
##
##        df = pd.DataFrame(data=data)
#
#    def network(self):
#        global edges
#        df = pd.DataFrame(data = [animals, categories])
#        df = df.transpose()
#
#        edges = []
#        for st in range(len(df.index)-1):
#                for comp in range(len(df.index)-1):
#                    if df.iloc[st][1] == df.iloc[comp][1]:
#                        edge = (df.iloc[st][0],df.iloc[comp][0])
#                        edges.append(edge)
#                        
#        for sw_edge_st in range(0, len(df.index)-1):
#            if df.iloc[sw_edge_st][1] != df.iloc[sw_edge_st+1][1]:
#                edge = (df.iloc[sw_edge_st][0],df.iloc[sw_edge_st+1][0])
#                edges.append(edge)            
#        
#        
#        ## NETWORK PLOTTING
#        graph = edges
#        
#        f = plt.figure(figsize=(5,4))
#        a = f.add_subplot(111)
#        plt.axis('off')
#        
#        ###NETWORK
#        # the networkx part
##        G=nx.complete_graph(5)
##        nx.draw_networkx(G,pos=nx.spring_layout(G),ax=a)
#            # extract nodes from graph
#            
#        nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])
#
#        # create networkx graph
#        G=nx.Graph()
#
#        # add nodes
#        for node in nodes:
#            G.add_node(node)
#
#        # add edges
#        for edge in graph:
#            G.add_edge(edge[0], edge[1])
#
#        # draw graph
#        pos = nx.spring_layout(G)
#        nx.draw(G, pos, node_color = '#F8CBAD', node_size = 2000, with_labels = True)
#
#        # a tk.DrawingArea
#        canvas = FigureCanvasTkAgg(f, master=self)
#        canvas.show()
#        canvas.get_tk_widget().pack(anchor = 'w', pady = 120)
#        
        

class MainView(t.Frame):
    def __init__(self, *args, **kwargs):
        t.Frame.__init__(self, *args, **kwargs)
        p1 = PageOne()
        p2 = PageTwo()
        p3 = PageThree()
        p4 = PageFour()

        container = t.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        
        p1.place(in_=container, relx=0, rely=0, relwidth=1, relheight=1)
        p2.place(in_=container, relx=0.05, rely=0, relwidth=1, relheight=1)
        p3.place(in_=container, relx=0.05, rely=0, relwidth=1, relheight=1)  
        p4.place(in_=container, relx=0.05, rely=0, relwidth=1, relheight=1)

        b1 = t.Button(p1, text="Continue >>", command=p2.lift)
        b2 = t.Button(p2, text="Continue >>", command=p3.lift)
        b3 = t.Button(p3, text="Continue >>", command=p4.lift)
        b4 = t.Button(p4, text="End | ", command=p1.lift)
        b4_back = t.Button(p4, text = '<< Network', command = p3.lift)
        
        b1.config(bg='#c5e0b4', width = 10, font = ('times', 20))
        b2.config(bg='#c5e0b4', width = 10, font = ('times', 20))
        b3.config(bg='#c5e0b4', width = 10, font = ('times', 20))
        b4.config(bg='#F8B0AE', width = 10, font = ('times', 20))
        b4_back.config(bg = '#F8CBAD', width = 10, font = ('times', 20))

        b1.place(anchor = 'center', rely = .8, relx = .8)
        b2.place(anchor = 'center', rely = .8, relx = .75)
        b3.place(anchor = 'center', relx = .75, rely = .8)
        b4.place(anchor = 'center', rely = .8, relx = .75)
        b4_back.place(anchor = 'center', rely = .8, relx = .15)


        p1.show()
        
if __name__ == "__main__":
    root = t.Tk()
#    root.attributes('-fullscreen', True)
    main = MainView(root)
    main.pack(side="bottom", fill="both", expand=True)
    root.wm_state('zoomed')
    root.mainloop()
        
