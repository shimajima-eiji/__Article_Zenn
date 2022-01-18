---
title: "my-awesome-article"
emoji: "🎉"
type: "tech" # tech: 技術記事 / idea: アイデア
topics: ["test"]
published: true
---

# 注意
公開のため、フォーマットを整備している。
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
title: "my-awesome-article"  # 公式で --slug my-awesome-articleとしていたので引用
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
