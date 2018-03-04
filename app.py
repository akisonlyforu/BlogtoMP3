# Author - Avinash Kumar (akisonlyforu)

import bs4 as bs # For Scraping
import urllib.request # To connect url
import sys 
import os # To save MP3
from gtts import gTTS # To create MP3
import string # For String Manipulation
import re  # For regex
from tkinter import * # For GUI
from tkinter import messagebox # For prompt message box

# Method to generate MP3 and TXT from ThoughtCatalog Blog post
def generatetc(str):
    try:
        source = urllib.request.urlopen(str);
        soup = bs.BeautifulSoup(source,'lxml');
        summary=soup.find('div',class_='summary'); #For posts with summary
        match=soup.find('article',id='article-sticky'); #For sponserd posts
        if(match==None):
            match = match=soup.find('article',class_='tc_article tc_article-width entry post'); #For normal posts
        str=soup.title.text+"\n"+"\n";
        if(summary!=None):
            str+=summary.text+"\n";
        name=soup.title.text;
        for paragraph in match.find_all(['h3' , 'h2' , 'h3' , 'p']):
            str+=paragraph.text+"\n" #Generating string

        name = re.sub(r'[^\w\s]','',name) #Regex used here to remove punctuations from Title
        st =name + ".mp3"; #name of MP3 file
        nameoffile= name + ".txt"; #name of TXT file
        with open(nameoffile, "w") as text_file:
            text_file.write(str)  #Generating txt file
        language = 'en';
        myobj = gTTS(text=str, lang=language, slow=False);
        myobj.save(st); #Generating MP3
        messagebox.showinfo("ThoughtCatalog Blog to MP3 " , " Successful. MP3 and TXT Generated. \n Location : Current Directory " );
    except (Exception) as e:
        messagebox.showinfo("ThoughtCatalog Blog to MP3 " , " Failed. Please check URL or your internet connection. If everything is right at your end, send a mail to avinashkr226@gmail.com along with the article link." );

# Method to generate MP3 and TXT from ThoughtCatalog Blog post
def generatemedium(url):
    try:
        req = urllib.request.Request(
            url, 
            data=None, 
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        f = urllib.request.urlopen(req)
        soup=bs.BeautifulSoup(f,'lxml');
        match1=soup.find('h1',class_='ui-brand2 u-marginBottom30'); #For Medium members only articles.
        if (match1!=None):
            messagebox.showinfo("Medium Blog to MP3 " , "This is a Medium Only for Member's story. Please Visit the web page to read the stroy. We do not support it yet.");
            return;
        match=soup.find('div',class_='postArticle-content js-postField js-notesSource js-trackedPost'); #For articles which does not require sign-in
        str=soup.title.text+"\n\n";
        name=soup.title.text;
        for paragraph in match.find_all(['p' , 'h4' , 'h3' , 'h2' , 'blockquote']):
            str+=paragraph.text+"\n"; #Generating string
        st =name + ".mp3";  #name of MP3 file
        nameoffile= name + ".txt";  #name of TXT file
        with open(nameoffile, "w") as text_file:
            text_file.write(str)  #Generating txt file
        language = 'en';
        myobj = gTTS(text=str, lang=language, slow=False);
        myobj.save(st); #Generating MP3
        messagebox.showinfo("Medium Blog to MP3 " , " Successful. MP3 and TXT Generated. \n Location : Current Directory  " );
    except (Exception) as e:
        messagebox.showinfo("Medium Blog to MP3 " , " Failed. Please check URL or your internet connection. If everything is right at your end, send a mail to avinashkr226@gmail.com along with the article link;" );    

# Method to exit Window
def exit():
    root.destroy();

# Method to display about
def about():
    messagebox.showinfo("Blog to MP3 " , " Version 1.0 \n Developed by akisonlyforu \n Feedback - avinashkr226@gmail.com " );

# Method to display Instructions
def instructions():
    messagebox.showinfo("Blog to MP3 " , " With this tool, you can download your favorite articles as portable mp3's and txt's and enjoy reading/listening any time you want. Currently it supports only two websites , ThoughtCatalog and Medium. \n Note - On Medium only those articles are supported , which does not require user login. (Working on it)." );

# Method used here to obtain which radiobutton is selected
def selected():
    return var.get()

# Method to generate MP3 and TXT 
def generate():
    output1=tc_entry.get();
    output=selected();
    if(output=="med"):
       generatemedium(output1);
    else:
       generatetc(output1);

# Method to clear text field    
def clear():
    text=""
    tc_entry.delete(0,END)
    tc_entry.insert(0,text)
    return

root = Tk()
root.resizable(width=False, height=False) #Size fixed of Window
root.title('Blog to MP3') #Title of Window
root.geometry('500x200') #Default Size
var = StringVar()
var.set('Not yet defined')

#RadioButton for selecting ThoughtCatalog
rb_tc = Radiobutton(text='ThoughtCatalog Article' , variable = var, padx = 20  ,value="tc" , command=selected );
rb_tc.grid(row=0, pady = 20);
#RadioButton for selecting Medium
rb_med = Radiobutton(text='Medium Article', variable = var ,value="med" , padx = 10 , command=selected );
rb_med.grid(row=0, column= 1 , pady = 20 );

#Label
tc = Label(root,text="Blog Link Here -");
tc.grid(row = 2 , column = 0 , padx = 10 , pady = 20);
#Label for warning
progress = Label(root,text="After clicking on Generate Button, don't close \n the Window and wait for status message. ");
progress.grid(row = 3 , column = 0 , columnspan = 2 , padx = 10 , pady = 20);

#Textbox for input
tc_entry = Entry(root );
tc_entry.grid(row=2,column=1);

#Generate Button
gen = Button(root, text = "Generate" , command=generate);
gen.grid(row = 3 , column = 2 , padx = 10 , pady = 10);
#Clear Button
clr = Button(root, text = "Clear" , command=clear);
clr.grid(row = 2 , column = 2 , padx = 10 , pady = 10);

#For main Menu
menu = Menu(root);
root.config(menu=menu);

# For file SubMenu
submenu=Menu(menu);
menu.add_cascade(label="File" , menu=submenu);
submenu.add_command(label="Exit" ,command = exit);  

# For Edit SubMenu
editmenu = Menu(menu);
menu.add_cascade(label="Help" , menu=editmenu);
editmenu.add_command(label="About" ,command = about);
editmenu.add_command(label="Instructions" , command = instructions); 


root.mainloop();
