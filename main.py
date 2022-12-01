import json
import webbrowser

import fire


def url(name):
    urls_file = open("urls.json")
    urls_dict = json.load(urls_file)
    for k in urls_dict:
        target_name = k["name"]
        if target_name == name:
            print(target_name)
            url = k["url"]
            webbrowser.open(url, new=0, autoraise=True)
            return

    return "指定されたサイトが存在しません。"


if __name__ == "__main__":
    fire.Fire()
