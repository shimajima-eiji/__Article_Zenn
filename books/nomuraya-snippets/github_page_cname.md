---
title: Github Pagesに独自ドメインを設定する方法
---

:::message
この記事は「備忘録」です。
本稿に似た記事は探せばあるので、分からなくても諦めず頑張ってみてください。
:::

:::message alert
Githubリポジトリは開発用で使っているものなので、すぐに消えます。
リンク切れあるいはソースがない可能性もあります。
:::

# 作ったページ
https://nomuraya.tk

とりあえず動けばいいよ、で作ってるので内容はないよう。

なんつってｗｗｗｗｗｗｗ

## ちゃんとやります。
|項目|URL|
|---|---|
|ページのドメイン|https://nomuraya.tk|
|元ページ(Github PagesのURL)|https://shimajima-eiji.github.io/__Debug_Github|
|リポジトリ|https://github.com/shimajima-eiji/__Debug_Github|

このように設定できればOKです。

## やったこと
- ドメインを取得する。
  - 今回は[freenom](https://freenom.com/)を使用
  - ドメインは`nomuraya.tk`とするので、各自読替えのこと
- ドメインサーバーにAレコードを設定する
  - freenomの場合、https://my.freenom.com/clientarea.php?action=domains の「Manage Domain⚙️」->「Manage Freenom DNS」でレコード設定画面が開く
  - レコードの設定は後述
- GithubPages設定
  - GithubPagesを使えるように設定。そもそもリポジトリがない場合は作成しておく
  - /settings/pagesのcustom domainで作成したいドメイン名(`nomuraya.tk`)を書く
  - これにより、GithubPagesのルートにCNAMEファイルが作成される。
  - なお、手動で作成してもよい。CNAMEには取得したドメインだけ書いておく。(この場合は`nomuraya.tk`)

### レコードを登録する
カスタムドメインについて(ここではWWW)
https://docs.github.com/ja/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages

Apexドメイン(Aレコード)について
https://docs.github.com/ja/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

を参照すると、上記の通り書いてあったので言われるままに設定。

|名前|レコード(タイプとか)|設定値(対象とかターゲットとか)|備考|
|---|---|---|---|
|WWW|CNAME|[アカウント名].github.io(私の場合、shimajima-eiji.github.io)||
||A|185.199.108.153||
||A|185.199.109.153||
||A|185.199.110.153||
||A|185.199.111.153||
||AAAA|2606:50c0:8000::153|IPv6を使う場合|
||AAAA|2606:50c0:8001::153|IPv6を使う場合|
||AAAA|2606:50c0:8002::153|IPv6を使う場合|
||AAAA|2606:50c0:8003::153|IPv6を使う場合|

AとかAAAAとかに名前がないですが、何も書かないとApexドメインを指定するのと同じです。
暗黙的に`nomuraya.tk`が入っているという認識ですね。

![設定例](https://raw.githubusercontent.com/shimajima-eiji/__Backup_Images/main/Zenn/book/nomuraya-snippets/github_page_cname/DNS%E3%82%B5%E3%83%BC%E3%83%8F%E3%82%99%E3%83%BC%E5%81%B4%E8%A8%AD%E5%AE%9A.webp)

## この記事で出てきた用語など解説について
ご覧の通り、ドメインやネットワークの知識があることを前提に書いていますので、設定できたからOKではなく、分からない用語やアーキテクチャーについてはしっかり学んで自身に腹落ちさせましょう。
より深く学びたい場合は参考サイトを探してみたり、受講生の方は質問にきてもらってOKです。
