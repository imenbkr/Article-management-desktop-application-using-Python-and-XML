#!/usr/bin/env python
# coding: utf-8

# # <font color=#483C32><center>XML PROJECT : SEARCH OR MODIFY XML FILES WITH PYTHON</center></font></center>

# ### <font color=#8E7618> Importing the necessary models and components : </font>

# In[2]:


import xml.etree.ElementTree as ET #for parsing and creating XML data.
#we can also use the dom.minidom module.
import xml.dom.minidom

import tkinter as tk #tkinter is a standard Python interface to the Tk GUI.
from tkinter import *
from tkinter import ttk #ttk module provides access to the Tk themed widget set.

from tkinter.ttk import Frame, Label,Entry,Button #importing necessary widgets.
from tkinter import Tk, StringVar, BOTH, W, E #importing necessary components for the display.


# ### <font color=#8E7618> Execute this code if you want to add elements to the XML file: </font>

# In[3]:


#FUNCTION TO ADD ELEMENTS TO AN XML FILE
def add_elements_to_file ():
                def addition():
                    #We can import this data by reading from a file.
                    mytree = ET.parse('publications.xml')
                    root = mytree.getroot() 
                    #create new sub-elements for a given element.
                    pub = ET.SubElement(root,"pub")
                    a=ET.SubElement(root,"author")
                    a.text=entry_2.get()
                    b=ET.SubElement(root,"pub_name")
                    b.text=entry_3.get()
                    c=ET.SubElement(root,"pub_type")
                    c.text=entry_4.get()
                    d=ET.SubElement(root,"year")
                    d.text=entry_5.get()
                    mytree.write("publications.xml")
                    
                #widget is to display text
                label_2 = ttk.Label(root, text="Enter name of author:")
                
                #implement a display box where you can place text 
                label_2.place(relx=0.01,rely=0.62)
                global entry_2
                
                #used to get input
                entry_2=Entry(root)
                entry_2.get() #returns the data of the entry widget which further can be printed on the console
                entry_2.place(relx=0.4,rely=0.62)  #implement a display box where you can place text  
                label_3 = ttk.Label(root, text='Enter name of publication:', width=20, font=("bold", 10))
                label_3.place(relx=0.01,rely=0.72)
                global entry_3
                entry_3=Entry(root)
                entry_3.get()
                entry_3.place(relx=0.4,rely=0.72)
                label_4 = ttk.Label(root, text='Enter type of publication:', width=20, font=("bold", 10))
                label_4.place(relx=0.01,rely=0.82)
                global entry_4
                entry_4=Entry(root)
                entry_4.get()
                entry_4.place(relx=0.4,rely=0.82)       
                label_5 = ttk.Label(root, text='Enter year of publication:', width=20, font=("bold", 10))
                label_5.place(relx=0.01,rely=0.92)
                global entry_5
                entry_5=Entry(root)
                entry_5.get()
                entry_5.place(relx=0.4,rely=0.92)
                bo= Button(root, text="Add" ,command= lambda:addition()) #button "Add" that will call the function "addition"
                bo.place(x=410, y=400) #implement a display box where you can place the button
                
                
                
#RADIO BUTTONS TO CHOOSE BETWEEN SEARCH TYPE
root= Tk() #creates the root window
root.geometry("500x500") #edit dimensions of the window
root.config(background='#DCDCDC') #background color
root.title("Add publications") #title
label1=tk.Label(root,text="Search or Modify publications?:",fg="#008080") #widget is to display text
label1.place(relx = 0, rely = 0)
var =StringVar() #Holds a string; the default value is an empty string
button1=tk.Radiobutton(root,text="Search for publications",variable=var,value="Search for publications")
button1.place(relx = 0.07, rely = 0.07)
var1 =StringVar()
button2=tk.Radiobutton(root,text="Add publication",variable=var1,value="Add publication")
button2.place(relx = 0.07, rely = 0.2)
#BUTTON TO PROCEED TO PLOT COMMAND
b5=tk.Button(root,text="Proceed",command=lambda:add_elements_to_file ())
b5.place(relx = 0.2, rely = 0.4)
root.mainloop()


# ### <font color=#8E7618> Execute this code if you want to search for elements in the XML file : </font>

# In[4]:


from distutils.filelist import findall #finds *all* the matches and returns them as a list of strings, with each string representing one match.
from struct import pack #This geometry manager organizes widgets in blocks.
from tkinter import *
import xml.etree.ElementTree as e #for parsing and creating XML data.
from tkinter import messagebox #used to display a message.

mytree=e.parse('publications.xml') #We can import this data by reading from a file.
myroot=mytree.getroot() #This function returns root element of the tree.
def recherche():
     nom_info=nom.get() #returns the data of the entry widget which further can be printed on the console
     l=[] #empty list
     for x in myroot.findall("pub"): #for x in the list of elements that matches "pub" in the xml file:
         item=x.find('author').text #item = name of the author in the xml file
         l.append(item) #adds item to the empty list l
         if item==nom_info: #if item matches the name of the author given by the user :
             Label(text="informations on the publication:",font=30,bd=1,relief=SOLID).place(x=25,y=120) #displays the specified text.
             Label(text="author",).place(x=25,y=150) #edit dimensions.
             Label(text=nom_info).place(x=60,y=150) #display the name of the author
             Label(text="publications name:").place(x=25,y=170)
             Label(text=x.find('pub_name').text).place(x=75,y=170) #display publication name
             Label(text="Publication type:").place(x=25,y=190)
             Label(text=x.find('pub_type').text).place(x=50,y=190) #display publication type
             Label(text="Venue:").place(x=25,y=210)
             Label(text=x.find('venue').text).place(x=90,y=210) #display venue
             Label(text="Year:").place(x=25,y=230)
             Label(text=x.find('year').text).place(x=65,y=230) #display year
                
     if nom_info not in l: #if name given by the user does not match the elements in the list:
             messagebox.showinfo("auteur inexsistant") #show the specified message
     nom_entry.delete(0,END) #delete the entry
    
screen=Tk() #creates the root window
screen.geometry("500x500") #edit dimensions of the window
screen.config(background='#DCDCDC') #background color
screen.title("Search in publications") #title
head=Label(screen,text="Search in publications:",bd=1,font=('Arial',15),bg="#DCDCDC",fg="black",width=0,height=0)
#display a head title
head.pack()
nom_text=Label(text="Enter name of author")  #display a specified text
nom_text.place(x=25,y=40)

nom=StringVar() #holds a string 
nom_entry=Entry(textvariable=nom) #used to get input
nom_entry.place(x=25,y=60) #edit dimensions 

valide=Button(text="Search",width="20",height="1",command=recherche) #button search which calls the function recherche
valide.place(x=25,y=85)
head.mainloop()  #to keep display of the window on loop.


# In[ ]:




