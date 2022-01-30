# wethenewPricesChecker
Check the sneakers selected price on wethenew

# how to use it ?
install the selenium library:
```
pip install selenium
```
Then download the Chrome webdriver at: https://chromedriver.chromium.org/downloads and locate it in the main.py at (line 25 and 33) 
```
driver = webdriver.Chrome(executable_path="chromedriver",)
```
replace "chromedriver" by your path (is a little bit complicated if your in macOs: "https://www.edureka.co/community/52315/how-to-setup-chrome-driver-with-selenium-on-macos")

After you can run the main.py and open "http://localhost:5000/" in your favorite browser. 

If you want use another browser than chrome, you must change a little a bit the code. 

# what it does

After run the main.py and open "http://localhost:5000/" in your browser, it will open popUp. Don't touch it. In this popUp, It will open the wethenew page, copy the price in a variable and close automaticaly the browser. Don't close it. After open this two popUp, it gonna just load the website. 

# Website's plan

In the top of this basic website there is a simple slider with img come from stocX, if you click in an image, it will open the link in questions. 

Under you can see a card with an image of the shoes and, under, the price. 
