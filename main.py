#!/usr/bin/python3
from bs4 import BeautifulSoup
import requests
import json

from requests.sessions import session
url = "https://forms.wayne.edu/covid-19-screening/"
file = open("login.txt")
fileArr = file.read().splitlines() 

accessid = fileArr[0];pwd = fileArr[1];phonenumber = fileArr[2]

def login():
    loginform = {"accessid": accessid, "passwd": pwd, "submit": "Login"}
    auth = requests.post(url,
                         headers={'User-Agent': 'Mozilla/5.0'}, data=loginform)
    soup = BeautifulSoup(auth.text, "html.parser")
    print("Logging in...")
    tags = soup.find_all("form")
    ourForm = None
    # print(response.text)
    for tag in tags:
        if tag.get("method") == "post":
            ourForm = str(tag.get("id")).replace("form-", "")
    return {"session": dict(auth.cookies)["WSUMSESSIONID"], "formid": ourForm}

def form(logincreds):
    payload = {"f_253006": phonenumber,
               "f_251741": "No",
               "f_251742": "No",
               "f_255927": "No",
               "f_253229[0]": "191",
               "f_253229[1]": "637",
               "f_253229[2]": "217",
               "f_253229[3]": "594",
               "f_253229[4]": "491",
               "f_253229[5]": "070",
               "f_253229[6]": "071",
               "f_253229[7]": "041",
               "f_253229[8]": "067",
               "f_253229[9]": "066",
               "f_253229[10]": "195",
               "f_253229[11]": "207",
               "f_253229[12]": "199",
               "f_253229[13]": "083",
               "f_253229[14]": "202",
               "f_253229[15]": "503",
               "f_253229[16]": "489",
               "f_253229[17]": "062",
               "f_253229[18]": "556",
               "f_253229[19]": "042",
               "f_253229[20]": "122",
               "f_253229[21]": "603",
               "f_253229[22]": "040",
               "f_253229[23]": "655",
               "f_253229[24]": "724",
               "f_253229[25]": "064",
               "f_253229[26]": "059",
               "f_253229[27]": "169",
               "f_253229[28]": "089",
               "f_253229[29]": "620",
               "f_253229[30]": "175",
               "f_253229[31]": "609",
               "f_253229[32]": "1002",
               "f_253229[33]": "1001",
               "f_253229[34]": "136",
               "f_253229[35]": "007",
               "f_253229[36]": "598",
               "f_253229[37]": "621",
               "f_253229[38]": "048",
               "f_253229[39]": "039",
               "f_253229[40]": "193",
               "f_253229[41]": "592",
               "f_253229[42]": "023",
               "f_253229[43]": "140",
               "f_253229[44]": "629",
               "f_253229[45]": "167",
               "f_253229[46]": "090",
               "f_253229[47]": "060",
               "f_253229[48]": "130",
               "f_253229[49]": "511",
               "f_253229[50]": "150",
               "f_253229[51]": "634",
               "f_253229[52]": "618",
               "f_253229[53]": "097",
               "f_253229[54]": "189",
               "f_253229[55]": "623",
               "f_253229[56]": "212",
               "f_253229[57]": "211",
               "f_253229[58]": "033",
               "f_253229[59]": "509",
               "f_253229[60]": "635",
               "f_253229[61]": "726",
               "f_253229[62]": "611",
               "f_253229[63]": "053",
               "f_253229[64]": "046",
               "f_253229[65]": "049",
               "f_253229[66]": "104",
               "f_253229[67]": "006",
               "f_253229[68]": "017",
               "f_253229[69]": "188",
               "f_253229[70]": "591",
               "f_253229[71]": "155",
               "f_253229[72]": "166",
               "f_253229[73]": "080",
               "f_253229[74]": "608",
               "f_253229[75]": "043",
               "f_253229[76]": "025",
               "f_253229[77]": "065",
               "f_253229[78]": "091",
               "f_253229[79]": "001",
               "f_253229[80]": "051",
               "f_253229[81]": "056",
               "f_253229[82]": "498",
               "f_253229[83]": "613",
               "f_253229[84]": "045",
               "f_253229[85]": "088",
               "f_253229[86]": "595",
               "f_253229[87]": "536",
               "f_253229[88]": "003",
               "f_253229[89]": "203",
               "f_253229[90]": "022",
               "f_253229[91]": "027",
               "f_253229[92]": "499",
               "f_253229[93]": "028",
               "f_253229[94]": "624",
               "f_253229[95]": "617",
               "f_253229[96]": "038",
               "f_253229[97]": "565",
               "f_253229[98]": "005",
               "f_253229[99]": "612",
               "f_253229[100]": "050",
               "f_253229[101]": "068",
               "f_253229[102]": "510",
               "f_253229[103]": "063",
               "f_253229[104]": "101",
               "f_253229[105]": "156",
               "f_253229[106]": "078",
               "f_253229[107]": "016",
               "f_253229[108]": "008",
               "f_253229[109]": "034",
               "f_253229[110]": "535",
               "f_253229[111]": "209",
               "f_253229[112]": "074",
               "f_253229[113]": "504",
               "f_253229[114]": "505",
               "f_253229[115]": "633",
               "f_253229[116]": "079",
               "f_253229[117]": "127",
               "f_253229[118]": "096",
               "f_253229[119]": "614",
               "f_253229[120]": "507",
               "f_253229[121]": "643",
               "f_253229[122]": "036",
               "f_253229[123]": "082",
               "f_253229[124]": "585",
               "f_253229[125]": "085",
               "f_253229[126]": "727",
               "f_253229[127]": "728",
               "f_253229[128]": "729",
               "f_253229[129]": "730",
               "f_253229[130]": "115",
               'formy-save': logincreds["formid"]}
    files = [

    ]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'Cookie': f'WSUMSESSIONID={logincreds["session"]}'
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)
    """ if "You have reached a page that requires authentication, please enter your Wayne State AccessID and password." in response.text:
        print("FAILED LOGIN") # this cond doesnt work the way i thought it did...
        return """
    soup = BeautifulSoup(response.text, "html.parser")
    print("Submitting Form...")
    errors = soup.find_all(id="form-errors")
    if len(errors) > 0:
        print([err.getText() for err in errors])
        print([err.getText()
              for err in soup.find_all("div", {"class": "form-errors"})])
    else:
        imgs = soup.find_all("img")
        print([(img["src"] if "https://chart.apis.google.com" in img['src'] else None) for img in imgs])
    print("SUCCESS, check your school email in a couple of mins..." if len(errors) < 1 else "FAILED")


if __name__ == "__main__":
    form(login())
    file.close()
