from flask import Flask, request, render_template
import urllib.request as urllib2

from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my_form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']

    req = urllib2.Request(text, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib2.urlopen(req)

    soup = BeautifulSoup(webpage, 'html.parser')
    sno=1
    flag=0
    MyAns=[]
    CorrAns=[]
    for section in soup.findAll('td'):
        td_text=section.get_text(strip=True)
        if flag == 1:
            MyAns.append(td_text)
            flag=0;
        elif td_text == 'Chosen Option :':
            flag=1;
        elif section.has_key('class') and section['class'][0] == 'rightAns':
            ans=td_text[:1]
            CorrAns.append(ans)
        sno=sno+1;

    cPos=0;
    cNeg=0;
    for i in range(len(MyAns)):
        if(CorrAns[i]=='A'):
            CorrAns[i]='1'
        elif(CorrAns[i]=='B'):
            CorrAns[i]='2'
        elif(CorrAns[i]=='C'):
            CorrAns[i]='3'
        elif(CorrAns[i]=='D'):
            CorrAns[i]='4'
            
    for i in range(len(MyAns)):
        if(MyAns[i] == CorrAns[i]):
            cPos=cPos+1;
        elif(MyAns[i] != "--"):
            cNeg=cNeg+1;

    s="Correct Attempt: " + str(cPos) +"\n";
    s=s+"Wrong Attempt: " + str(cNeg);
    return s;


'''if __name__=='__main__':
    app.run()
'''

