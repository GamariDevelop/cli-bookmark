import re
import json
import webbrowser

import fire


def main():
    fire.Fire()


def url(name):
    """指定のサイトに遷移する機能。"""
    urls_file = open("urls.json")
    urls_dict = json.load(urls_file)
    for url_map in urls_dict:
        target_name = url_map["name"]
        if target_name == name:
            target_url = url_map["url"]
            webbrowser.open(target_url, new=0, autoraise=True)
            return

    return "指定されたサイトが存在しません。"


def add(name, url):
    """URLの追加を行う。"""
    with open("urls.json", "r") as urls_file:
        urls_dict = json.load(urls_file)
        for url_map in urls_dict:
            if url_map["name"] == name:
                return "サイト名が重複しています。別の名前で登録してください。"
        # URL形式の判定
        url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
        if not re.match(url_pattern, url):
            return "URLの形式が間違っています。確認してください。"

        # 追加処理
        with open("urls.json", "w") as write_file:
            urls_dict.append({"name": name, "url": url})
            json.dump(urls_dict, write_file, indent=4)
    return "追加完了"


def list():
    """URL一覧を確認する機能。"""
    urls_file = open("urls.json")
    urls_dict = json.load(urls_file)
    for url_map in urls_dict:
        target_name = url_map["name"]
        target_url = url_map["url"]
        print(target_name, target_url)
    return "OK"


if __name__ == "__main__":
    main()
