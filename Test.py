from Driver.WebDriver import *
import time

from Driver.Select import *


key = Keys()
driver = WebDriver("Chrome")
driver.start_browser()
driver.navigate("http://newtours.demoaut.com/mercurywelcome.php")
#driver.navigate("http://google.com")
#driver.navigate(os.getcwd()+"/Test_site/index.html")
driver.max_browser()
driver.min_browser()
driver.full_screen_browser()
search_user = driver.locate_element("name","userName")
search_password = driver.locate_element("name","password")
driver.write(search_user,"admin"+key.get_key('SEMICOLON'))
time.sleep(2)
driver.write(search_password,"admin")


login_button = driver.locate_element("name","login")
driver.click(login_button)

link = driver.locate_element("xpath","/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[2]")
driver.click(link)

combo = driver.locate_element("name","country")
comboSelector = Select(combo,driver)
comboSelector.select_by_text("ALBANIA")
time.sleep(2)
comboSelector.select_by_index(2)
time.sleep(2)
driver.get_status()
driver.close_browser()
#driver.end_session()
#driver.end_driver()

