# -*- coding: utf-8 -*-
##### Zenab Tamimy
##### Personal Semantic Memory network

# Importing modules
import tkinter as t
import csv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

# Creating Page class from tkinter.Frame
class Page(t.Frame):
    def __init__(self, *args, **kwargs):
        t.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

# Creating Page One as a Page-Class
# Title and welcome text as objects in this class
class PageOne(Page):
    def __init__(self):
        Page.__init__(self)
        
        #Title
        titel = ("Personal visualization of Semantic Memory")
        
        titel_p1 = t.Message(self, text = titel)
        titel_p1.config(font=('calibri', 40, 'bold'), borderwidth=2, 
                        justify='center', width=1000, anchor='center')
        titel_p1.pack(pady=50)

        #Welcome Text
        welcome_text = ("With this app you will gain knowledge on Optimal" 
        "Foraging Theory(OFT) for human semantic memory by your own " 
        "experience.  You will have to participate in a verbal fluency task " 
        "where you will be asked to name 50 objects from a specific category. " 
        "We will try to visualize the retrieval process underlying your "  
        "responses to give you an idea of OFT based on your own responses.""")

        message_welcome_text = t.Message(self, text=welcome_text, 
                                         justify = 'center')
        message_welcome_text.config(justify='left', font=('calibri light', 20), 
                                    width=1000)
        message_welcome_text.pack(pady=50)
        
# Creating Page Two as a Page-Class
class PageTwo(Page):
    def __init__ (self):
        Page.__init__(self)
        
        #Title
        titel2 = ("Name 50 different animals")
        
        titel_p2 = t.Label(self, text = titel2)
        titel_p2.config(font=('calibri', 40, 'bold'), justify='left')
        titel_p2.grid(row=0, column=0, columnspan=5)
        
        #Task explanation
        task = ("Please try to spell the animal names correctly. \n" 
        "Do not use other sources to come up with the animal names.")
        
        message_task = t.Label(self, text=task)
        message_task.config(justify='left', font=('calibri light', 20))
        message_task.grid(row=1, rowspan=4, column=0, columnspan=5, pady = 10)
        
        #For loop to create 25 entry widgets for animals
        counter = 0
        self.entries_animals = []
        for c in range(5):
            for n in range(6,10):
            # create entries list
                self.entries_animals.append(t.Entry(self, width=25, font=(20), 
                                                    bg='#BDD7EE'))
            # grid layout the entries
                self.entries_animals[counter].grid(row=n, column=c, pady=3, 
                                    padx=3)
                counter += 1      
        
        #Submit button to evoke command   
        submit = t.Button(self, text="Submit Animals", command=self.transfer)
        submit.config(bg='#F8CBAD', font=('calibri light', 20))
        submit.grid(row=11, column=2)  
        
        #Task 2 explanation text
        task2 = ("Now categorize your responses in the same order")
        
        message_task2 = t.Label(self, text = task2)
        message_task2.config(justify='left', font=('calibri light', 20))
        message_task2.grid(row=12, column=0, columnspan=5, pady=10)
        
        #For loop to create 25 entry widgets for categories
        counter = 0
        self.entries_categories = []
        for c in range(5):
            for n in range(13,17):
            # create entries list
                self.entries_categories.append(t.Entry(self, width=25, 
                                                       font=(20), 
                                                            bg='#BDD7EE'))
            # grid layout the entries
                self.entries_categories[counter].grid(row=n, column=c, pady=3, 
                                       padx=3)
                counter += 1  
                
        #Submit button to evoke command        
        submit2 = t.Button(self, text="Submit Categories", 
                           command=self.transfer2) 
        submit2.config(bg='#F8CBAD', font=('calibri light', 20))
        submit2.grid(row=18, column=2)  
        
    # Function that is evoked when submit button for animals is pressed
    def transfer(self):
        global animals
        
        animals = []
        
        for i in range(49):
            animals.append(self.entries_animals[i].get())  
            
            f = open(r'C:\Users\Zenab\Documents\VerbalFluencyData.csv', 'w')
            w=csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
            w.writerow([animals])
            f.close()
    
    # Function that is evoked when submit button for categories is pressed        
    def transfer2(self):
        global categories
        
        categories = []
        
        for i in range(49):
            categories.append(self.entries_categories[i].get())  
            
            f = open(r'C:\Users\Zenab\Documents\Categories.csv', 'w')
            w=csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
            w.writerow([categories])
            f.close()

