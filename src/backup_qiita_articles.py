import requests
import time
import json
import argparse


def fetch_qiita_articles(access_token):
    """
    Qiita API を利用して指定されたアクセストークンのユーザーの記事データを取得します。

    :param access_token: Qiita API アクセストークン。
    :return: Qiita 記事データのリスト。
    """
    # 1回のリクエストで取得する記事数
    ARTICLES_PER_PAGE = 100
    # 取得を始めるページ
    PAGE = 1

    endpoint = "https://qiita.com/api/v2/authenticated_user/items"
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
    }

    all_articles = []
    while True:
        params = {
            'page': PAGE,
            'per_page': ARTICLES_PER_PAGE,
        }
        try:
            response = requests.get(endpoint, headers=headers, params=params)
            response.raise_for_status()  # HTTPエラーがあれば例外を発生させる
        except requests.exceptions.RequestException as e:
            print("APIのリクエストに失敗しました:", e)
            break

        articles = response.json()
        if not articles:  # 取得した記事がなければループを抜ける
            break
        all_articles.extend(articles)
        PAGE += 1
        if len(articles) < ARTICLES_PER_PAGE:
            break
        # API レート制限を避けるためのスリープ
        time.sleep(1)

    return all_articles


def save_to_json(data, filename):
    """
    データを JSON ファイルに保存します。

    :param data: 保存するデータ。
    :param filename: データを保存するファイル名。
    """
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def main():
    """
    メイン関数。Qiita 記事データを取得してバックアップします。
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--access-token", required=True,
                        help="Qiita API アクセストークン")
    args = parser.parse_args()

    qiita_articles = fetch_qiita_articles(args.access_token)
    if qiita_articles:
        save_to_json(qiita_articles, "qiita_articles.json")
        print("Qiita 記事データのバックアップが成功しました。")


if __name__ == "__main__":
    main()
