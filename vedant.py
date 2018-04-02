from bs4 import BeautifulSoup

def checkattendance():
    fr=open('erp.txt','r')
    text=fr.read()
    soup = BeautifulSoup(text,"html.parser")
    fr.close()
    present=0
    absent=0
    for link in soup.findAll('td', {'data-title':'Present'}):
            p=int(link.string)
            present+=p
    for link in soup.findAll('td', {'data-title':'Absent'}):
             a=int(link.string)
             absent+=a
    print("absent",absent)
    total=present+absent
    print("present=",present,"total=",total,"aggreagate=",present*100/total)



checkattendance()
