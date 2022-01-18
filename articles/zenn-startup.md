---
title: "【まとめ】QiitaからZennに乗り換える時に知っておくべき知識"
emoji: "🎉"
type: "tech"
topics: ["Qiita", "初心者", "まとめ"]
published: true
---

## スクラップ
- [Githubに翻訳したい文章をファイルで作ると翻訳したファイルをGithubActionで作成するCIを完成させるまで](https://zenn.dev/nomuraya?tab=scraps)

## 使い方
[Zenn-CLI](https://zenn.dev/zenn/articles/zenn-cli-guide)を使うのが圧倒的に楽ですが、手動で実施したい場合のメモを残します。

### 推奨: Zenn-CLIをインストールする
[公式](https://zenn.dev/zenn/articles/install-zenn-cli)

```
npm install -g zenn-cli
git clone (new repository)
cd (new repository)
npx zenn init
```

### 尚良: VSCodeにZennの拡張機能を入れる
[Zenn Editor](https://marketplace.visualstudio.com/items?itemName=negokaz.zenn-editor)がおすすめ（要精査）

### 必須:Github連携
真っ新なリポジトリを作ってZenn-Github連携をするのが良さそうですが、既存リポジトリでもできます。設定は[Deploy from GitHub(Zenn)](https://zenn.dev/dashboard/deploys)を参照。

#### 手動で作業する場合
とりあえず真っ新なリポジトリを連携した直後では、以下のようなエラーが出ました。

```
articlesディレクトリが見つかりませんでした。ディレクトリ構造やディレクトリ名がZennのルールに則っていない可能性があります。
booksディレクトリが見つかりませんでした。ディレクトリ構造やディレクトリ名がZennのルールに則っていない可能性があります。
```

`npx zenn init`を実施すると、以下のように作成される理由が一つ理解できました。

```
.
├── README.md
├── articles
└── books
```

これを手動で作ってもエラーは解消されます。やったね！

## トラブルシューティング
Zennを使わなくなったかもしれない来年の自分、を想定して書き残します。

### 何をしたらいいかわからない
とりあえずおもむろに`npx zenn preview`とすると、[ローカルにこんな感じのページ(リンク先は要コマンド)](http://localhost:8000)が出てきます。

![ローカルプレビュー](/images/articles/zenn-startup/ローカルプレビュー.png)

困ったらこれをみれば良さそうです。

### 記事の書き方
`npx zenn new:article`の結果。

`--slug (my-awesome-article)`をつけると、記事URLを指定できますが、タイトルには反映されませんでした。

VSCodeのZennEditorは内部的に http://localhost:8000/articles/my-awesome-article に接続しているようですね。
なお、絵文字は「えもじ」で変換すると色々出てきます。

### my-awesome-article.mdは作れない？
エラーメッセージが違いました。

- https://zenn.dev/nomuraya/articles/curl_python_arg (つながるもの。200)
- https://zenn.dev/nomuraya/articles/my-awesome-article (今回作ったもの。403)
  - https://zenn.dev/nomuraya/articles/try-my-awesome-article (執筆後に回避するために作成)
- https://zenn.dev/nomuraya/articles/my-awesome-article2 (今も存在しない。404)
- https://zenn.dev/nomuraya/articles/zenn-startup (執筆時点ではまだ上げていない。404)

ファイルが存在するから？と思ったので上記パターンを検証したんですが、上記結果の通りです。
ダメっぽいので、`my-awesome-article.md`は使わないようにしましょう。
もしかしたら、同じような事が他にもあるかもしれません。

### 外部イメージは使えない？
markdownで書いても上手くいかなかったので、htmlタグを使うなどの方法を検討する必要がありそうです。

![外部ページの画像はマークダウンで使えない](/images/articles/zenn-startup/外部ページの画像はマークダウンで使えない.png)

そもそも出来るのでしょうか？

### 本の書き方
（後日追記）こちらは少々複雑でした。

#### 記事の名前.mdと本の名前(ディレクトリ)は一致しても良い
パスが違うので問題なさそうです（未検証）

#### 本の名前にも制限がある？
パスを見ると

- https://zenn.dev/(USER)/articles/(TITLE:ファイル名)
- https://zenn.dev/(USER)/books/(TITLE:ディレクトリ名)

なので、一見問題なさそうなのに、このエラーメッセージはなんでしょうね？

![本の名前にも制限がある？](/images/articles/zenn-startup/本は全ユーザー共通の名前.png)

## 要望
[GitHubリポジトリ連携で画像をアップロードする方法（公式）](https://zenn.dev/zenn/articles/deploy-github-images)（[ローカルでも見れる](http://localhost:8000/guide/deploy-github-images)）を見ると、webpには対応していないようです。
[webpに移行したい者として](https://github.com/shimajima-eiji/__Backup_Images)webpを使う方法も考えてみたいところです。
