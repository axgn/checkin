import json
import os
import time

import requests
from dotenv import load_dotenv

from getwbi import encWbi, getWbiKeys

load_dotenv()

session = requests.Session()

session.cookies.update(
    {
        "SESSDATA": os.environ.get("BILIBILI_SESSDATA"),
    }
)

params2 = {"csrf": os.environ.get("BILIBILI_CSRF")}


def check_in_exp():
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0"
    }
    exp_check = session.post("https://api.bilibili.com/x/vip/experience/add", headers=headers, params=params2)

    data = exp_check.json()
    print(json.dumps(data, indent=2, ensure_ascii=False))


def check_in_coin():
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36 Edg/144.0.0.0",
        "Referer": "https://example.com/",
    }
    img_key, sub_key = getWbiKeys()
    enc_param = encWbi(params2, img_key=img_key, sub_key=sub_key)
    coin_check = session.post(
        "https://api.bilibili.com/pgc/activity/score/task/sign", headers=headers, params=enc_param
    )

    data = coin_check.json()
    print(json.dumps(data, indent=2, ensure_ascii=False))


def main():
    # check_in_exp()
    # time.sleep(3)
    check_in_coin()
    # resp = session.get("https://api.bilibili.com/x/vip/privilege/my", headers=headers)


if __name__ == "__main__":
    main()
