from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

comUrl1 = "https://finance.yahoo.com/quote/BMW.DE?p=BMW.DE"
comUrl2 = "https://finance.yahoo.com/quote/SAP?p=SAP&.tsrc=fin-srch"

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get(comUrl1)
time.sleep(5)

driver.maximize_window()
driver.implicitly_wait(10)
i = 0
try:
    driver.find_element_by_name("agree").click()
    time.sleep(5)
    while(i < 2):
        if i == 1:
            driver.get(comUrl2)
            time.sleep(5)
        mCap = driver.find_element_by_xpath('//*[@id="quote-summary"]/div[2]/table/tbody/tr[1]/td[2]').text
        print("\n Market Cap : "+mCap)

        Volume = driver.find_element_by_xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[2]').text
        print("\n Volume : "+Volume)

        driver.find_element_by_xpath('//*[@id="quote-nav"]/ul/li[7]/a').click()
        time.sleep(7)


        totRev2020 = driver.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[3]/div[1]/div/div[2]/div[1]/div[1]/div[3]').text
        totRev2019 = driver.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[3]/div[1]/div/div[2]/div[1]/div[1]/div[4]').text
        totRev2018 = driver.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[3]/div[1]/div/div[2]/div[1]/div[1]/div[5]').text
        totRev2017 = driver.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[3]/div[1]/div/div[2]/div[1]/div[1]/div[6]').text
        grossProfit2020 = driver.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[3]').text
        grossProfit2019 = driver.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[4]').text
        grossProfit2018 = driver.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[5]').text
        grossProfit2017 = driver.find_element_by_xpath('//*[@id="Col1-1-Financials-Proxy"]/section/div[3]/div[1]/div/div[2]/div[3]/div[1]/div[6]').text

        print("\n TotRev2020 : "+totRev2020 + "\n TotRev2019 : "+totRev2019 + "\n TotRev2018 : "+totRev2018 + "\n TotRev2017 : "+totRev2017) 
        print("\n grossProfit2020 : "+grossProfit2020 + "\n grossProfit2019 : "+grossProfit2019 + "\n grossProfit2018 : "+grossProfit2018 + "grossProfit2017 : "+grossProfit2017) 

        time.sleep(5)

        driver.find_element_by_xpath('//*[@id="quote-nav"]/ul/li[11]/a').click()
        time.sleep(5)
        
        totESG = driver.find_element_by_xpath('//*[@id="Col1-0-Sustainability-Proxy"]/section/div[1]/div/div[1]/div/div[2]/div[1]').text
        print("\nTotal ESG : "+totESG)

        eScore = driver.find_element_by_xpath('//*[@id="Col1-0-Sustainability-Proxy"]/section/div[1]/div/div[2]/div/div[2]/div[1]').text
        sScore = driver.find_element_by_xpath('//*[@id="Col1-0-Sustainability-Proxy"]/section/div[1]/div/div[3]/div/div[2]/div[1]').text
        gScore = driver.find_element_by_xpath('//*[@id="Col1-0-Sustainability-Proxy"]/section/div[1]/div/div[4]/div/div[2]/div[1]').text
        esgLevel = driver.find_element_by_xpath('//*[@id="Col1-0-Sustainability-Proxy"]/section/div[1]/div/div[1]/div/div[3]/div/span').text
        esgPercent = driver.find_element_by_xpath('//*[@id="Col1-0-Sustainability-Proxy"]/section/div[1]/div/div[1]/div/div[2]/div[2]/span/span').text
    
        print("\n Enviornment score :"+eScore+"\n Social score :"+ sScore +"\n Governance Score : "+gScore+ "\n Status :"+esgLevel+"\n Esg Percentile :"+esgPercent)

        # Product Involvements area
        time.sleep(10)

        tabel_id = driver.find_element_by_xpath('//*[@id="Col2-3-InvolvementAreas-Proxy"]/section/table')
        proAct = tabel_id.text

        all = proAct.split()
        NoIndex = []
        YesIndex = []
        allIndex = []
        factor = []
        tempList = []
        tempstr = ""
        start = 5
        lastIndex = "Yes"
        for index,each in enumerate(all):
            
            if each == 'No':
                NoIndex.append(index)
                allIndex.append(index)
                tempList = all[start:index]
                tempstr = ' '.join(tempList)
                factor.append(tempstr)
                tempstr =  ''
                tempList = []
                lastIndex = 'No'
                start = index
            

            if each == "Yes" :
                YesIndex.append(index)
                allIndex.append(index)
                tempList = all[start:index]
                tempstr = ' '.join(tempList)
                factor.append(tempstr)
                tempstr =  ''
                tempList = []
                lastIndex = 'Yes'
                start = index

        factor.append(lastIndex)

        keyList = []
        valList = []
        for ff in factor:
            if not 'No' in ff and not 'Yes' in ff:
                keyList.append(ff)
            elif 'No' in ff:
                valList.append("No")
                ff = ff[3:]
                keyList.append(ff)
            elif 'Yes' in ff:
                valList.append("Yes")
                ff = ff[4:]
                keyList.append(ff)
            
        keyList.pop()  

        zip_iterator = zip(keyList,valList)
        myDict = dict(zip_iterator)

        print(myDict)
        i = i+1

            


     
except:
    driver.quit()

def acceptCookies():
    driver.find_element_by_name("agree").click()
    time.sleep(5)
