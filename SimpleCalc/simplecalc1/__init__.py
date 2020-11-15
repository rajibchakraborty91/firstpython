from selenium import webdriver
import datetime


#browserdriver = webdriver.Chrome(executable_path=r"D:\Java Documents\chromedriver_win32\Updated\chromedriver.exe") 

#browserdriver.get("https://www.google.com")


#browserdriver.maximize_window()

#browserdriver.close()


for i in range(1,10,3):
    if i==5:
        print("number",i)
    else:
        print("nothing",i)

x=datetime.datetime.now()

print(x.strftime("%B"))

y = datetime.date.today()

print(y.weekday())




