---
title: "【後に📚本化します】GASで翻訳記録を残すChrome拡張機能を作るまでの手引き"
emoji: "📚"
type: "tech"
topics: ["Bot", "GAS", "chrome拡張機能", "JavaScript", "API"]
published: true
---
<!-- テンプレートバージョン: 2022.01.24.b.book_md -->

:::message alert
## ❗本記事の内容は、最終更新時点での情報です。
あなたがご覧になっているタイミングでは、記事の内容が古い可能性があります。
:::

:::message
### コメントについて：この記事は「ヒント集」です。
コメント欄には質問または回答を書かないでください。
質問がある場合は、非公開コメント機能を使ってください。
:::

# やること
細かい作業はありますが、ざっくり以下。

1. GASを作る。[GASリポジトリ](https://github.com/shimajima-eiji/--GAS_v5_Translate)をforkして[Google Apps Script GitHub アシスタント](https://chrome.google.com/webstore/detail/google-apps-script-github/lfjcgcmkmjjlieihflfhjopckgpelofo?hl=ja)からpullしてデプロイ
1. GASにcurlで接続し、期待した結果を得られることを確認する
1. ブラウザからhtmlファイルを開き、JavaScriptからcurlコマンドと同じ内容を実行し、結果が同じことを確認する
1. manifest.jsonを作ってChrome拡張機能にする
1. Bot(LINE, Slack, Twitter)と連携する

GASが一番キツいと思います。
GASが出来たら、あとはちょっとしたコマンドぐらいです。
Botが一番便利なのに、最後の項番にしたのはまたGASを書き換える必要があるからです。

# エッセンスを抜粋
## 1. GAS
:::details curlでアクセスした時にリクエストを受ける関数
```
function doGet(e) {
  // 説明のため、略
}
```

:::details 翻訳処理
```
LanguageApp.translate("翻訳したい単語", "単語の言語", "翻訳する言語");
```
:::

:::details アクセスされたらJSONを返す
```
let output = ContentService.createTextOutput();
output.setMimeType(ContentService.MimeType.JSON);
output.setContent(JSON.stringify(jsonData));
```
:::

## 2. curlコマンド
これが一番簡単だと思います。調べればすぐわかりますよ。

## 3. JavaScriptでcurl相当の処理を実行
:::details 自分で作ったGoogle Apps ScriptsのスクリプトIDに書き換えること
```
const SCRIPT_ID = 'AKfycbzX_fawOiQ-7ZKfbBlVc_3GM5YSDrStUJ5oASwt_Gt7VuzQciSLT8WTA426Vhxxiq3NOg'
// GETでパラメータを送る方法について調べること
```
:::

:::details JavaScriptでcurl(GET)する例
```
let request = new XMLHttpRequest();
request.open( 'GET', url, true );
request.responseType = 'json';

// アロー関数にしたら怒られるのでこのままで
request.onload = function ()
{
  add( this.response.translate );
};
request.send();
```
:::

## 4. chrome拡張機能
「manifest.json」で検索しましょう。
version3で書いていますが、version2について調べてみたり、オリジナルでアイコンを設定してみましょう。

## 5. Bot(Line)
応用問題です。
1.の解説を読んで、[GASでLINEBotを作るリポジトリ](https://github.com/shimajima-eiji/--GAS_v5_LineDebug)と上手く組み合わせてやってみてください。

応用問題はGASのソースコードを１行ずつ読んで理解しないと、どこをどうすればよいか分からない難問です。
コードだけで理解するのは大変ですが、フローチャートにするとやりたいことがイメージできるようになります。

## 非公開コメントフォーム(GoogleForm)
https://docs.google.com/forms/d/e/1FAIpQLSe6rZxqJpPOvuN5mHG0t0523ANjrh7reiC60YMXqlGWwTYHAQ/viewform

## あなたにとって、この記事がお役に立てたなら、💓いいねをいただけると私はとても嬉しいです。
:::message
もし良ければ、この本を読み終わった後にでもコーヒー一杯ぐらいを奢っていただけませんか？
あなたの応援が、より良い記事を書くモチベーションになって嬉しいです。
:::
