from tkinter import *


with open('File_1.txt') as f1:
    s1=f1.read().lower().split()
    l1=[]
    for i in s1:
        if i.isalnum():
            l1.append(i)
with open('File_2.txt') as f2:
    s2=f2.read().lower().split()
    l2=[]
    for i in s2:
        if i.isalnum():
            l2.append(i)


plag_words=len(set(l1).intersection(set(l2)))

total_words=len(l1)+len(l2)

plag_percent=100-round((total_words-plag_words*2)/total_words*100)

result="      The Plagarized Content Percent among two files is "+str(plag_percent)+"%"
if plag_percent30 and plag_percent&lt;=60:
    win= Tk()
    win.geometry(&quot;800x200&quot;)
    canvas= Canvas(win, width= 700, height= 650, bg=&quot;Yellow&quot;)
    canvas.create_text(300, 100, text=result, fill=&quot;black&quot;, font=(&#039;Helvetica 15 bold&#039;))
    canvas.pack()
    win.mainloop()
else:
    win= Tk()
    win.geometry(&quot;800x200&quot;)
    canvas= Canvas(win, width= 700, height= 650, bg=&quot;Red&quot;)
    canvas.create_text(300, 100, text=result, fill=&quot;black&quot;, font=(&#039;Helvetica 15 bold&#039;))
    canvas.pack()
    win.mainloop()
