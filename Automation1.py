from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

# import xlsxwriter
from csv import writer
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://recro-team.freshteam.com/")
action = ActionChains(driver)
# workbook = xlsxwriter.Workbook('JavaRemote.xlsx')

# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
# worksheet = workbook.add_worksheet()
# worksheet.write('A1', 'Name')
# worksheet.write('B1', 'Email')
# worksheet.write('C1', 'Mobile')

# Use the worksheet object to write
# data via the write() method.

def freshteam():
     driver.maximize_window()  # For maximizing window
     driver.implicitly_wait(20)
     print("debugging #1 entering username and password")
     driver.find_element(By.ID, 'username').send_keys("ismail@recro.io")
     driver.find_element(By.ID, "password").send_keys("Initial@123")
     driver.find_element(By.CLASS_NAME, "css-o1ejds").click()
     driver.implicitly_wait(20)
     driver.find_element(By.ID, "ember216").click()
     driver.implicitly_wait(15)
     myDivs = driver.find_elements(By.CLASS_NAME, "col-inside")
     print("Find my anchor", len(myDivs))
     # print("what is in titles", myDivs.find_element(By.LINK_TEXT, '/hire/jobs/4000013308/applicants'))
     pushNewpage = False
     for myitem in myDivs:
          myancor = myitem.find_element(By.TAG_NAME,'a')
          if "/hire/jobs/4000013308/applicants" in myancor.get_attribute("href"):
               print("Bingo click this now")
               myancor.click()
               pushNewpage = True
               break

     if pushNewpage:
          # jobDetailPage()
          time.sleep(20)
          freshParsing()
          # getNextPage()





def jobDetailPage():
     time.sleep(10)
     # filters = driver.find_elements(By.CLASS_NAME, "list-inline")
     # allCandfilter = filters[0]
     # allCandfilter.find_element(By.TAG_NAME, 'a').click()
     print("Filter open and wait 5 econds")
     # time.sleep(3)
     # parsePages()

     # dropdownview = allCandfilter.find_element(By.CLASS_NAME, "ember-bootstrap-dropdown-bs3-popper")
     # h5tagList = dropdownview.find_elements(By.TAG_NAME, "h5")
     # print("h5tagList", h5tagList)
     # for tag in h5tagList:
     #      if tag.get_attribute("data-test-id") in 'section-followed_candidates':
     #           print("Bingo******* got the h5")
     #           h5tag = tag.get_attribute("data-test-id")
     #           h5tag.click()
     # divtagList = dropdownview.find_elements(By.TAG_NAME, "div")
     # print("divtagList", divtagList)
     # for tag in range(0,len(divtagList)):
     #      print("wht is the tag", tag)
     #      if tag == 1:
     #           print("Bingo******* got the div we wanted")
     #           h5tag = divtagList[tag].find_element(By.ID, "filter-All")
     #           h5tag.click()


def parsePages():
     print("Parsing the data method")
     xpathEle = driver.find_element(By.XPATH, "//table/tr[contains(@class, 'candidate-list-item')]/td[@class = 'onhover-active']")
     # a.move_to_element(xpathEle).perform()
     # print("xpathEle",xpathEle)



     rowList = driver.find_elements(By.CLASS_NAME, "candidate-list-item")
     for row in rowList:
          tdrow = row.find_elements(By.CLASS_NAME, "onhover-active")[1]
          divList = tdrow.find_elements(By.TAG_NAME, "div")
          action.move_to_element(tdrow).perform()
          divele = tdrow.find_element(By.XPATH, "//table/tr[contains(@class, 'candidate-list-item')]/td[@class = 'onhover-active']/div[@class = 'popover fade in right']]")
          print("divele***", divele.text)
          # for divitem in divList:
          #
          #      temListDiv = divitem.find_elements(By.TAG_NAME,"div")
          #      for ohveritem in temListDiv:
          #           # print("ohveritemohveritem=",ohveritem.get_attribute('innerHTML'),"\n")
          #           mobileElement = divitem.find_element(By.CLASS_NAME, "vertical-align")
          #           print("mobile = ", ohveritem.text, ohveritem.tag_name, '==', ohveritem.parent, "==")
          #      # print("divitem*********",)
          #
          #      break
          print("--------*********---------\n")
          break



