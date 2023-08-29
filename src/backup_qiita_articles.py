import requests
import argparse
import json

def fetch_qiita_posts(access_token):
    """
    Qiita APIから記事を取得する関数
    :param access_token: Qiita APIアクセストークン
    :return: 取得した記事のデータ（JSON形式）
    """
    endpoint = "https://qiita.com/api/v2/authenticated_user/items"
    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # HTTPエラーがあれば例外を発生させる
    except requests.exceptions.RequestException as e:
        print("API call failed:", e)
        return None

    return response.json()

def save_to_json(data, filename):
    """
    データをJSONファイルに保存する関数
    :param data: 保存するデータ
    :param filename: 保存先のファイル名
    """
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)  # ユニコードエスケープを無効化

def main():
    """
    メイン関数。Qiita記事をバックアップする
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--access-token", required=True, help="Qiita API access token")
    args = parser.parse_args()

    qiita_posts = fetch_qiita_posts(args.access_token)
    if qiita_posts is not None:
        save_to_json(qiita_posts, "/src/qiita_posts.json")
        print("Qiita posts saved successfully.")

if __name__ == "__main__":
    main()
