from distutils.log import debug
from flask import Flask, render_template, redirect
from selenium.webdriver.chrome.options import Options
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

app = Flask(__name__)

picFolder = os.path.join("static","pics")
styleFolder = os.path.join("static","styles")
jsFolder = os.path.join("static","js")

app.config["UPLOAD_FOLDER"] = picFolder
app.config["STYLE_FOLDER"] = styleFolder
app.config["JS_FOLDER"] = jsFolder

def reditection():
    return render_template("test.html")

@app.route('/')
def index():
    driver = webdriver.Chrome(executable_path="chromedriver",)
    driver.get("https://wethenew.com/products/air-jordan-1-high-zoom-air-cmft-easter?variant=39355247558765")
    acceptCookies = driver.find_element_by_id("didomi-notice-agree-button").click()
    findPrice = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div[1]/div[2]/p[2]/span[2]/span/span')
    priceInner = findPrice.get_attribute("innerHTML")
    jordanOneEasterPrice = priceInner.strip()
    driver.close()

    driver = webdriver.Chrome(executable_path="chromedriver")
    driver.get("https://wethenew.com/products/adidas-yeezy-boost-350-v2-mono-mist?variant=39410683904109")
    acceptCookies = driver.find_element_by_id("didomi-notice-agree-button").click()
    #time.sleep(10)
    #webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    findPrice = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div[1]/div[2]/p[2]/span[2]/span/span')
    priceInner = findPrice.get_attribute("innerHTML")
    yeezy250MonoMistPrice = priceInner.strip()
    driver.close()

    style = os.path.join(app.config["STYLE_FOLDER"], 'style.css')
    js = os.path.join(app.config["JS_FOLDER"], "app.js")
    firstPic = os.path.join(app.config["UPLOAD_FOLDER"], "slider1.jpg")
    secondPic = os.path.join(app.config["UPLOAD_FOLDER"], "slider2.jpg")
    thirdPic = os.path.join(app.config["UPLOAD_FOLDER"], "slider3.jpg")
    jordanOneEasterPic = os.path.join(app.config["UPLOAD_FOLDER"], "jordanOneEaster.jpg")
    yeezy350MonoMistPic = os.path.join(app.config["UPLOAD_FOLDER"], "yeezy350MonoMist.jpg")
    return render_template("index.html",priceJordan=jordanOneEasterPrice,style=style,sliderImg=firstPic,jordanOneEaster=jordanOneEasterPic,yeezy350MonoMist=yeezy350MonoMistPic,priceYeezy250MonoMist=yeezy250MonoMistPrice,secondSlider=secondPic,thirdSlider=thirdPic,js=js)

if __name__ == "__main__":
    app.run(debug=True)