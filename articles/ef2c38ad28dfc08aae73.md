---
title: "【コピペで済ませたい人向け】 rbenvのインストールを環境構築からパスチェックまとめ [2019版]"
emoji: "📝"
type: "tech"
topics: ["Ruby", "rbenv"]
published: true
---

:::message
この記事はQiitaから移行しています。
:::

https://qiita.com/items/ef2c38ad28dfc08aae73

-----

## お詫び
Qiitaの元記事にて、区切り線を「---」で書いている場所があり、これがZennの記法に干渉して一部うまく表示できない記事がある事を認識しています。
全ての記事を精査しきれていないため、お手数ですがお見かけの際は教えていただけると大変喜びます。

-----


# コマンドを探しにきた人に
```
# macOS
brew tap homebrew/core && brew install apple-gcc42

# Ubuntu/Debian/Mint
sudo apt install autoconf bison build-essential libssl-dev libyaml-dev libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm5 libgdbm-dev

# CentOS/Fedora
yum install -y gcc-6 bzip2 openssl-devel libyaml-devel libffi-devel readline-devel zlib-devel gdbm-devel ncurses-devel

# openSUSE
zypper install -y gcc6 automake gdbm-devel libffi-devel libyaml-devel libopenssl-devel ncurses-devel readline-devel zlib-devel

# Arch Linux
pacman -S --needed base-devel libffi libyaml openssl zlib
```

```
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
eval $(rbenv init)
source ~/.bashrc

rbenv install 2.x.x
rbenv local 2.x.x
```

# 動かない場合（既存の環境など）
パスとバージョンを確認

```
which rbenv
rbenv -v

which ruby
ruby -v

which gem
gem -v

which bundle
bundle -v
```

※インストールしてもパスが適用されていない場合は手動で通す。

```
# [command]はパスが間違っているコマンド名
cd $(which ruby)
unlink [command]
ln -s $HOME/.rbenv/bin/[command] [command]
```

# 解説
[コマンドの最新はWiki参照](https://github.com/rbenv/ruby-build/wiki)
ここでは執筆時点の最新を公式Wikiより引用。

また、[bash_profileではなくbashrcに書く理由](https://qiita.com/dark-space/items/cf25001f89c41341a9fd)はリンク先の通り。

# 筆者環境
WSLを使用している。
実行環境にbashを使用しているのでzshやfishでは実行できないかもしれない。

```
cat /etc/os-release 
# NAME="Ubuntu"
# VERSION="18.04.3 LTS (Bionic Beaver)"
# ...
```

# 動機
rbenvの情報が多いので解説はいいとして、そういうのは既に分かっている側の立場としては検索するのも面倒なんでお手軽にできるものが欲しかった。
執筆時点では、後述の筆者環境のみ検証しており、必要に応じて他環境も追記したい。

# 読了後いいね！をお願いします。
どれだけの方に読んでもらっているか知りたいので、お手数をおかけしますがご協力いただけると嬉しいです。

