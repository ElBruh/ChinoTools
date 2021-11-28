from bs4 import BeautifulSoup
import requests

url = "https://www.officeally.com/slogin.aspx"
DataURL = "https://www.officeally.com/secure_oa.asp?GOTO=ClaimFix&TaskAction=Edit&Mode=Insert&FromIR=True&AllowCorrectedClaim=True&ClaimID=2480336207"
headers = {
             'user-agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0'
}
LoginData = {
             "Login1_UserName" : "romaminc",
             "Login1_Password": "Advancemedical$2021!^!",
             'Login1_LoginButton': 'Login',
             'Login1_AccessReason': 'user',
             "__RequestVerificatoinToken": 'DNZqp3ynfv4zN6gd_oktLtilTGnzg6k5wzhEc0KkzoRE67VPPIiowowjd86e7_3_7UD9Lf0pGtZ4S5JmuhY19CCQxPZ6lkF1W164mVq8uZqlUmeU04MXH6dGBreKXUY9Ppis6Q2'
}

with requests.Session() as s:
    page = s.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    LoginData['__VIEWSTATE'] = soup.find('input', attrs={'id': '__VIEWSTATE'})['value']
    LoginData['__VIEWSTATEGENERATOR'] = soup.find('input', attrs={'id': '__VIEWSTATEGENERATOR'})['value']
    LoginData['__EVENTVALIDATION'] = soup.find('input', attrs={'id': '__EVENTVALIDATION'})['value']
    
    r = s.post(url, data=LoginData, headers = headers)

    mainPage = s.get(DataURL)
    mySoup = BeautifulSoup(mainPage.content)
    print(mySoup)

    #print(LoginData)
#login_url = "https://www.officeally.com/slogin.aspx"
#result = session_requests.get(login_url)
#tree = html.fromstring(result.text)
#print(tree)
#authenticity_token = list(set(tree.xpath("//input[@name='__RequestVerificationToken']/@value")))[0]

#payload = {
#    "Login1_UserName" : "romaminc",
#    "Login1_Password": "Advancemedical$2021!^!",
#    "__RequestVerificationToken": "DNZqp3ynfv4zN6gd_oktLtilTGnzg6k5wzhEc0KkzoRE67VPPIiowowjd86e7_3_7UD9Lf0pGtZ4S5JmuhY19CCQxPZ6lkF1W164mVq8uZqlUmeU04MXH6dGBreKXUY9Ppis6Q2"
#}

#URL = "https://www.officeally.com/secure_oa.asp?GOTO=ClaimFix&TaskAction=Edit&Mode=Insert&FromIR=True&AllowCorrectedClaim=True&ClaimID=2480336207"
#page = requests.get(URL)

#print(page.text)
#print(authenticity_token)
