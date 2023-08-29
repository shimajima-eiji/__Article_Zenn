import os
import json


def convert_to_zenn_format(qiita_article):
    """
    Qiitaの記事をZennの形式に変換する関数
    :param qiita_article: Qiitaの記事データ（JSON形式）
    :return: Zenn形式の記事データ（文字列）
    """
    topics = [tag["name"] for tag in qiita_article["tags"]]
    zenn_article = f"""---
title: "{qiita_article['title']}"
emoji: "📝"
type: "tech"
topics: [{', '.join([f'"{topic}"' for topic in topics])}]
published: true
---

:::message
この記事はQiitaから移行しています。
:::

https://qiita.com/items/{qiita_article["id"]}

-----

## お詫び
Qiitaの元記事にて、区切り線を「---」で書いている場所があり、これがZennの記法に干渉して一部うまく表示できない記事がある事を認識しています。
全ての記事を精査しきれていないため、お手数ですがお見かけの際は教えていただけると大変喜びます。

-----

{qiita_article["body"]}
"""
    return zenn_article


def load_qiita_articles(filename):
    """
    Qiitaの記事データを読み込む関数
    :param filename: 読み込むファイル名
    :return: 記事データ（JSON形式）
    """
    with open(filename, "r") as file:
        qiita_posts = json.load(file)
    return qiita_posts


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
    json_path = "qiita_articles.json"  # 削除したいファイルのパス
    qiita_articles = load_qiita_articles(json_path)

    for qiita_article in qiita_articles:
        zenn_article = convert_to_zenn_format(qiita_article)
        file_name = f"articles/{qiita_article['id']}.md"
        save_to_file(file_name, zenn_article)

    # ファイルの取り込みが終了したら元ファイルは不要なので削除しておく
    if os.path.exists(json_path):
        os.remove(json_path)


if __name__ == "__main__":
    main()
