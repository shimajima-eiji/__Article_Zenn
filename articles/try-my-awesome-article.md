---
title: "１ミリも知らないでzennに記事を投稿するまでのリアルな作業"
emoji: "🎉"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["test"]
published: true
---

# 想定読者
- 今日はじめてzennにさわった
- 今Qiitaを使っているが、zennにも興味がある
- エンジニアだって気軽にポエムを書きたい
  - むしろポエム駆動開発だ[^1]

[^1]: 【ポエム駆動開発】実務においては馬鹿馬鹿しいと笑われますが、エンジニアの傾向を見極めるのに大変重要な情報です。

# 注意
公開のため、フォーマットを整備しています。
`npx zenn new:article`の初期値は以下の通り。

```
---
title: ""
emoji: "🎉"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: []
published: false
---
```

これでは公開できないので、公開できるようにするため、以下のようにしました。

```
---
title: "my-awesome-article以外のタイトルで公開"  # 公式で --slug my-awesome-articleとしていたので引用したが、これは使えないので任意に設定する
emoji: "🎉"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["test"]  # 必ず１つは必要
published: true   # falseでは公開できない
---
```

# 個人的なハマりポイント
- 初期にハマりやすいのですが、ファイル名は**12文字以上**が必要です。
- 使えないファイル名があるようです。以下検証。
  - `my-awesome-article.md`は403、それ以外は404のエラー画面が出ます
- Bookは全ユーザー共通？のようで、デプロイするまでエラーが分かりません。作り込む前に公開可能か確認しておきましょう。
- `emoji`欄は「えもじ」で検索すると色々出てきます。
- 自分の記事を確認する方法が２つあるので、記事内にアドレスを入れる時は気をつけましょう。以下、私が見たこの記事の例
  - https://zenn.dev/nomuraya/articles/try-my-awesome-article
  - https://zenn.dev/articles/try-my-awesome-article/edit

もっと細かい情報をまとめておきます。
https://zenn.dev/nomuraya/articles/zenn-startup
