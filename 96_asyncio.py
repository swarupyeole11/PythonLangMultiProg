import asyncio
from concurrent.futures import ThreadPoolExecutor
import requests

def image_download(url):

    # the split function returs the splited parts in form of list of values 
    value = url.split('/')[-1]
    response = requests.get(url)
    if response.status_code == 200:
      with open(f"/home/swarupyeole11/Desktop/{value}", 'wb') as f:
        f.write(response.content)


def image_download_using_threads():

    with ThreadPoolExecutor(max_workers=20) as executor:
      urls = ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPG1K5nSt13QLTyxkwGmFs10MHHchxr50IzA&usqp=CAU","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQMseA7BYmazbD2d3HXVHaEAmiYP-y74qC_rXflyy2fxA&s"]
      executor.map(image_download,urls)



    