def freshParsing():
     time.sleep(10)
     trList = driver.find_elements(By.XPATH, "//table/tr[contains(@class, 'candidate-list-item')]/td[@class = 'onhover-active']")
     scrollItem = driver.find_element(By.CLASS_NAME, "toggle-all-wrap ")
     # getNextPage()

     for trItem in trList:
          action.move_to_element(trItem).perform()
          popoverDiv = trItem.find_elements(By.XPATH, "//div[@class = 'popover fade in right']")
          if len(popoverDiv) < 1:
               continue
          firstDiv = popoverDiv[0]
          nameDiv = firstDiv.find_element(By.XPATH, "//div[@class = 'popover-content contact-popover']/div[@class='semi-bold ellipsis']")
          print("Name = ",nameDiv.text)
          # compDiv = firstDiv.find_element(By.XPATH,
          #                                 "//div[@class = 'popover-content contact-popover']/p")
          # print("compName = ", compDiv.text)

          emailDiv = firstDiv.find_element(By.XPATH,
                                          "//div[@class = 'popover-content contact-popover']/div[@class='btn-full-width ellipsis'][1]")
          print("emailDiv = ", emailDiv.text)

          myinfoList = [nameDiv.text, emailDiv.text]

          if check_exists_by_xpath("//div[@class = 'popover-content contact-popover']/div[@class='btn-full-width ellipsis'][2]"):
               mobileDiv = firstDiv.find_element(By.XPATH,
                                           "//div[@class = 'popover-content contact-popover']/div[@class='btn-full-width ellipsis'][2]")
               myinfoList.append(mobileDiv.text)

          # print("mobileDiv = ", mobileDiv.text)
          # worksheet.write('A1', nameDiv.text)
          # worksheet.write('B1', emailDiv.text)
          # worksheet.write('C1', mobileDiv.text)
          with open('JavaRemote.csv', 'a') as f_object:

               # Pass this file object to csv.writer()
               # and get a writer object
               writer_object = writer(f_object)

               # Pass the list as an argument into
               # the writerow()
               writer_object.writerow(myinfoList)

               # Close the file object
               f_object.close()
          action.key_down(Keys.DOWN).perform()
          action.key_down(Keys.DOWN).perform()
          # action.key_down(Keys.DOWN).perform()
          # driver.execute_script("window.scrollTo(0,document.body.scrollHeight + 300)")
          time.sleep(1)
          print("---------*********------------\n")

     getNextPage()



def getNextPage():
     time.sleep(2)
     print("Go to next page ")
     paginationDiv = driver.find_element(By.ID,"candidatePaginate")
     ulItem = paginationDiv.find_element(By.XPATH, "//ul")
     # print("ul items ", ulItem.get_attribute("innerHTML"))
     currentPage = ulItem.find_element(By.XPATH, "//li[@class='active']")
     print("currentPAge", currentPage.text, currentPage.get_attribute('class'))
     liItems = ulItem.find_elements(By.XPATH, "//li")
     nextPAgeObj = driver.find_element(By.XPATH,"//div[@id='candidatePaginate']/ul/li/a[@aria-label='Next Page']")

     print("nextPAgeObj",nextPAgeObj.text,"----",nextPAgeObj.tag_name)
     nextPAgeObj.click()
     time.sleep(5)
     freshParsing()





def check_exists_by_xpath(xpath):
    try:
        driver.find_element(By.XPATH,xpath)
    except NoSuchElementException:
        return False
    return True


freshteam()

#Freshteam parsing done




