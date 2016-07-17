from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import StringIO

resp = requests.get("http://www.bing.com")
soup = BeautifulSoup(resp.text, "html.parser")
instance = soup.find_all("script", {"type": "text/javascript"})
for i in instance:
    jsContent = i.text
    if "g_img={url:" in jsContent:
        beginIndex = jsContent.find('g_img={url: "') + 13
        endIndex = jsContent.find('jpg', beginIndex) + 3
        imgURL = jsContent[beginIndex:endIndex]
        imgURL = "http://www.bing.com/" + imgURL

resp = requests.get(imgURL)
print type(resp.content)
i = Image.open((resp.content))

