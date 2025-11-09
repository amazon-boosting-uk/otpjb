import requests,json,time,os

BOLD = "\033[1m"
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
D = "\033[0m"





BIN_ID = "68ce938743b1c97be9493c68"
API_KEY = "$2a$10$UFSeZeyc10fKX8SlSZ8wCOnfNpu7hd87.zlRgbHSOClRVZ9R7U0b6"

def fetch_data():
    """
    Fetch token and number from JSONBin.
    Returns a tuple (token, number) or (None, None) if failed.
    """
    url = f"https://api.jsonbin.io/v3/b/{BIN_ID}/latest"
    headers = {"X-Master-Key": API_KEY}

    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        record = r.json()["record"]
        return record.get("token"), record.get("number")
    return None, None


# Example usage


def main():
    os.system("clear")
    token, number = fetch_data()
    i = 1
    print(f"\n{BOLD}{B} THIS NUMBER WILL BE ADDED >> {G}{number}{D}\n")

    while True:
        token, number = fetch_data()
        print("\n\n")
        input(f"{BOLD}{Y} PRESS ENTER TO SEND {D}")
        headers = {
            'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'Authorization': f'Bearer {token}',
            'sec-ch-ua-arch': '""',
            'Content-Type': 'application/json',
            'sec-ch-ua-full-version': '"139.0.7339.0"',
            'Accept': 'application/json, text/plain, */*',
            'sec-ch-ua-platform-version': '"14.0.0"',
            'Referer': 'https://jeetbuzz66.me/bd/en/member/profile/info/verify-phone',
            'X-Internal-Request': '61405202',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
            'sec-ch-ua-full-version-list': '"Chromium";v="139.0.7339.0", "Not;A=Brand";v="99.0.0.0"',
            'sec-ch-ua-bitness': '""',
            'sec-ch-ua-model': '"LE2101"',
            'sec-ch-ua-platform': '"Android"',
        }

        json_data = {
            'languageTypeId': 1,
            'currencyTypeId': 8,
            'contactTypeId': 2,
            'domain': 'https://jeetbuzz66.me',
            'receiver': number,
            'callingCode': '880',}
        response = requests.post('https://jeetbuzz66.me/api/wv/v1/user/getVerifyCodeByContactType', headers=headers, json=json_data).json()

        api_status = response.get("status")
        msg = response.get("message")
        print(msg)
        print(f"{BOLD}{B} ATTEMPT >> {G}{i}{D}")
        try:

            if api_status == "000000":
                send_noti()
                print(f"\n{BOLD}{G} OTP SENT VALIDITY >> 5 MUNITES{D}")
            elif response.get("status") == "FS9997":
                print(f"{R} THIS NUMBER ALREADY USED!{D}")
                break

            elif "S0001" == api_status:
                print(f"{BOLD}{R} You are logged out. Please Log In and Try Again{D}")
            else:
                print(f" ⚠️ {api_status}")
                print(f"{R} OTP FAILED TO SEND TRY AGAIN !{D}")

        except Exception as e:
            print(e)

        i += 1

def send_noti():
    BOT_TOKEN = "8322244716:AAGHdeW8qxwdz_OcEPR5WsULpaKFWodFqzQ"
    CHAT_ID = "-1002994732538"   # group/channel/user id
    msg = " IG BOOSTING START...."
    requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",json={"chat_id": CHAT_ID, "text": msg,'parse_mode': 'Markdown'}).json()


def switch():
    s = requests.get("https://raw.githubusercontent.com/bajilive-support/verify/refs/heads/main/switch.txt").text
    if "ON" in s:
        pass
    else:
        print(f"\n{BOLD}{R} THIS TOOL HAS DISABLED BY ADMIN!{D}")
        exit(0)



switch()
main()
