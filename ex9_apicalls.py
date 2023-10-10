import requests
from dotenv import load_dotenv
import os 

load_dotenv() 
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def CountryNews():
    
    country_name = input("Enter the name of the country you want new from type : \n us : United States \n in : India  \n")
    url = (f'https://newsapi.org/v2/top-headlines?country={country_name}&from=2023-10-08&to=2023-10-08&sortBy=popularity&apiKey={NEWS_API_KEY}')
    response = requests.get(url)
    data = response.json()
    
    try : 
          useful_data = []
          counter = 0
          for datapoint in data['articles'] :
           counter+=1

           if counter <= 10 :
            useful_data.append(datapoint['url'])
            #stores the url for top 10 news in the file News.txt
            with open("News.txt",'a') as file :
              file.write(datapoint['url']+"\n")

           else :
             break
    except :
         print(data)
    
    print(useful_data)

#  function to get the top 10 news from the news api
def AllTop10News():
    
    url = (f'https://newsapi.org/v2/everything?country=us&from=2023-10-08&to=2023-10-08&sortBy=popularity&apiKey={NEWS_API_KEY}')
    response = requests.get(url)
    data = response.json()
    useful_data = []
    
    counter = 0
    for datapoint in data['articles'] :
         counter+=1

         if counter <= 10 :
          useful_data.append(datapoint['url'])
          #stores the url for top 10 news in the file News.txt
          with open("News.txt",'w') as file :
              file.write(datapoint['url']+"\n")

         else :
             break
    
    print(useful_data)


# Function for the News 
def News(): 
    
    user_input = int(input("Enter 1 to get latest news For specfic News Enter 2 : "))
   
    if user_input == 1:
        AllTop10News()
    else :
        CountryNews()


News()

    



