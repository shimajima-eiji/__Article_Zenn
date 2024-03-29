---
title: "buttonタグをクリックした時にlocation.hrefが正常に機能しない問題の原因と解決"
emoji: "📝"
type: "tech"
topics: ["HTML", "JavaScript"]
published: true
---

:::message
この記事はQiitaから移行しています。
:::

https://qiita.com/items/ca918cba7d4c3bb6f7c0

-----

## お詫び
Qiitaの元記事にて、区切り線を「---」で書いている場所があり、これがZennの記法に干渉して一部うまく表示できない記事がある事を認識しています。
全ての記事を精査しきれていないため、お手数ですがお見かけの際は教えていただけると大変喜びます。

-----

私の環境だけだと思うんですが、不可解な現象に出くわしたので備忘録。

# TL:DR 原因と解決
buttonタグはonclickを書いてもsubmitを無効にしないとスクリプトが実行されない。
そのため、`<button type='button' onclick='...'>`としなければならなかった。

# 経緯と再現
ボタンをクリックするとページジャンプ！をやりたいので、
`location.href='(ジャンプ先)'`を指定。
サクッとサンプルページを作りたいので、ローカルで環境を作ってVivaldi2.10...で実施。
ディレクトリ構造は以下の通り。

```
# tree
.
├── index.html
└── jump.html
```

たとえば、index.htmlからjump.htmlにリンクさせたいケースがあったとする。
aタグで指定した時はjump.htmlにジャンプできているとして、問題は

- `<input type='button' onclick='...'>`ならjump.html
- `<button onclick='...'>`ならindex.html **?**

にジャンプする。
幾つかのサイトを参考にしたが、**submitについて言及されておらず気付かないとハマるため**、書き残しておく。

