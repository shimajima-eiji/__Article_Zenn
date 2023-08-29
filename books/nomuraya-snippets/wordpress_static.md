---
title: "wordpressで静的サイトを作る"
---

無料ブログからadiaryに移行したりmicroCMS-GatsbyJSやnote,Qiitaと使ってきて結局、wordpressが最強なのでは？というお話です。
が、あの頃のように若くないので、wordpressのマズさも理解しています。

- 作って１時間もしないうちにBotに攻撃される
  - セキュリティ設定が面倒
- PHPのバージョンによっては互換性がないテーマやプラグインがある
- そもそも遅い

他にも問題は数えきれないほどありますが、wordpressにはwordpressなりの問題があったわけです。
そこで、静的サイトにしよう！と決定したのが自分で言うのもなんですが、

- wordpressほど便利ではない
  - 群雄割拠しているので情報が錯綜している
- 記事データは別途管理しているので、見るべき点が２ヶ所以上ある
  - wordpressだと記事の内容もwordpressで完結できます。
- 結局サイトを作り込まなければならない(テンプレートが貧弱)

といった問題がありました。
一応細かい話なんですが、静的サイトジェネレーター自体のメンテナンスが必要な事もあったので、本質的にはwordpressのセキュリティ問題に似た課題は残りました。
セキュリティ上の問題ではないのですが、使っているプラグインやライブラリの影響は受けるので、これは盲点でした。

が、これらを一気に解決する方法がありました。
「wordpressでサイトを作って、静的サイトにすれば良くね？」と。

# 優れたWebサービスを使う
- shifter
- espar

などがまず候補に上がりますが、どちらも有料です。
ちょっとやりたいだけなのに、これは堪りません。
「それなら自前で作ってしまえ」と思い立つのに時間はかかりませんでした。

# やったこと
完全無料でできました。

1. wordpressをローカル環境に作る
1. wordpressからHTML化するプラグインを導入する
1. html化したファイルをホスティングサーバーにアップロード

これで完成です。
プラグインも色々ありますが、おすすめはwp2htmlです。
設定が日本語でわかりやすい！

- wordpressをローカル環境に作ったので外部から攻撃される事はありません
- wordpress上（ローカル）で動作検証ができるので、プラグインの導入がスムーズ
  - ただし、プラグインの内容によっては想定した通りhtmlファイルが生成されなかったりするので、やりすぎは厳禁です。

といった具合です。

# 副産物
1. ファイルアップロード先をGithubにしたので、バージョン管理ができる
1. ついでに、Githubにwordpressごとアップロードしてしまえば本体自体のバックアップもできる
1. 本体とファイルをアップロードできるリポジトリを同じにすればコマンドや環境を分けたりする必要もない
1. ホスティングサービスにアップロードする工程もCIで自動化する

正直、ここまで出来たらwordpressで静的サイトを作っている感覚です。
求めていたレベルはここなので、非常に満足しています。

あとは細かいプラグインですよね。どこまで出来て、どこからが出来ないのかはこれから見定めていくしかないです。