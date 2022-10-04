from flask import Flask,request
import openpyxl
from scraper import web_scrape
import pandas as pd

app = Flask(__name__)

@app.get('/')
def showUp():
    return("This is home")


@app.post('/execute')
def doIt():
    data=request.get_json()
    
    url=data["url"]
    selector=data["selector"]
    fxn=data["fxn"]

    if(url):
        data=web_scrape(url, selector)

        if(fxn=="excel"):
            df=pd.DataFrame(data)
            # df.to_excel('bigup.xlsx')
            print('reading this')
            return (data)

        return(data)

    
    return (url)


# app.run(port=3000)
