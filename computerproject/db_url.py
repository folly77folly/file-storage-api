import dj_database_url
from decouple import config

def url_generator(DEBUG, url):
    if DEBUG == False:
        return {"default" :{
            "ENGINE": "djongo",
            "HOST": url
        }}
    else:
        return{"default" :{
            "ENGINE": "djongo",
            "NAME": "computerapi",
            "HOST": "localhost",
            "PORT":27017
        }}