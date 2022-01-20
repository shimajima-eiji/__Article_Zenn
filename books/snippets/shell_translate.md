---
title: "実際に運用していたtranslate-shellを使った翻訳アプローチ"
---

# なぜ廃止してしまったのか
shellで複雑な運用をするといろいろな問題がありますが、転機になったのは日本語の文字化けです。
これを解決しようとするといくら時間があっても足りない！

なので、当初案は翻訳する部分だけに絞ってpythonで書いて、リファクタリングをしなくて済むようにしようとしました。

```
python "${curl_py}" "${GAS_TRANSLATE_ENDPOINT}?text=${line}&source=${source}&target=${target}" "${curl_log}"```
```

GAS_TRANSLATE_ENDPOINTは`.env`に書いて`source ~/.env`などで拾ってくれば気軽にGAS側も修正できるので、これは良かったです。
ただ、使ってみて気付いたんですがLanguageAPIはあまり精度が良くありません。
翻訳の内容というよりは翻訳語のフォーマットが壊れたり翻訳してくれなかったりします。

次にAPI制限です。
詳細は手前味噌の記事にまとめてありますが、一つ二つを翻訳するなら気にならないとしても、マークダウンファイルの内容をごっそり渡して処理させるのは無謀でした。
運用に耐えません。

https://qiita.com/nomurasan/items/aebead4856e02cbd9fd3

そこで、なるべくならGASを使って足りない部分をtranslate-shellで翻訳するという流れにしました。

# translate-shellの良かった点
コマンド一発で翻訳してくれるのは非常に好印象です。
現時点ではpythonのGoogleTransを採用しましたが、考え方は受け継がれています。
「技術選定をしないとムダな手戻りが発生する」と考えるシニアエンジニアの方も多いです[^1]が、運用を想定して書いても漏れ抜け仕様の壁にぶち当たりながらゴールに辿り着いたので技術的負債を清算する機会にできて良かったです。
[^1]: 【車輪の再発明は避けよ】他者に迷惑を掛けない範囲なら積極的にすべきと考えます。フレームワークやライブラリのありがたみや考え方を習得しやすいです。

# translate-shellの課題
先述しましたが、仕様の壁があります。API制限です。
API制限があっても運用でカバーできるかと思いましたが、１行翻訳するのに５秒以上掛かっていたら、ファイルの修正が頻発した時は地獄です。

そういった問題もあったのでLanguageAPI(GAS)を使う方法で対応する方法を検討しましたが、LanguageAPIも完全ではないため、翻訳結果が怪しくなりました。
結局、つぎはぎのコードになって保守性の観点から読みづらくなり、廃止に至りました。

# 代替案：GASとtranslate-shell(GoogleTrans)の併用
- 翻訳の速さはGASに、
- 正確性はTranslate-Shell(GoogleTrans)を
- 最終的な調整はスクリプトで

と、運用を使い分けることを考えます。
多くの解説サイトではどちらか一方を使って運用を検討するアプローチが多かったですが、運用を想定する場合は目的にあった方法を検討する必要があります。

# 文字化けについて
これは本題とは逸れてしまいますが、廃止した理由には間違いないので言及します。
shellで頑張ると沼にハマるので、早々にshellを捨てるという判断が出来ました。
shellで文字列走査を扱わない事を考える必要があるので、文字列処理に強いものを検討する必要があります。

ただ単純に文字列処理をするだけならrubyという選択肢はあったかもしれませんが、翻訳したデータを活用する(自然言語処理など)事を考えると、pythonに落ち着きました。
どちらも使い慣れていますが、私の先入観ながらRuby＝Webアプリを作るものという印象もあり、こういったケースでは優先度が低い傾向にあるかもしれません。

# これらを踏まえて、ソースコード
:::details ソースコード
```
#!/bin/sh
### need `apt install translate-shell`
### curl -sf https://raw.githubusercontent.com/shimajima-eiji/Settings_Environment/main/for_WSL/translate.sh | sh -s "(変換したいファイルパス)"
### .gitや.githubディレクトリなど、隠しファイルは対象にしない。
### 実運用時は出力を捨てた方が使いやすいかもしれない。

