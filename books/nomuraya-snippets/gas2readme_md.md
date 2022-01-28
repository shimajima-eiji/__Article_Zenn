---
title: "🤖[GAS]WehIDEでREADME.gsを作ってREADME.mdを作るGithub Actions"
---
<!-- テンプレートバージョン: 2022.01.24.b.book_md -->

:::message alert
## ❗本記事の内容は、最終更新時点での情報です。
あなたがご覧になっているタイミングでは、記事の内容が古い可能性があります。
:::

:::message
## 💓いいねについて：本記事は供養のために書いています
本当にどこに置いておけば良いか分からないものになってしまったので、ごった煮に混ぜ込んでます。
もしお役に立つことがあれば彼らも救われます。
:::

# 目的
Google Apps ScriptsのWebIDE(https://script.google.com/home)を使って開発する事があり、ドキュメンテーションが軽視されがちです。
せめてREADME.gsを書いていますが、Githubで見た時にしっくりこない。
これではユーザーにとっては使いにくい事この上ない。

という問題を解決したい思いで作りました。

# ソースコード
```
name: README.gsをREADME.mdに変換
on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2  # git clone (this)
      - name: run
        run: |
          # README.gsから1行目の/*と、最終行の*/を削除。
          # 行ごと削除しているので、上記以外は考慮しない
          # /*
          # （中略）
          # */
          cat README.gs | sed '1d' | sed '$d' | tee README.md

          # 更新がない場合は処理しない
          if [ -z "$(git status -s)" ]
          then
            echo "[Skip] no Changed README.md"

          # https://github.com/(ユーザー)/(リポジトリ名)/settings/secrets/actions
          else
            git config --global user.name "${{ secrets.USER }}"
            git config --global user.email "${{ secrets.EMAIL }}"
            git add -A
            git commit -m "Created README.md from README.gs by Github Actions"
            git pull
            git push
            echo "[COMPLETED] Update README.md"
          fi
```

# 使われない理由
単純に需要がないです。
作っておいてこんな事を言うのもなんですが、こんなところにリソース割くよりもっとやることがあるはず。

個人では使い勝手が良いので使っていますが、ドキュメンテーションするなら品質の高いコードを書け、というのも正論です。
品質の高いコードを書いて、品質の高いコメントを書ければベストです。私もそう思います。
が、実情としてなかなかそういう訳にはいかないので「コメントやドキュメンテーションにも技術があるんだよ」という気付きになれば幸いです。

せめて、個人開発なら時間をいっぱい使って知見を得ましょう。

## あなたにとって、この記事がお役に立てたなら、💓いいねをいただけると私はとても嬉しいです。
:::message
もし良ければ、この本を読み終わった後にでもコーヒー一杯ぐらいを奢っていただけませんか？
あなたの応援が、より良い記事を書くモチベーションになって嬉しいです。
:::
