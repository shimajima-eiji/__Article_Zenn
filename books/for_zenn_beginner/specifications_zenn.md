---
title: "📝記事(Articles)と📖本(Books)の仕様調査"
---
:::message alert
# 本記事の内容は、最終更新時点での情報です。
あなたがご覧になっているタイミングでは、記事の内容が古い可能性があります
:::

:::message
この記事は「自分用の学習ノート」です。
コメントもマサカリも歓迎しますが、切れ味のよい内容はご容赦ください。
:::

どこかで情報がまとまっていると思いますが、手探りで調べたことを置いておきます。

# README.mdは無視される
単一ファイルで実行した例です。

![更新されたファイルはありません]()
*READMEを更新しても「更新されたファイルはありません」と表示されます。*

FrontMatter(`--- 〜 ---`)を消したり、色々な事をやってみたんですが反映されませんでした。
Githubで参照する時にも必要なファイルなので、敢えてこういう作りにしているんでしょうか。
連携解除してまで試す気力はなかったので検証していません。

# my-awesome-article.mdは作れない？
まず、そもそものエラーメッセージが違いました。

- https://zenn.dev/nomuraya/articles/curl_python_arg (つながるもの。200)
- https://zenn.dev/nomuraya/articles/my-awesome-article (今回作ったもの。403)
  - https://zenn.dev/nomuraya/articles/try-my-awesome-article (執筆後に回避するために作成)
- https://zenn.dev/nomuraya/articles/my-awesome-article2 (今も存在しない。404)
- https://zenn.dev/nomuraya/articles/zenn-startup (執筆時点ではまだ上げていない。404)

ファイルが存在するから？と思ったので上記パターンを検証したんですが、上記結果の通りです。
ダメっぽいので、`my-awesome-article.md`は使わないようにしましょう。
もしかしたら、同じような事が他にもあるかもしれません。

# 画像呼び出しで２バイト文字は使えない
## できないケース
![内部呼び出し.png](/images/articles/zenn-startup/2バイト文字のURLは使えない.png)
*/images/articles/zenn-startup/2バイト文字のURLは使えない.png*

---

## できるケース
![外部URLは使える](https://shimajima-eiji.github.io/__Backup_Images/Zenn/articles/zenn-startup/２バイト文字のURLは使えない.png)
*https://shimajima-eiji.github.io/__Backup_Images/Zenn/articles/zenn-startup/２バイト文字のURLは使えない.png*

---

これはなんででしょうね？
読み込めることもあるみたいですが、基本的に２バイト名は避けた方がいいです。

# Webpは使えない？
## できないケース
![内部呼び出し.webp](/images/articles/zenn-startup/cantuse_2byte.webp)
*/images/articles/zenn-startup/cantuse_2byte.webp*

---

## できるケース
![外部URL](https://shimajima-eiji.github.io/__Backup_Images/Zenn/articles/zenn-startup/２バイト文字のURLは使えない.webp)
*https://shimajima-eiji.github.io/__Backup_Images/Zenn/articles/zenn-startup/２バイト文字のURLは使えない.webp*

---

外からwebpを呼んでくるのは問題ないです。
内部的にwebpを呼ぶとこのようなエラーになります。

---

![外部URL](https://shimajima-eiji.github.io/__Backup_Images/Zenn/articles/zenn-startup/webpは内部的には使えない.webp)
*`/images/articles/zenn-startup/cantuse_2byte.webp`を表示できません。対応している画像の拡張子は`png, jpg, jpeg, gif`です。*

---

# それでもwebpを使うべきかpngやjpgを使うべきか
現状は後者と思います。
サーバーの場所やネットワークの状況にもよりますが、ファイル容量より通信の方が遅くなる可能性が高いと思われます。
が、厳密な調査はしていないので、興味があれば試してみてください。

https://pagespeed.web.dev

## Githubのwebpを使う方法
ホスティングしなくても使えます。(Raw)
ホスティングしていても使えます。(要Github Pages設定)

- [対象ファイル(Github)]()
- [raw](https://raw.githubusercontent.com/shimajima-eiji/__Backup_Images/main/Zenn/articles/zenn-startup/articles以下にディレクトリを置けない.webp)
- [GHP](https://shimajima-eiji.github.io/__Backup_Images/Zenn/articles/zenn-startup/articles以下にディレクトリを置けない.webp)

おすすめは前者です。

### 要望
[GitHubリポジトリ連携で画像をアップロードする方法（公式）](https://zenn.dev/zenn/articles/deploy-github-images) / （[ローカルでも見れる](http://localhost:8000/guide/deploy-github-images)）を見ると、webpには対応していないようです。
[webpに移行したい者として](https://github.com/shimajima-eiji/__Backup_Images)現状はGithubPagesで.webpをホスティングして呼び出す方法を想定しています。
:::

:::details 記事の書き方（操作は先述）
## articles以下にディレクトリを作ることはできない
![articles/2022にアクセスできない](https://shimajima-eiji.github.io/__Backup_Images/Zenn/articles/zenn-startup/articles以下にディレクトリを置けない.webp)
*https://zenn.dev/nomuraya/articles/2022/other-directory につなげない*

ある程度記事をまとめられそうなら本にしていった方がいいかもしれません。

## アコーディオン内のhタグが目次に反映されない
![アコーディオン内のhタグが目次に反映されない](https://shimajima-eiji.github.io/__Backup_Images/Zenn/articles/zenn-startup/アコーディオンのhタグは目次欄に表示されない.webp)
*更新前ながら、確認には問題なし*

たとえば、この項目でも複数のhタグを入れていますが、目次欄にはありません。
:::

:::details 本の書き方
## 記事の名前.mdと本の名前(ディレクトリ)は一致しても良い
パスが違うので問題なさそうです（未検証）

## 本の名前にも制限がある？
パスを見ると

- https://zenn.dev/(USER)/articles/(TITLE:ファイル名)
- https://zenn.dev/(USER)/books/(TITLE:ディレクトリ名)

なので、一見問題なさそうなのに、このエラーメッセージはなんでしょうね？

![本の名前にも制限がある？](https://shimajima-eiji.github.io/__Backup_Images/Zenn/articles/zenn-startup/my-awesome-bookは使えない.webp)

:::
