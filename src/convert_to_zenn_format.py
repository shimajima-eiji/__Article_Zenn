import json
import os
import shutil

def convert_to_zenn_format(qiita_article):
    """
    Qiitaの記事をZennの形式に変換する関数
    :param qiita_article: Qiitaの記事データ（JSON形式）
    :return: Zenn形式の記事データ（文字列）
    """
    topics = [tag["name"] for tag in qiita_article["tags"]]
    zenn_article = f"""---
title: {qiita_article["title"]}
emoji: 📝
type: qiita
topics: [{", ".join([f'"{topic}"' for topic in topics])}]
published: true
---

:::message
この記事はQiitaから移行しています。
:::

https://qiita.com/items/{qiita_article["id"]}

---

{qiita_article["body"]}
"""
    return zenn_article

def load_qiita_posts(filename):
    """
    Qiitaの記事データを読み込む関数
    :param filename: 読み込むファイル名
    :return: 記事データ（JSON形式）
    """
    with open(filename, "r") as file:
        qiita_posts = json.load(file)
    return qiita_posts

def create_directory(directory_name):
    """
    ディレクトリを作成する関数
    :param directory_name: 作成するディレクトリ名
    """
    if os.path.exists(directory_name):
        shutil.rmtree(directory_name)
    os.makedirs(directory_name)

def save_to_file(file_name, content):
    """
    ファイルに内容を書き込む関数
    :param file_name: 書き込むファイル名
    :param content: 書き込む内容
    """
    with open(file_name, "w") as file:
        file.write(content)

def main():
    """
    メイン関数。Qiita記事をZenn形式に変換して保存する
    """
    qiita_posts = load_qiita_posts("/src/qiita_posts.json")
    create_directory("articles")
    
    for qiita_post in qiita_posts:
        zenn_article = convert_to_zenn_format(qiita_post)
        file_name = f"articles/{qiita_post['title']}.md"
        save_to_file(file_name, zenn_article)

if __name__ == "__main__":
    main()
