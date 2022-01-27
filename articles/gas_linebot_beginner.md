---
title: "🔰(新IDE対応版)オウム返しをするLINEBotをGASのWebエディタで最小限に作る"
emoji: "🤖"
type: "tech"
topics: ["コード有り", "LINE", "Bot", "GAS", "GoogleAppsScript"]
published: true
---
<!-- テンプレートバージョン: 2022.01.24.b.book_md -->

:::message alert
## ❗本記事の内容は、最終更新時点での情報です。
あなたがご覧になっているタイミングでは、記事の内容が古い可能性があります。
:::

:::message
### コメントについて：この記事は「教材予定」です。
将来的に本に移行する予定ですが、この記事を「いいね！」しておいてもらえると、本に移行した後でも本文を読むことができるようにしておきます。
また、本に移行した後もコメントができるようにしておきます。
:::

# 想定読者
- 受講生の方
- いつも「LINEBot オウム返し」で検索する私
- GetあるいはPostしたデータをデバッグする方法を探している方

# やること
いきなり運用レベルの話をするとこんがらがるので、

1. LINEからメッセージを送るためにMessagingAPIを使えるBOTアカウントを作る
1. MessagingAPIを使う設定にして「チャネルアクセストークン」を作成する
1. GASのプロジェクトを作る
1. GASのソースコードに上記MessagingAPIで作成したチャネルアクセストークンを指定する
1. GASのプロジェクトをデプロイする
1. GASのWebアプリURL(https://script.google.com/macros/s/ここに適当なID/exec)をLINEBotのWebhookURLに設定する

に絞ってやります。

## 後で探し直すものまとめ
### LINE Developerの用語
|用語|意訳、またはイメージ|
|---|---|
|プロバイダー|ディレクトリのようなもの。Botをあまり作らないならなるべくまとめてしまった方が見通しが良い（個人差あり）|
|チャネル|プロバイダーがディレクトリならファイルのようなもの。実態はLINEアカウントのようなもの。|

### URL
|概要|アドレス|作り方|
|---|---|---|
|LINEBotアカウントを作る|https://developers.line.biz/console|LINE Developers。新しいチャネルはここで作る。また、ログインはLINEアカウントを使う|
|LINEのMessagingAPI設定|https://developers.line.biz/console/channel/チャネルID/messaging-api|チャネルアクセストークンを発行したり、WebhookURLを設定する|
|LINEBotのグループ設定|https://manager.line.biz/account/(BOTのアカウントID)/setting|グループに使えるようにする設定がある場所|
|GASプロジェクトの新規作成|https://script.google.com/home|Googleアカウントは作っている想定。ログインできない場合はパスワードを再発行したり、アカウントを作り直すかする。|
|(GAS)LINEBot WebhookURL|https://script.google.com/macros/s/ここに適当なID/exec|GASプロジェクトをデプロイする|
|Githubリポジトリ|https://github.com/shimajima-eiji/--GAS_v5_LINEdebug|今回使うリポジトリのルート|

注意するべきは上記の通りです。
細かいのはそれぞれの章で書いています。

## LINE側の設定
1. まずはLINE Developersにログインしましょう。
1. 初めての方はプロバイダーを設定しましょう。
  1. https://developers.line.biz/console/ のプロバイダーの近くに作成ボタンがあります。色々言われるままに設定しましょう。
1. プロバイダーに新しくチャネルを作成します。既存のものに影響があるので全員が作った方がいいです。
1. 作ったチャネルのMessagingAPI設定 (https://developers.line.biz/console/channel/チャネルID/messaging-api) でチャネルアクセストークンを発行する
  1. WebhookURLは後で設定するので、ページは閉じないこと

基本的にこれでいけますが、プロバイダーとチャネルの作成時に色々聞かれるので、あなたの状況に一番近いものを選択しておきましょう。
執筆時点では、この作業でサブスクリプションが発生することはありません。

## GASでやること
### まずはプロジェクトを作成する
https://script.google.com/home

で、新しいプロジェクトを作成しましょう。
名前はなんでもいいので、分かりやすく管理できるようにしておくのがおすすめです。

Google Driveで見た時にルートディレクトリ以下に作成されているので、ごちゃごちゃして見づらいと思います。
後で手動で配置換えをしておきましょう。

https://drive.google.com/drive/my-drive

### ソースコードを作成
コピペでOKです。
一部編集する必要があるので、後述しておきます。

https://github.com/shimajima-eiji/--GAS_v5_LINEdebug/blob/main/%E3%82%AA%E3%82%A6%E3%83%A0%E8%BF%94%E3%81%97BOT%E3%81%AE%E8%A7%A3%E8%AA%AC%E3%82%B3%E3%83%BC%E3%83%89.gs

ファイル名は`コード.gs`でいいんですが、関数名は`myfunction()` → `doPost(e)`としてください。
この名前じゃないとPOSTされたデータを受け取れません。[^1]
[^1]: 【GETとPOST】ここでは詳しく解説しませんが、Webでデータをやり取りする方法です。LINEからデータを受け取るためPOSTを使います。

```
const TOKEN = "(ここは自分で入れる)"
const ENDPOINT_TARGET = "push"  // トークはreply, グループはpush
// GASでデバッグする場合はグループのみ（トークのリプライトークンが使えないため）
```

このTOKENとは、LINEBOTのチャネルアクセストークンのことです。
ENDPOINT_TARGETには、トークとグループで送信先が異なるため、手動対応が必要です。
GASでデバッグしやすいのはグループなので初期値は`push`にしてますが、トークを使いたい場合は`reply`にしてデプロイしてください。

### GASのプロジェクトをデプロイ
デプロイに罠があります。
新しいWebIDEの話をしますが、新しいデプロイを作るたびに新しいWebhookURLが発行されます。
なので、やり方を間違えるとデプロイをするたびに後述のLINEBotのWebhookURLを書き換える必要が出てきます。

注意する点だけピックアップします。

1. 新しいデプロイを作成
  1. 次のユーザーとして実行：「自分」
  1. アクセスできるユーザー：「全員」
1. デプロイを作り直す場合
  1. デプロイの管理を開く
  1. 編集（ペンのアイコン）を押下
  1. バージョンを「新バージョン」に変更する。これを忘れると何も更新されていない事になる。

よくわからない場合は、デプロイするたびに後述のLINEBotのWebhookURLを書き換えるというルールを徹底すればOKです。

### LINEBotとGASを連携する
LINE Developers(https://developers.line.biz/console/channel/チャネルID/messaging-api)に戻って、GASのWebアプリURL(https://script.google.com/macros/s/ここに適当なID/exec)をLINEBotのWebhookURLに設定します。
「更新」ボタンを押した後に「検証」ボタンを押すと、接続先が正しいか確認できます。

ここまでできたら、友達追加のQRコードをLINEで読み取ってメッセージを投げたり、グループを作ったりすると色々できます。
GASで設定したENDPOINTがreplyかpushかは確認しておきましょう。よく忘れるので、心配なら両方にメッセージを投げると良いです。

# ぼやき
この内容ぐらいならNode-RED(enebler)を使えばノーコードで同じことができるんじゃないかと思ってます。
他のことで使いたいので、いったんGASで作る方法をまとめておきました。

ということで、ここまで出来たら受講生の方は次の発展課題へ進んでみましょう。
元リポジトリではどうやって運用しているのか、完成したコードと比較してみるのも良いです。

---

# 発展：デバッガの改善案
そもそもこの記事の方法は「通信がうまくいっている場合」に有効なので、うまく行っていない場合は恐ろしくデバッグしにくいです。
開発しやすくなるように（という訳ではないんですが、ローカルでも開発できる）claspがあるんですが、環境構築の手間があるので使いたくない事もある事を想定しています。

さて、そうなるとGASのデバッガではなく、GET/POST(curlコマンドとか)のprintデバッグの方法も考える必要があります。
つまり、doPostスプレッドシートに書き込んでいく方法です。
以下、当該コード。

https://github.com/shimajima-eiji/--GAS_v5_LINEdebug/blob/main/%E5%87%BA%E5%8A%9B%E9%96%A2%E9%80%A3.gs

```
function output_sheet(value = {}){
  const SSID = property("SSID").value;
  const SSNAME = property("SSNAME").value;
  const SHEET = SpreadsheetApp.openById(SSID).getSheetByName(SSNAME);

  message = "[Skip] Not found [Spread-Sheet ID] or [Spread-Sheet Name] or [value(json)].";
  if (SHEET != null) {
    SHEET.appendRow([new Date(), JSON.stringify(value)]);
    message = "[COMPLETE]add data";
  }

  Logger.log("output.gs/output_sheet: " + message);
  return message;
}
```

`output_sheet(JSON形式)`で実行すると、スプレッドシートに書き込んでいくものです。
ここで渡すべき引数こそ`doPost(e)`の`e`です。
propertyは独自関数なんで恐縮ですが、スプレッドシートのIDとシート名を格納しているものと置き換えてください。
`SHEET.appendRow([データ])`で値を格納しています。`JSON.stringfy`で文字列にしないと登録されるデータが`[Object, Object]`になってしまいます。
注意すべきポイントは、eの中にJSONデータになる文字列があり、これを`JSON.parse`でデータとして使えるようにしていく必要がある点です。

こういったデータの内容を洗い出すためにも、デバッガは重要です。

## 参考
正直、GAS(WebIDE)はデバッグ能力がほぼゼロなので、ちゃんとデバッグをするならローカルでclasp入れて作った方がいいです。
nodeへの理解とノウハウが必要ですが、理解すると大体のnode開発に活かせるので学ぶ価値は高いと思います。

今回はGASのWebIDEに固執しました。
ツールも自身でうまく使えればそれなりの環境は整備できます。
が、慣れないうちは無理せず使える機能を活用していく事を考えましょう。

## あなたにとって、この記事がお役に立てたなら、💓いいねをいただけると私はとても嬉しいです。
:::message
もし良ければ、この本を読み終わった後にでもコーヒー一杯ぐらいを奢っていただけませんか？
あなたの応援が、より良い記事を書くモチベーションになって嬉しいです。
:::
