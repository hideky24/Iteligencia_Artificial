
import time
from datetime import date
from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys



driverPath = "C://Users//User//Dropbox//Script//chromedriver.exe"
url = "https://crm.spapps.eafit.edu.co/index.php?action=Login&module=Users&login_module=Leads&login_action=index"




options = webdriver.ChromeOptions()
#options.add_argument("--headless")
service = Service(executable_path=driverPath)



driver = webdriver.Chrome(service=service, options=options)
params = {"behavior": "allow", "downloadPath":r"C:\Users\User\Dropbox\INPUT GENERALES\BasesManuales"}
driver.execute_cdp_cmd("Page.setDownloadBehavior", params)
driver.set_window_size(300,524)
driver.implicitly_wait(20)
driver.get(url) 

textUser = "HeinerAcosta"
textPassword = "12345"
inputUser = driver.find_element(by=By.NAME, value="user_name")
inputPassword = driver.find_element(by=By.NAME, value="username_password")
sendButton = driver.find_element(by=By.NAME, value="Login")


inputUser.send_keys(textUser)
inputPassword.send_keys(textPassword)
sendButton.click()


items = driver.find_element(By.XPATH, value="//*[@id='ajaxHeader']/nav/div/div[1]/button")
items.click()
time.sleep(20)
clientes = driver.find_element(By.XPATH, value="//*[@id='mobile_menu']/li[1]/a") 
clientes.click()

#filtroActivo = driver.execute_script(' return document.getElementsByClassName("glyphicon glyphicon-remove::before")[1];')

#driver.execute_script('arguments[0].click();', filtroActivo)

time.sleep(20)
filtro = driver.find_element(By.XPATH, value="//*[@id='pagination']/td/table/tbody/tr/td[1]/ul[3]/li/a") 
filtro.click()
time.sleep(5)
limpiar = driver.find_element(By.XPATH, '//*[@id="search_form_clear_advanced"]')
limpiar.click()
selector = driver.find_element(By.NAME, "date_entered_advanced_range_choice")
selector = Select(selector)
selector.select_by_value("between")
#today = date.today()
#print(today)
desde = "01/10/2022"
hasta = "today"
inputdesde = driver.find_element(by=By.NAME, value="start_range_date_entered_advanced")
inputhasta = driver.find_element(by=By.NAME, value="end_range_date_entered_advanced")
inputdesde.send_keys(desde)
inputhasta.send_keys(hasta)

buscar = driver.find_element(By.XPATH, "//*[@id='search_form_submit_advanced']")
buscar.click()

menu = driver.find_element(By.XPATH, '//*[@id="selectLinkTop"]/li/label/span')
menu.click()

seleccionar = driver.find_element(By.XPATH, '//*[@id="button_select_all_top"]')
seleccionar.click()

menuAccionMasiva = driver.find_element(By.CLASS_NAME, "parent-dropdown-handler")
menuAccionMasiva.click()
exportar = driver.find_element(By.XPATH, "//*[@id='export_listview_top ']")
exportar.click()
print("Descargando archivo")
if os.path.exists(r"C:\Users\User\Dropbox\INPUT GENERALES\BasesManuales\BaseCRMEAFIT_PT4.csv"):
    print("Borrando")
    os.remove(r"C:\Users\User\Dropbox\INPUT GENERALES\BasesManuales\BaseCRMEAFIT_PT4.csv")
while True:
    time.sleep(5)
    if os.path.exists(r"C:\Users\User\Dropbox\INPUT GENERALES\BasesManuales\Clientes potenciales.csv"):
        os.rename(r"C:\Users\User\Dropbox\INPUT GENERALES\BasesManuales\Clientes potenciales.csv", r"C:\Users\User\Dropbox\INPUT GENERALES\BasesManuales\BaseCRMEAFIT_PT4.csv")
        break
time.sleep(5)
if os.path.exists(r"C:\Users\User\Dropbox\INPUT GENERALES\BasesManuales\Clientes potenciales.csv"):
    os.remove(r"C:\Users\User\Dropbox\INPUT GENERALES\BasesManuales\Clientes potenciales.csv")

print("Ya termine")
