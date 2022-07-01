from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from re import T
import smtplib
from time import sleep
from typing_extensions import Self
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pgeocode
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from datetime import datetime
from datetime import date
from datetime import timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from time import sleep
from typing_extensions import Self
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sympy import EX, re
from webdriver_manager.chrome import ChromeDriverManager
import pgeocode
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from datetime import datetime
from datetime import date
from datetime import timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ScrapContacts:
    def __init__(self):
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("--log-level=OFF")
        self.driver = webdriver.Chrome(ChromeDriverManager(
        ).install(), service_log_path='NUL', options=options)

        # self.driver = webdriver.Firefox(
        #     executable_path=GeckoDriverManager().install())<
    def login(self):
        self.driver.get('https://myselogerpro.com/')
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div/div/div[2]/button[2]').click()
        sleep(0.2)
        while True:
            try:
                self.driver.find_element_by_xpath(
                    "/html/body/msp-root/msp-home-layout/div/div/div/div/div/section/login-login/div/div/form/div/div[2]/ui-input/div/label/input").send_keys("1091")
                sleep(0.2)
                passwd = "Lavieestbelle5782,"
                self.driver.find_element_by_xpath(
                    "/html/body/msp-root/msp-home-layout/div/div/div/div/div/section/login-login/div/div/form/div/div[3]/ui-input/div/label/input").send_keys(passwd)
                self.driver.find_element_by_xpath(
                    "/html/body/msp-root/msp-home-layout/div/div/div/div/div/section/login-login/div/div/form/div/div[4]/div/ui-button/div/button").click()
                break
            except Exception:
                pass
        print("Connected")
        sleep(7)

    def geContact(self, retake):
        continueC = True
        msg = ""

        nomi = pgeocode.Nominatim('fr')
        try:
            client = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_name('key.json', [
                'https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']))
            sheet = client.open('selogerall')
            sheet_instance = sheet.get_worksheet(0)
            if not retake:
                sheet_instance.clear()
        except Exception as e:
            pass
        self.driver.get("https://myselogerpro.com/contacts/acquereurs")
        print("Page acquereur")
        while True:
            try:
                # self.driver.execute_script("window.scrollTo(0, 1000)")
                self.driver.find_element_by_xpath(
                    "/html/body/msp-root/msp-app-layout/main/cnt-contacts-outlet/div/cnt-contacts/div/div[2]/ui-page-size-selector/div/span/span[2]").click()
                self.driver.find_element_by_xpath(
                    "/html/body/msp-root/msp-app-layout/main/cnt-contacts-outlet/div/cnt-contacts/div/div[2]/ui-page-size-selector/div/div/div/div[3]").click()
                sleep(15)
                # self.driver.execute_script("window.scrollTo(0, 0)")
                break
            except Exception:
                pass
        if retake:
            while True:
                try:

                    soup2 = BeautifulSoup(self.driver.page_source, "lxml")
                    sheet = int(
                        (len(sheet_instance.get_all_values()) + 1) / 100)
                    num = int(soup2.find("span", {
                        'class': "ui-pagination-page__link ui-pagination-page--current"}).text)

                    if str(num) == str(sheet) or str(sheet) == "0":
                        print("here")
                        break
                    nav = soup2.find("ul", {"class": "ui-pagination"})

                    print(num + 5, sheet)
                    if num + 5 > sheet:
                        if len(nav.find_all("li")) == 11:
                            self.driver.find_element_by_xpath(
                                "/html/body/msp-root/msp-app-layout/main/cnt-contacts-outlet/div/cnt-contacts/div/div[2]/ui-pagination-old/ul/li[10]").click()
                        else:
                            self.driver.find_element_by_xpath(
                                "/html/body/msp-root/msp-app-layout/main/cnt-contacts-outlet/div/cnt-contacts/div/div[2]/ui-pagination-old/ul/li[9]").click()
                        sleep(0.2)
                    else:
                        if len(nav.find_all("li")) == 11:
                            self.driver.find_element_by_xpath(
                                "/html/body/msp-root/msp-app-layout/main/cnt-contacts-outlet/div/cnt-contacts/div/div[2]/ui-pagination-old/ul/li[9]").click()
                        else:
                            self.driver.find_element_by_xpath(
                                "/html/body/msp-root/msp-app-layout/main/cnt-contacts-outlet/div/cnt-contacts/div/div[2]/ui-pagination-old/ul/li[8]").click()

                except Exception as e:
                    print(e)
        input("q")
        i = 1
        sleep(10)
        while True:
            try:
                print("Geting data...")
                dataLst = []
                # self.driver.execute_script(
                #     "window.scrollTo(0, document.body.scrollHeight);")
                # get data
                soup = BeautifulSoup(self.driver.page_source, "lxml")
                table = soup.find(
                    'cdk-table', {'class': 'cdk-table cnt-contacts-list__table cccl-table'})
                # , {'class': 'cdk-row cccl-table__row cccl-table-row cccl-table-row--highlighted cccl-table-row--clickable'})
                lines = table.find_all('cdk-row')
                for el in lines:
                    datestr = el.find(
                        "cdk-cell", {'class': 'cdk-cell cccl-table-row__cell cccl-table-row-cell date cdk-column-date'}).get_text()

                    dt1 = datestr
                    dt_obj = datetime.strptime(dt1, '%d/%m/%Y')
                    namestr = el.find(
                        "cdk-cell", {'class': 'cdk-cell cccl-table-row__cell cccl-table-row-cell cdk-column-name'}).get_text()

                    phonestr = el.find(
                        "cdk-cell", {'class': 'cdk-cell cccl-table-row__cell cccl-table-row-cell cdk-column-phone'}).get_text()

                    bienstr = el.find(
                        "cdk-cell", {'class': 'cdk-cell cccl-table-row__cell cccl-table-row-cell cdk-column-goods'}).get_text()

                    pricestr = el.find(
                        "cdk-cell", {'class': 'cdk-cell cccl-table-row__cell cccl-table-row-cell cdk-column-price'}).get_text()

                    surfacestr = el.find(
                        "cdk-cell", {'class': 'cdk-cell cccl-table-row__cell cccl-table-row-cell cdk-column-area'}).get_text()

                    zipCodestr = el.find(
                        "cdk-cell", {'class': 'cdk-cell cccl-table-row__cell cccl-table-row-cell cdk-column-location'}).get_text()

                    try:
                        city = nomi.query_postal_code(
                            int(zipCodestr)).place_name
                        if "," in city:
                            city = city.split(",")[0]
                    except Exception:
                        city = ""

                    dataLst.append([datestr, namestr, phonestr, bienstr,
                                   pricestr, surfacestr, zipCodestr, city])
                while True:
                    try:
                        entry = sheet_instance.insert_rows(
                            dataLst, len(sheet_instance.get_all_values()) + 1)
                        print("Added")
                        break
                    except Exception:
                        pass
                i += 1
                print("Next Page... - " + str(i))

                nav = soup.find("ul", {"class": "ui-pagination"})
                if len(nav.find_all("li")) == 11:
                    self.driver.find_element_by_xpath(
                        "/html/body/msp-root/msp-app-layout/main/cnt-contacts-outlet/div/cnt-contacts/div/div[2]/ui-pagination-old/ul/li[10]").click()
                else:
                    self.driver.find_element_by_xpath(
                        "/html/body/msp-root/msp-app-layout/main/cnt-contacts-outlet/div/cnt-contacts/div/div[2]/ui-pagination-old/ul/li[9]").click()
                # sleep(30)

                while BeautifulSoup(self.driver.page_source, 'lxml').find("div", {'class': "ui-loader__overlay"}) != None:
                    pass

            except Exception as e:
                print(e)
                print("C'est la")
                # if "id" in str(e) or "chrome not reachable" in str(e):
                #     msg = "c"
                #     break

        return "c"

    def close(self):
        self.driver.close()

    def sendEmail(self):
        try:
            client = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_name('key.json', [
                'https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']))
            sheet = client.open('seloger')
            sheet_instance = sheet.get_worksheet(0)
        except Exception as e:
            pass
        link = "https://docs.google.com/spreadsheets/d/%s" % sheet.id
        try:
            fromaddr = "antigenique@gmail.com"
            toaddr = "mickaelsonego@gmail.com"
            msg = MIMEMultipart()
            msg['Subject'] = "Lien excel se loger"
            msg['From'] = fromaddr
            msg['To'] = toaddr
            html = f"""\
            <html>
            <body>
                <p>
                Bonjour voici le lien du excel se loger: <br>
                <a href="{link}">{link}</a> 
                </p>
            </body>
            </html>
            """
            part1 = MIMEText(html, "html")
            msg.attach(part1)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, '20052005Dh')
            server.sendmail(fromaddr, toaddr, msg.as_string())

        except Exception as e:
            print(e)
            pass


if __name__ == "__main__":

    a = ScrapContacts()
    a.login()
    a.geContact(retake=True)
    # a.close()
