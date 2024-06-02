import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("7033446230:AAESwYfEjAzwi-oQsPbm3881M4kf23-8OFM", "")
    API_ID = int(os.environ.get("22946135", ))
    API_HASH = os.environ.get("93e1b0c387cabe34a3ccfa1724ae8527", "")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("-1001948647139", "")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