# Creating Page Three as a Page class        
class PageThree(Page):
    def __init__ (self):
        Page.__init__(self)
        
        #Title
        titel4 = ("Your Personal Semantic Memory Network")
        
        message_titel4 = t.Label(self, text=titel4)
        message_titel4.config(font=('calibri', 35, 'bold'))
        message_titel4.place(anchor='center', relx=.45, rely=.1)
        
        #Creating button that evokes network funtion
        network_button = t.Button(self, text="Make My Network", 
                                  command=self.network)
        network_button.config(bg='#F8B0AE', font=('calibri light', 20))
        network_button.place(anchor='center', relx=.45, rely=.5)
    
    # Creating networking function that plots network of the entries of user
    def network(self):
        
        # Creating a dataframe from the entries of the user
        df = pd.DataFrame(data = [animals, categories])
        df = df.transpose()

        # Specifying the model in terms of edges using two loops:
            # 1) Create edge when two responses are from the same category
        edges = []
        for st in range(len(df.index)-1):
                for comp in range(len(df.index)-1):
                    if df.iloc[st][1] == df.iloc[comp][1]:
                        edge = (df.iloc[st][0],df.iloc[comp][0])
                        edges.append(edge)
            
            # 2) Create switching edges when two responses differ in category
        for sw_edge_st in range(0, len(df.index)-1):
            if df.iloc[sw_edge_st][1] != df.iloc[sw_edge_st+1][1]:
                edge = (df.iloc[sw_edge_st][0],df.iloc[sw_edge_st+1][0])
                edges.append(edge)            
        
        
        ## Plotting the network
        graph = edges
        
        f = plt.figure(figsize=(8,4))
        plt.axis('off')
         
        nodes = set([n1 for n1, n2 in graph] + [n2 for n1, n2 in graph])

        # Create networkx graph
        G=nx.Graph()

        # Add nodes
        for node in nodes:
            G.add_node(node)

        # Add edges
        for edge in graph:
            G.add_edge(edge[0], edge[1])

        # Draw graph
        pos = nx.spring_layout(G)
        nx.draw(G, pos, node_color='#F8CBAD', node_size=2000, with_labels=True)

        # Add tk.DrawingArea
        canvas = FigureCanvasTkAgg(f, master=self)
        canvas.show()
        canvas.get_tk_widget().pack(pady=120, padx=210, anchor='w')

# Create Page Four as a Page Class
class PageFour(t.Frame):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        
        # Title
        titel4 = ("Optimal Foreaging Theory for Semantic Memory")
        
        message_titel4 = t.Label(self, text = titel4)
        message_titel4.config(font=('calibri', 35, 'bold'))
        message_titel4.place(anchor='center', relx =.45 , rely =.1)
        
# Create Main View of the App by inheritance of all the pages into mainview
class MainView(t.Frame):
    def __init__(self, *args, **kwargs):
        t.Frame.__init__(self, *args, **kwargs)
        
        # Call pages
        p1 = PageOne()
        p2 = PageTwo()
        p3 = PageThree()
        p4 = PageFour()
        
        # Creating containter to place pages in
        container = t.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        
        # Placing pages
        p1.place(in_=container, relx=0, rely=0, relwidth=1, relheight=1)
        p2.place(in_=container, relx=0.05, rely=0, relwidth=1, relheight=1)
        p3.place(in_=container, relx=0.05, rely=0, relwidth=1, relheight=1)  
        p4.place(in_=container, relx=0.05, rely=0, relwidth=1, relheight=1)

        # Creating buttons
        b1 = t.Button(p1, text="Continue >>", command=p2.lift)
        b2 = t.Button(p2, text="Continue >>", command=p3.lift)
        b3 = t.Button(p3, text="Continue >>", command=p4.lift)
        b4 = t.Button(p4, text="End | ", command=p1.lift)
        b4_back = t.Button(p4, text = '<< Network', command = p3.lift)
        
        # Button configurations
        b1.config(bg='#c5e0b4', width=10, font=('times', 20))
        b2.config(bg='#c5e0b4', width=10, font=('times', 20))
        b3.config(bg='#c5e0b4', width=10, font=('times', 20))
        b4.config(bg='#F8B0AE', width=10, font=('times', 20))
        b4_back.config(bg = '#F8CBAD', width=10, font=('times', 20))
        
        # Button placings 
        b1.place(anchor='center', rely=.8, relx=.8)
        b2.place(anchor='center', rely=.8, relx=.75)
        b3.place(anchor='center', relx=.75, rely=.8)
        b4.place(anchor='center', rely=.8, relx=.75)
        b4_back.place(anchor='center', rely=.8, relx=.15)

        # Specify starting page
        p1.show()
        
# Call software
if __name__ == "__main__":
    root = t.Tk()
    main = MainView(root)
    main.pack(side="bottom", fill="both", expand=True)
    root.wm_state('zoomed')
    root.mainloop()
        
