import requests
import json
from tkinter import *

#Initiate window
window = Tk()
window.title('Covid-19 Information')
window.geometry('600x100')
window.iconbitmap(r'C:\Users\example\OneDrive\Desktop\covidicon2.ico')


def get_country_info():
    url = "https://api.covid19api.com/summary"
    response = requests.request("GET", url)

    #DATA from json
    data = json.loads(response.text)

    #Get dynamic country index
    searchCountry = text.get()

    #Get input country index
    def get_country_index(country):
        for index,item in enumerate(data['Countries']):
            if item['Country'] == country:
                return index

    countryId = get_country_index(searchCountry)

    newConfirmed = data['Countries'][countryId]['NewConfirmed']
    totalConfirmed = data['Countries'][countryId]['TotalConfirmed']

    covid_msg = f'Last number of new confirmed cases in {searchCountry} are: {newConfirmed}. \nThe total cases in {searchCountry} are: {totalConfirmed}.'
    output_text.set(covid_msg)

label = Label(window, text='Enter Country:')
label.grid(column=0, row=0, sticky=W)

#User input
text = Entry(window, width=30)
text.grid(column=1, row=0, sticky=E)

#create button
button = Button(window, text='Get Information', command=get_country_info)
button.grid(column=2, row=0, sticky=E)

#Display output
output_text = StringVar()
label_output = Label(window, textvariable=output_text)
label_output.grid(column=0, columnspan=4, row=2, sticky=W)

window.mainloop()
