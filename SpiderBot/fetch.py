import requests
import json
import wget
import discord

# limit = 10
# subreddit = "boobs"
# link = f"https://www.reddit.com/r/{subreddit}/top.json?limit={limit}&t=year"


def filter_images(image_urls : list) -> list:
    filtered_list = filter(lambda url: ".png" in url or ".jpg" in url , image_urls)
    return list(filtered_list)

def fetch(subreddit : str , mode : str, limit : int, time : str):
    # mode can be : controversial, best, hot, new, rising, top
    # time can be : hour, day, week, month, year, all
    link = f"https://www.reddit.com/r/{subreddit}/{mode}.json?limit={limit}&t={time}"

    try:
        r = requests.get(url=link, headers = {'User-agent': 'bot 0.1'})
        print(r.status_code, r.reason)
        

        if r.status_code != 200:
            
            raise discord.errors.HTTPException

        data = r.json()
        if mode != "random":
    
            # print(json.dumps(data,indent=4))
            #print(data["data"]["children"][0]["data"]["url"])
            image_urls = []
            length = len(data["data"]["children"])
            for child in range(length):
                image_urls.append(data["data"]["children"][child]["data"]["url"])
            return image_urls #filter_images(image_urls)
        else:
            return data[0]["data"]["children"][0]["data"]["url"]

    except:
        print("Something went wrong, oops")
        return "Cant crawl on a subreddit that  does not exist"

# bobs = fetch(subreddit="boobs",mode="rising",limit=5,time="week")

#print(bobs)