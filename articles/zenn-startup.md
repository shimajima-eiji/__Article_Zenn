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
[Zenn-CLI](https://zenn.dev/zenn/articles/zenn-cli-guide)を使うのが圧倒的に楽だが、手動で実施したい場合のメモを残す

### 推奨: Zenn-CLIをインストールする
[公式](https://zenn.dev/zenn/articles/install-zenn-cli)

```
npm install -g zenn-cli
git clone (new repository)
cd (new repository)
npx zenn init
```

### 尚良: VSCodeにZennの拡張機能を入れる
[Zenn Editor](https://marketplace.visualstudio.com/items?itemName=negokaz.zenn-editor)がおすすめ

### 必須:Github連携
真っ新なリポジトリを作ってZenn-Github連携をするのが良さそうだが、既存リポジトリでもできる。設定は[Deploy from GitHub(Zenn)](https://zenn.dev/dashboard/deploys)を参照。

#### 手動で作業する場合
とりあえず真っ新なリポジトリを連携した直後では、以下のようなエラーが出ていた。

```
articlesディレクトリが見つかりませんでした。ディレクトリ構造やディレクトリ名がZennのルールに則っていない可能性があります。
booksディレクトリが見つかりませんでした。ディレクトリ構造やディレクトリ名がZennのルールに則っていない可能性があります。
```

`npx zenn init`を実施すると、以下のように作成される理由が一つ理解できた。

```
.
├── README.md
├── articles
└── books
```

これを手動で作ってもエラーは解消された。

### 何をしたらいいかわからない
とりあえずおもむろに`npx zenn preview`とすると、[ローカルにこんな感じのページ(リンク先は要コマンド)](http://localhost:8000)が出てくる。

![ローカルプレビュー](https://shimajima-eiji.github.io/__Backup_Images/Zenn/articles/my-awesome-article/ローカルプレビュー.png)

困ったらこれをみれば良さそう。

### 記事の書き方
`npx zenn new:article`の結果。

`--slug (my-awesome-article)`をつけると、記事URLを指定できるが、タイトルには反映されないようだ。

内部的には http://localhost:8000/articles/my-awesome-article に接続している。

### 本の書き方
（後日追記）こちらは少々複雑のようだ。

## 要望
[GitHubリポジトリ連携で画像をアップロードする方法（公式）](https://zenn.dev/zenn/articles/deploy-github-images)（[ローカルでも見れる](http://localhost:8000/guide/deploy-github-images)）を見ると、webpには対応していない。
[webpに移行したい者として](https://github.com/shimajima-eiji/__Backup_Images)は、webpにも対応してもらえると管理が非常に楽になる。

当面は、うまい運用管理を検討する他ない
