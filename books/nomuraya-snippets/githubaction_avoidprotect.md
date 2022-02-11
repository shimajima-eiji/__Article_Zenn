---
title: ブランチにプロテクトルールを掛けたいが、GithubActionからもpushしたい
---

タイトルのようなケースの運用をしたくなる事ってあると思うんですよね。
私が思うに、

1. 開発用のリポジトリ(仮にdevリポジトリ)のmainブランチにはプロテクトルールを設定する
1. 公開用のリポジトリ(仮にopeリポジトリ)にはプロテクトルールを設定しない
1. devリポジトリにGithubActionを動く状態で置いておく（ただし、プロテクトルールにより失敗する）
1. opeリポジトリにdevリポジトリをミラーし、opeリポジトリでCIを動かして成功させる

という運用案は割と真面目にアリだと思いました。
が、さすがにリポジトリが２つもあると管理コストも発生しますし、運用対処もつらいですね…。

こういった問題を解決するアプローチを考えます。

# ソースコード
```
# ポイントは`hub pull-request -f -m "${MESSAGE}" -h ${BRANCH} -a ${REVIEWER} -r ${REVIEWER}`
# ブランチ名に日付を入れたのは、push時にブランチが残っているとエラーになるので必ず新しいブランチを生成させるため
# pushするユーザーはGAを指定しないと、レビュアーに反映されない（自分をレビュアーにできない）

name: プロテクト検証
on:
  push:
    branches: [ master ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: ここで何かしらの処理をする想定。テストのため、README.mdを適当に書き換える
        run: echo $RANDOM >README.md
      
      - name: 更新状態を確認
        id: check_files
        # 実行結果としてはエラーではないので、continue-on-errorでパスさせる
        # Ref: https://qiita.com/ljourm/items/556f5ccc8425891865de
        continue-on-error: true
        run: |
          if [ "$(git status -s)" ]
          then
            echo "[Run] ファイルの変更を検出したため、処理を継続"
            
          else
            echo "[Skip] ファイルの変更がないため、処理を中断"
            exit 1  # 本来はここで終了してしまうが、見た目上エラーにしたくないのでcontinue-on-errorを設定している
          fi
          
      - name: コミット
        id: commit
        if: steps.check_files.outcome == 'success'
        env: 
          BRANCH: avoid_protect
          MESSAGE: Mirror root README txt to md by Github Actions
          OWNER: shimajima-eiji
          EMAIL: ${{ secrets.EMAIL }}
        run: |
          # ブランチ名は日付を追加して競合を回避する
          BRANCH="${BRANCH}_$(TZ=JST-9 date '+%Y%m%d_%H%M%S')"
          
          # Ref: https://scrapbox.io/nwtgck/GitHub_Actions%E3%81%AE%E3%83%9C%E3%83%83%E3%83%88%E3%81%8C%E3%82%B3%E3%83%9F%E3%83%83%E3%83%88%E3%81%97%E3%81%9F%E3%82%88%E3%81%86%E3%81%AB%E3%82%A2%E3%82%A4%E3%82%B3%E3%83%B3%E3%82%92%E3%81%A4%E3%81%91%E3%82%8B%E3%81%AB%E3%81%AF%E3%83%A1%E3%83%BC%E3%83%AB%E3%81%AB%E3%80%8Cgithub-actions%5Bbot%5D@users.noreply.github.com%E3%80%8D%E3%82%92%E6%8C%87%E5%AE%9A%E3%81%99%E3%82%8C%E3%81%B0%E8%89%AF%E3%81%84
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git config user.name "github-actions[bot]"
          git add -A
          git commit -m "${MESSAGE}"
          git push -u origin master:${BRANCH}
          echo "[COMPLETED] Success ${BRANCH} push"
          # 次のステップに変数を引き継ぐ
          echo "::set-output name=OWNER::${OWNER}"
          echo "::set-output name=BRANCH::${BRANCH}"
          echo "::set-output name=MESSAGE::${MESSAGE}"
      - name: プルリク作成
        if: steps.commit.conclusion == 'success'
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}  # hubコマンドの実行にパスワードが必要
          REVIEWER: shimajima-eiji
          BRANCH: ${{ steps.commit.outputs.BRANCH }}
          MESSAGE: ${{ steps.commit.outputs.MESSAGE }}
        run: |
          hub pull-request -f -m "${MESSAGE}" -h ${BRANCH} -a ${REVIEWER} -r ${REVIEWER}
          echo "[COMPLETED] Success create pull-request"
```

https://github.com/shimajima-eiji/__Github-Operation/blob/main/.github/workflows/txt2md.yml

# 良かったこと
- BOTが実行されたらREVIEWRに通知がいきます
- 既存の動作部分に影響はありません
- バグがあった時に原因を切り分けられるようにしていますので、エラーの特定が比較的容易です。
- 前段の処理で何をやっても組み込み部分には影響がないようにできています
- BOTのPR後に修正して、再度BOTが動いても正しくPRを出してくれます
  - 古いPRはクローズし、ブランチごと削除でOK

# 失敗したこと
- mainに直接pushできる運用をしていた場合はPRすら出さなかったので、承認作業が面倒くさい
