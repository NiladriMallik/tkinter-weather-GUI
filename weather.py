from tkinter import *
from tkinter.font import BOLD
import requests
import json
import pandas as pd

#read the csv file containing weather codes and descriptions
weather=pd.read_csv('weather-codes/weathercodes.txt',sep='\t')

#get the first two columns and put them into a dictionary for future reference
weatherDict=dict(zip(weather.values[:,0],weather.values[:,1]))

root=Tk()
root.title('Weather Now')
root.iconbitmap('icons/weather.ico')
root.configure(background='#03021c')


params={
    'access_key':'get-your-own-access-key',
    'query':'Kolkata'
}

uvIndexColors={
    0:['Low','green'],
    1:['Low','green'],
    2:['Low','green'],
    3:['Moderate to High','yellow'],
    4:['Moderate to High','yellow'],
    5:['Moderate to High','yellow'],
    6:['Moderate to High','orange'],
    7:['Moderate to High','orange'],
    8:['Very High to Extreme','red'],
    9:['Very High to Extreme','red'],
    10:['Very High to Extreme','red'],
    11:['Very High to Extreme','dark violet']
}


try:
    api_request=requests.get("http://api.weatherstack.com/current",params)
    api=json.loads(api_request.content)
    
    #get the values from the api dictionary
    currDate=api['location']['localtime'][0:10]
    currTime=api['location']['localtime'][-5:]
    city=api['location']['name']
    state=api['location']['region']
    country=api['location']['country']
        
    uvIndex=api['current']['uv_index']
    temperature=api['current']['temperature']
    weather_desc=api['current']['weather_descriptions'][0]
    humidity=api['current']['humidity']
    feelsLike=api['current']['feelslike']
        
    #create labels for the respective values
    currDateLabel=Label(root,text='Date: {}'.format(currDate),font=("Helvetica",15),background='#03021c',foreground='#00f8fc')
    currTimeLabel=Label(root,text="Time: {}".format(currTime),font=('Helvetica',15),background='#03021c',foreground='#00f8fc')
        
    cityLabel=Label(root,text='{}'.format(city),font=("Times New Roman",25,BOLD),background='#03021c',foreground='#00f8fc')
    stateLabel=Label(root,text="{}".format(state),font=("Times New Roman",25,BOLD),background='#03021c',foreground='#00f8fc')
    countryLabel=Label(root,text="{}".format(country),font=("Times New Roman",25,BOLD),background='#03021c',foreground='#00f8fc')
    
    tempLabel=Label(root,text='{}'.format(temperature),font=("Helvetica",20,BOLD),background='#03021c',foreground='#00f8fc')
    feelsLikeLabel=Label(root,text="Feels like {}".format(feelsLike),font=("Helvetica",10,BOLD),
                         background='#03021c',foreground='#00f8fc')
    
    uvIndexLabel=Label(root,text="{}\nUV Index".format(uvIndex),
                       font=("Helvetica",10,BOLD),foreground=uvIndexColors[uvIndex][1],background='#03021c')
    
    weatherDescLabel=Label(root,text='\n{}'.format(weather_desc),
                           font=("Helvetica",10,BOLD),background='#03021c',foreground='#00f8fc')
    
    humidityLabel=Label(root,text="{}\nHumidity".format(humidity),
                        font=('Helvetica',10,BOLD),background='#03021c',foreground='#00f8fc')

    #put the labels into grid
    cityLabel.grid(row=1,column=0,columnspan=2,padx=(20,20),pady=(20,0))
    stateLabel.grid(row=2,column=0,columnspan=2,padx=(20,20))
    countryLabel.grid(row=3,column=0,columnspan=2,padx=(20,20))

    currDateLabel.grid(row=4,column=0,padx=(20,20))
    currTimeLabel.grid(row=5,column=0,padx=(20,20),pady=(0,20))
        

    tempLabel.grid(row=1,column=5,pady=(20,0))
    feelsLikeLabel.grid(row=2,column=5)
    uvIndexLabel.grid(row=4,column=3,columnspan=2)
    weatherDescLabel.grid(row=4,column=5,columnspan=2)
    humidityLabel.grid(row=4,column=7,columnspan=2,padx=(0,20))
    
    
except Exception as e:
    api="Error"
    print(e)

root.mainloop()