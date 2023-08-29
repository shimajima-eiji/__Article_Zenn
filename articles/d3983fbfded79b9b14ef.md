---
title: ブートローダーが壊れただけの正常なファイルシステムのディスクを起動したい
emoji: 📝
type: qiita
topics: ["Linux", "grub", "LiceCD"]
published: true
---

:::message
この記事はQiitaから移行しています。
:::

https://qiita.com/items/d3983fbfded79b9b14ef

---

今回使ったのはUbuntuですが、同じやり方でCentOSも出来るんじゃないかなぁ、と思ってます。

# 構成
OS: Ubuntu16.04(Server: CUI)
CD: Ubuntu16.04(LiveCD: GUI)
HDD: 4TB
GRUB2

# 注意
ここでは起動をするだけですが、何か変更を加える場合(下記でGRUBの初期化を実施しようとしていますが、こういったケースも含め)バックアップを取っておいてください。
また、正常なシステムで行うと予期せぬ問題が発生する事も考えられます。

# 解決
**LiveCDのブートメニューを起動して、HDDをrootにする**
boot=casperをroot=/dev/sda2(sda1はbios bootパーティション）として、10分もかからないと思いますが待っていると起動されました。
イメージ的には、LiveCDで実行する時にchroot /media/ubuntu/(UUID)/とする、でしょうか。

# 展開
ネットワーク接続設定を変えてopenssh-serverを入れて接続するところまで確かめたので、この状態でアプリケーションを起動したりするのも問題はなさそうです。
とはいえ、入念なテストを行ったわけではないので、なるべくなら正常な状態に戻すようにすべきです。

## 備考
GRUB の初期化を実施するとログイン画面ではなくGRUB Rescueが立ち上がるので、私の環境では改善は出来なかったようです。

# 補足
正常なファイルシステムであることをfdisk -lとmount /dev/sda2 (mnt)としてファイルにアクセスできることを確認したぐらいですが、より確実に調べるならgpartedを使うべきでしょう。

# 参考
<a href="https://www.kunihikokaneko.com/free/linuxtoolchain/grubinstall.html">起動できなくなった Ubuntu の起動を試みる(金子邦彦研究室)</a>

# 読了後いいね！をお願いします。
どれだけの方に読んでもらっているか知りたいので、お手数をおかけしますがご協力いただけると嬉しいです。

