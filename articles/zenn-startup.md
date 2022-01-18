---
title: "【まとめ】QiitaからZennに乗り換える時に知っておくべき知識"
emoji: "🎉"
type: "tech"
topics: ["Qiita", "初心者", "まとめ"]
published: true
---

これは本にまとめた方が良さそうな気がしてきました。[^1]
[^1]: 【本にまとめる】まとめたらリンクだけ残して記事は削除かなぁ。

# インストール・使い方
[Zenn-CLI](https://zenn.dev/zenn/articles/zenn-cli-guide)を使うのが圧倒的に楽ですが、手動で実施したい場合のメモを残します。

## 推奨: Zenn-CLIをインストールする
[公式](https://zenn.dev/zenn/articles/install-zenn-cli)

```
npm install -g zenn-cli
git clone (new repository)
cd (new repository)
npx zenn init
```

## 尚良: VSCodeにZennの拡張機能を入れる
[Zenn Editor](https://marketplace.visualstudio.com/items?itemName=negokaz.zenn-editor)がおすすめ（要精査）

## 必須:Github連携
真っ新なリポジトリを作ってZenn-Github連携をするのが良さそうですが、既存リポジトリでもできます。設定は[Deploy from GitHub(Zenn)](https://zenn.dev/dashboard/deploys)を参照。

## 手動で作業する場合
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

---

# Qiitaと違う点
## 書いた記事をGithubで管理できる
:::details 私がQiitaを捨てた理由
これはQiitaに書きにくいと感じている私向けのお話ですが、基準が不明瞭な利用規約に怯えて投稿を吟味したり、Qiitaで「気軽に書く」ということに抵抗を感じている事があります。
そこで、やむなく手動で自分で書いた記事の内容をGithubに移したり、また気に入った記事もいつ消えるか分からないので全部バックアップを取るようにしています。
こういうとなんですが、**Qiitaの記事は全てがいつかよくわからない理由で消される**と私は思っています。

細かいことをいうと、記事の著作権は主張したいので勝手に消されてはたまらないのです。
個人ブログで記事を書いていた方も、利用規約の堅苦しさを感じていたのだと思います。
:::

自分が書いたものを、他者の干渉を受けずに管理できるというのは安心ですね。
バックアップという観点で考えても、Githubに書いたものはcloneすればローカルでも保持できます。

## 質問や意見交換はスクラップを使うが、用途は限定されていない
:::details 私がQiitaを捨てた理由
まずそもそも、質問や意見交換という機能がまた意味不明です。
全て記事にして、聖人君子の有識者の方がコメントで指摘もしくは修正をすれば良いと思っています。
運営サイドが干渉するべきではありません。

おそらく、StackOverFlowやteratailを持ってこようとしたんでしょうが、Qiitaではやりたくないなぁと思ってます。
:::

書けることはないけど、議論はしたい。
そんなシーンは結構多いので、そういった時に気軽にスクラップを使うのが良いと思います。
記事でコメント合戦をすると間違いなく荒れるので、スクラップを作ってそちらで意見交換をするというのがベストプラクティスだと思っています。
筆者と有識者たちで議論するのは良いですが、一般読者を巻き込むべきではありません。

### スクラップはGithubでは管理できない
https://zenn.dev/nomuraya?tab=scraps

試しに一つ作ってみましたが、まとめるなら本の方が良さそうです。[^1]
バックアップが必要な場合は、記事にしてしまうと良いでしょう。

:::message
スクラップにはOpen/Closeの概念があり、「他のユーザーの投稿を許可」機能があります。
他のユーザーを許可しないなら、質問以外でもGithub Issueのような使い方をするのもアリな気がします。
:::

---

# トラブルシューティング
Zennを使わなくなったかもしれない来年の自分、を想定して書き残します。

:::details 何をしたらいいかわからない
とりあえずおもむろに`npx zenn preview`とすると、[ローカルにこんな感じのページ(リンク先は要コマンド)](http://localhost:8000)が出てきます。

![http:localhost:8000](https://shimajima-eiji.github.io/__Backup_Images/Zenn/articles/zenn-startup/ローカルプレビュー.webp)

困ったらこれを見れば良さそうです。
:::

:::details 記事の書き方
`npx zenn new:article`の結果。

`--slug (my-awesome-article)`をつけると、記事URLを指定できますが、タイトルには反映されませんでした。

VSCodeのZennEditorは内部的に http://localhost:8000/articles/my-awesome-article に接続しているようですね。
なお、絵文字は「えもじ」で変換すると色々出てきます。

---

ほか、使えるマークダウン記法は[公式の記事参照](https://zenn.dev/zenn/articles/markdown-guide)。
この記事内でもやたらとエッセンスをねじ込んでます。
:::

# 仕様調査
どこかで情報がまとまっていると思いますが、手探りで調べたことを置いておきます。

:::details my-awesome-article.mdは作れない？
エラーメッセージが違いました。

- https://zenn.dev/nomuraya/articles/curl_python_arg (つながるもの。200)
- https://zenn.dev/nomuraya/articles/my-awesome-article (今回作ったもの。403)
  - https://zenn.dev/nomuraya/articles/try-my-awesome-article (執筆後に回避するために作成)
- https://zenn.dev/nomuraya/articles/my-awesome-article2 (今も存在しない。404)
- https://zenn.dev/nomuraya/articles/zenn-startup (執筆時点ではまだ上げていない。404)

ファイルが存在するから？と思ったので上記パターンを検証したんですが、上記結果の通りです。
ダメっぽいので、`my-awesome-article.md`は使わないようにしましょう。
もしかしたら、同じような事が他にもあるかもしれません。
:::

:::details 画像呼び出しで２バイト文字は使えない
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

:::

:::details Webpは使えない？
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

### webpを使うべきかpngやjpgを使うべきか
現状は後者と思います。
ファイル容量より通信の方が遅くなる可能性が高いからです。

[PageSpeed Insights](https://pagespeed.web.dev/)とかで怒られるのは許容しましょう。

### 要望
[GitHubリポジトリ連携で画像をアップロードする方法（公式）](https://zenn.dev/zenn/articles/deploy-github-images) / （[ローカルでも見れる](http://localhost:8000/guide/deploy-github-images)）を見ると、webpには対応していないようです。
[webpに移行したい者として](https://github.com/shimajima-eiji/__Backup_Images)現状はGithubPagesで.webpをホスティングして呼び出す方法を想定しています。

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
