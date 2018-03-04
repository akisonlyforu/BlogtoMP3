<h1>BlogtoMP3</h1>
GUI Application for Desktop built with python to convert Online Blog Post's to MP3 and TXT 

<h2>Getting Started</h2>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

<h3>Prerequisites</h3>
What things you need to install the software and how to install them.

```
Python

Libraries - 
bs4
gTTS
re
urllib.request
tkinter
string
os
```
<h3>Installing</h3>

```
For Linux and Mac, simpy run the Python File.
For Windows , run the Python/IDLE in administrator Mode and then execute.
```
<h2>Built With</h2>
  
```
Python
Google Text To Speech Library
BeautifulSoup4 Library
Tkinter Library
```

<h2> How to use it ? </h2>
The interface looks like this :

![Blog2MP3 interface](/readme_1.jpg)

Currently it supports only 2 websites as these are the blog websites, I read the most. More sites will be added as per need.
1) [ThoughtCatalog](https://www.thoughtcatalog.com)
2) [Medium](https://www.medium.com)

Steps to generate MP3 and TXT -
1) Choose the website by selecting appropriate radiobutton.
2) Copy the URL of the BlogPost.
3) Paste the URL in the TextField
4) Click on Generate

Note - After pressing the generate button, dont click on any other button/menu. Wait until the status message is generated.

Status message "Accepted" -

![Blog2MP3 Accepted](/readme_3.jpg)

Status message "Error" - 

![Blog2MP3 interface](/readme_2.jpg)

<h3> Saved File Location </h3>

The TXT and MP3 files generated are saved in the directory where the source file is stored. Their titles are in accordance with the blog titles.

Sample saved file - 

![Saved Files Location](/readme_4.jpg)

<h3> Help </h3>

To get help at any point of time, click the “Help” button.


To contact for any query or feedbacks, simply drop a mail at – <br>

avinashkr226@gmail.com <br>


<h3>Author</h3>

[Avinash Kumar](https://www.linkedin.com/in/akavinashkumar)


<h2>License</h2>
This project is licensed under the MIT License - see the LICENSE.md file for details