# transコマンドが使えなければやらない
if [ -z "$(which trans)" ]
then
  echo "[Stop] not found 'trans(translate-shell)'"
  exit 1
fi

# ディレクトリパスを引数に指定されていない場合はやらない
arg=$1
if ! [ -d "${arg}" -o -f "${arg}" ]
then
  echo "[Stop] Require arg. or arg isn't file or directory. ${arg}"
  exit 1
fi

source_arg=$2
target_arg=$3

# API制限を回避する
wait () {
  # FYI:
  # - https://qiita.com/eggplants/items/f3de713add0bb4f0548f
  # - https://webbibouroku.com/Blog/Article/linux-rand
  sleep "$(($(od -An -tu2 -N2 /dev/urandom | tr -d ' ')%5))"
}

# [Hint] 変換したファイルや行数が知りたい場合は、ファイル行数からカウントすべき
run () {
  echo  # メッセージを見やすくするため、改行する
  arg=$1
  source_arg=$2
  target_arg=$3

  # バイナリファイルは変換できないのでスキップ
  if [ -n "$(file --mime ${arg} | grep 'charset=binary')" ]
  then
    echo "[Skip] File is binary: ${arg}"
    return 1
  fi

  # ログファイルは対象にしない
  if [ "${arg##*.}" = "log" ]
  then
    echo "[Skip] File is exclude extension[.log]: ${arg}"
    return 1
  fi

  # ファイル名が「_」から始まる場合は対象にしない
  if [ "$(basename "${arg}" | cut -c1 )" = "_" ]
  then
    echo "[Skip] Filename is exclude pattern[_]: ${arg}"
    return 1
  fi

  # 対象ファイルが、過去に変換のために作成したものである場合はスキップ
  if [ -n "$(echo ${arg} | grep '_en.md')" -o -n "$(echo ${arg} | grep '_ja.md')" ]
  then
    echo "[Skip] translated file: ${arg}"
    echo "[Hint] '(name)_ja.md' and '(name)_en.md' is translate file."
    return 1
  fi

  #  既に変換済みのファイルの場合はスキップする（更新時は変換ファイルを手動削除すること）
  transen_file="${arg%.*}_en.md"
  transja_file="${arg%.*}_ja.md"
  if [ -f "${transen_file}" -o -f "${transja_file}" ]
  then
    echo "[Skip] Already translate: ${transen_file} or ${transja_file}"
    echo "[Hint] Case: updated ${arg}. 'rm (${transen_file} or ${transja_file})' after push."
    return 1
  fi

  # 翻訳する言語が決まっている場合は判定しない
  if [ -n "${source_arg}" -a -n "${target_arg}" ]
  then
    source=${source_arg}
    target=${target_arg}
    transfile="${arg%.*}_${target_arg}.md"

  else
    # 言語検出。ファイルの一行目を取得する。
    # ここでは基本的に日本語に変換するが、入力が日本語だったり、言語を検出できない場合は英語にする
    target="ja"
    source="en"
    result="$(trans -b :${target} "$(head -n 1 "${arg}")" 2>/dev/null)"
    transfile="${transja_file}"

    if [ "$(head -n 1 "${arg}")" = "${result}" -o -n "$(echo "${result}" | grep 'Did you mean: ')" ]
    then
      target="en"
      source="ja"

      transfile="${transen_file}"
    fi
  fi

  # ファイルから全ての行を抽出して変換する。
  echo
  echo "[INFO] Run translate(${target}): ${arg} -> ${transfile}"

  # 初期設定
  row_count=0
  source_flag='false'
  curl_log="$(pwd)/curl_gas.log"
  source ~/.env  # GAS_TRANSLATE_ENDPOINTを呼び出す
  curl_py="curl_translate.py"

  # jqコマンドが使えるならGASに問い合わせてみる
  if [ "$(which jq)" -a -n "${GAS_TRANSLATE_ENDPOINT}" ]
  then
    curl -sf https://raw.githubusercontent.com/shimajima-eiji/__Settings_Environment/main/for_WSL/translate_curl.py >${curl_py}
  fi

  # ファイル走査
  while read line
  do
    row_count=$((row_count+1))

    # 改行ではない場合
    if [ -n "${line}" ]
    then

      # markdownのソースコード表記は、フラグを入れ替えて```を追記
      if [ "${line}" = '```' ]
      then
        if [ "${source_flag}" = 'true' ]
        then
          source_flag='false'

        else
          source_flag='true'

        fi
        echo "${line}" >>${transfile}
        echo "[TRANSLATE PROGRESS] ${row_count}: ${line}"

      # ソースコードの場合は翻訳しない
      elif [ "${source_flag}" = 'true' ]
      then
        echo "${line}" >>${transfile}
        echo "[TRANSLATE PROGRESS] ${row_count}: ${line}"

      # ソースコードではない場合は翻訳する
      else
        # pyをcurlしているならGASを優先する
        if [ -f "${curl_py}" ]
        then
          python "${curl_py}" "${GAS_TRANSLATE_ENDPOINT}?text=${line}&source=${source}&target=${target}" "${curl_log}"

          # curlが成功した時はTranslate-GASの結果を入れる。2>/dev/nullは${curl_log}が存在しなかった場合にエラーメッセージを吐くため
          if [ -f "${curl_log}" -a "$(cat ${curl_log} 2>/dev/null | jq .result)" = "true" ]
          then
            translate_line="$(cat ${curl_log} | jq .translate)"
            echo "${translate_line}" >>${transfile}
            echo "[TRANSLATE PROGRESS] ${row_count}: ${line} -> ${translate_line}"

          # curlに失敗した場合は、translate-shellを使う
          else
            translate_line="$(trans -b ${source}:${target} "${line}" 2>/dev/null)"
            echo "${translate_line}" >>${transfile}
            echo "[TRANSLATE PROGRESS] ${row_count}: ${line} -> ${translate_line}"
            wait  # API制限に引っかかるので、待機時間を入れる
          fi

        # jqが使えない場合は、translate-shellを使う
        else
          translate_line="$(trans -b ${source}:${target} "${line}" 2>/dev/null)"
          echo "${translate_line}" >>${transfile}
          echo "[TRANSLATE PROGRESS] ${row_count}: ${line} -> ${translate_line}"
          wait  # API制限に引っかかるので、待機時間を入れる
        fi
      fi

    # 改行の場合
    else
      echo >>${transfile}
      echo "[TRANSLATE PROGRESS] ${row_count}:"
    fi
  done <"${arg}"

  # GASを使っている場合ｊは不要なファイルが残るので削除
  if [ -f "${curl_log}" ]
  then
    rm ${curl_log}
  fi
  # GASを使っている場合ｊは不要なファイルが残るので削除
  if [ -f "${curl_py}" ]
  then
    rm ${curl_py}
  fi

  echo "[COMPLETE] Done ${arg} -> ${transfile}"
  echo
  return 0
}

count=0  # 変換したファイル数をカウント
find_file () {
  arg="$1"
  source_arg=$2
  target_arg=$3

  # 変数がファイルなら変換処理
  if [ -f "${arg}" ]
  then
    run "${arg}" "${source_arg}" "${target_arg}"

    if [ $? -eq 0 ]
    then
      count=$((count+1))
    fi

  # 変数がファイル以外ならディレクトリを移動してサーチする
  else
    cd "${arg}"

    for path in *
    do
      find_file "${path}" "${source_arg}" "${target_arg}"
    done
    cd ..
    echo
  fi
}

find_file "${arg}" "${source_arg}" "${target_arg}"
echo "[COMPLETE] translate files:"
echo ${count}
```
:::
