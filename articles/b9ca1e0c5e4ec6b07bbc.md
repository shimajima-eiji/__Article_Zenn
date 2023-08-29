---
title: "ソフトウェア開発者目線で見る、among us界隈の問題にみるソフトウェアの取り扱い"
emoji: "📝"
type: "tech"
topics: ["ゲーム", "GPL", "著作権"]
published: true
---

:::message
この記事はQiitaから移行しています。
:::

https://qiita.com/items/b9ca1e0c5e4ec6b07bbc

---

話題になっていた事は知っていたので多分やべーネタだろうなぁ、と思っていましたが調べてみると結構興味深かったので共有しようというモチベーションで本稿を書き上げています。
正直、断片的な情報ばかりで調べても面白かっただけで特に何か得られたわけではなかったので、せっかくだからGPLライセンスと著作権についてフォーカスしてお話ししていきます。
また、Twitterを含む多くのSNSを辞めたおっさんからの説教が若干ありますが、平にご容赦ください。

## 概要
多くなってしまったんで、先にまとめます。

### 筆者のポジション
- 今回問題になったMOD作者や配信者については未知 or 名前だけ知ってた
- 今回の問題と、については情報提供者
- 事前情報や予備知識なし。界隈のG＝ゴースティングを読めなかった（現在執筆中）

### 本稿の目的
- GPLライセンスを学ぼう
- 著作権を学ぼう
- ソフトウェアライセンスの問題の事例を見よう

（※）後述していますが、特定の個人や団体を批判する意図はありません。

### 注意
- 特定のMOD作者や配信者について言及しません
- SNSなどのエコーチェンバーを考慮しません

### 今日やること
- ソフトウェアライセンスを設定する意義
- ライセンス関連のリスク分析
- 社会学的に考えるソフトウェアライセンス

※社会学のスキルはマーケティングの片手間に多少齧った程度の知識しかありません。

### 今日やらないこと
- SNS問題
  - 善悪の判断
  - 特定への忖度
  - 批評・批判
  - ポジショントーク
  - 関係者の民度問題
- 問題解決、改善点の提起

執筆中も気をつけているのですが、誤解を与えそうな表現と感じるものがあれば、お手数ですがご教示いただけると嬉しいです。

### 情報ソース
- [Among Us アモアス MOD 日本語解説Wiki さま](https://wikiwiki.jp/amasmod)
- [reactor(開発環境構築)](https://docs.reactor.gg)
  - [fork元？(Github)](https://github.com/TheOtherRolesAU/TheOtherRoles)
- 今回の配信者や関連する配信者のチャンネルページ等

### 注意
（本稿では以下匿名とします）氏の作品を取得することができないため、作品のライセンスがGPLであるという根拠を確かめる事ができませんでした。
そこで、私の手元で同じ（であろう）開発環境を構築する際に、特定のThe Other Rolesをforkする手順で実施したところGPLライセンスだったので、これを踏襲しているものと考えていきます。

## そもそも、GPLライセンスとは？
[超分かりやすいサイト(正しく知れば怖くない GPL ライセンスの特徴|yamaryさま)](https://yamory.io/blog/about-gpl-license/)を置いておきますが、GPLライセンスを使用するソフトウェアの場合はライセンステキストが同梱または案内されているため、そちらを必ず参照して理解してください。

私からGPLライセンスの解説は今更やりません。

## ライセンスを設定する意義とは？
参考ページに分かりやすく書いていますが、GPLに限らず主要ライセンスについては「著作権があるプログラムのバグフィックスや拡張を第三者ができる権利」と考えると良いでしょう。
たとえばQiitaの記事などで言えば、陳腐化してしまったり内容の誤りをコメントや編集リクエストを出されると思います。
これは指摘したユーザーが正しくても、記事自体の著作権は著作者が持っているため、良かれと思ってやった事が法的（著作権的）にマズかった、というケースにならないようにするため、あくまで提案でしかないわけです。
提案を受けて著作者が記事を変更するも変更しないも、指摘したユーザーに意見する権利はありません。
ただし、いわゆる名誉毀損や誹謗中傷にあたると考えられる場合は、著作者だけでなく管理者（運営）に削除要請をする事ができます。

### そのコードは記事？プログラム？
問題をややこしくしているお話をもう一つ。
サンプルコードとして取り扱ったコードがあった場合です。
大体の場合は、取り扱いたいコードにライセンスがあればそちらを尊重し、その上で記事の著作者に帰属するという考え方ができそうです。
（個別具体なケースが考えられるため、あえて濁してあります）

このように、執筆当時の著作権は言った言わない問題に近い性質があり、それぞれの善意や曖昧な判断に基づく事がしばしばあります。
よく「ネットで拾ったソース」と気軽に表現していますが、そのソースは著作者が記事に書いたものであって、コード作成者が捨てたものではありません。

#### 転載対策として
悪魔のスクレイピング大流行時代で人様のサイトコンテンツを盗んだり盗まれたりしたアフィリエイト群雄割拠時代を生きてきたのでマジで言うんですが、こういう人に性善説を唱えても無駄です。見てすらいません。

ではどうするべきか？
スクレイピング対策をする手もありますが、一般ユーザーの利便性を犠牲にする事は許容するしかありません。
これはマウスドラッグ・右クリック禁止スクリプトと同じ考え方ですが、一部の悪質なユーザーのために大多数の善良なユーザーにも負荷をかける事がWebサイト運営者として正しい姿なのでしょうか？
取られない方法を頑張るより、取られた時に期待しない動作をさせた方がまだマシです。
一番手っ取り早いのは`.htaccess`などでアクセス制御をする方法でしょうか。

この辺りは調べると結構な数でてきます。
ユーザーの利便性とコンテンツの安全性のどちらを優先するか考えながらサイト作成をしてください。

#### 講師向け：「拾った」という言葉のイメージ
そもそも「ネットで拾った」という表現自体が正しくないのかもしれません。

マナー講師のようで気が引けるのですが、画像にしろコードにしろネットでダウンロードする事を「拾う」という表現は正しくないという意識づけを浸透させるしかないのかもしれません。
これは明らかな言葉狩りなので、教育の自由を奪う行為です。ご判断は各講師の方に委ねたいと思います。

## 本題：ソフトウェアの取り扱い
### Q. 一度公開し、既に利用者がいるプログラムを削除する事に問題があるか？
A. ないです。

ライセンスのどこにもそんな規定はありませんが、特記事項等があればこの限りではありません。
今回は著作者の判断によりソフトウェアの公開停止という形になりましたが、たとえば昔から開発しているソフトウェアが無期限の開発停止になったとして、誰が責められるのか？ということです。

ただし、やり方はあります。
無償提供とはいえ、予告期間なく突然使用禁止にしたり非公開にしたり、というのは、現状使っているユーザーへの配慮がないなぁ、と感じてしまいます。
私も開発者なので、自分が作ったものが意図しない使われ方をすると思うところはありますが、法に触れない限りは予告期間を設けるかなぁ…とは思います。
ただし、当事者ではなく第三者としての意見なので、そういう状況でなかった可能性もあります。
リアルタイムに見ていないので、外から適当なこと（私が考える一般だと思う論）を言っています。

### Q. 特定の利用者の利用を制限できるのか？
A. できません。
ライセンス云々の前に、実際問題としてそんなことできますかね？

たとえば、個人情報が流出したとして「流出した個人情報を取得しないでください」とお願いする事はできると思いますが、個人情報を取得できる状態にあるなら取得する人は絶対に出てきますよ。
個人情報というと抵抗感は高いですが、たとえばNovelAIの学習モデルが流出した事件がありました。
上記の個人情報をNovelAIの学習モデルに置き換えてみてください。これ絶対やってる人いるよね、って思いませんか？
また、リークの話とは無関係としても（本稿では著作権について言及したいので）NovelAIが学習したデータの著作権に問題があります。
とはいえ、問題があるからといって制限は不可能です。あくまでお願いとなります。

#### Q. 制限出来ないならやってもいい？
A. トラブルを回避したいなら避けましょう。

たとえば、流出した個人情報を取得してストレージになんて入れておいたら二次災害リスクや単純所持自体そのものがリスクになります。
個人情報だと１件あたりは大した事ない金額ですが、データ数でいえば間違いなくビッグデータと言えるので、個人で賠償するのは不可能な金額です。
流出時は重大な過失に該当するため、会社を倒産させて自己破産すればチャラになる、なんて事はないです。

NovelAIのケースは扱いが微妙なのでどうなるか断言しにくいですが、NovelAI自体にも問題がある事を留意してください。
私ならリスクがある以上は使わないです。

### Q. 今回の騒動の問題点とは何か？
A. （※）何もないです。

何も問題はないんですが、マナーやモラルとしてどうなの？という点では疑問です。
もしソフトウェアライセンスに「（※）お気持ち制度」が必要であれば、それを議論すればよいと思います。
どこかに但し書き（契約など）でもない限りは、基本的に作者が公開したものを非公開にしたりする事に異議を唱える権利はありません。

ただし、問題ないからOKとならないのも現実です。
冒頭で触れないと言いつつ若干触れてしまいますが、声が大きくなると正しさより（正しいか間違っているかは別にして）正義感が勝ってしまう事があるのもエコーチェンバー現象の恐ろしいところです。
この辺りは心理学の話になるのでこれ以上の言及は避けますが、対立する意見を受け入れられているか、自身を客観評価できているかは都度見直した方が良いかもしれません。

[Twitterのポストから自身が染まっていないか確認できる方法があるようです。](https://torilab.sakura.ne.jp/twitter/echamber/index.html)

## 生きにくいSNS時代を強く生きるメソッド例
普段から意識して「自分と反対意見を出す人」を耐えられる量の精神毒として相手方の代表格をフォローする手もあります。
分かりやすいところだとガノタなら連邦とジオンの両陣営だったり、きのことたけのこの両陣営だったり、vimとemacsなど色々です。
ガチ宗教の話もあるので踏み込むのがこわいですが、与党と野党（与党は党内でも左右に分かれており、意見を探すのが大変で、野党は党ごとに意見が統一されているが、各党で考え方が異なる）なんかは一番分かりやすく良い例だと個人的には思います。

何が言いたいかというと、特定のどこかに染まるのではなくて、別の意見や見方ができる環境を自分で作りましょうというお話です。
本稿ではGPLライセンスの扱いと著作権を主題に取り扱っていますが、他の意見が絶対あるはずなので、あなたが本稿に賛同でも反対でも違う人の考え方に触れてみてほしいと思います。

## 次の記事
- [(14日目) エンジニアが講師業を営んで学び得た哲学の話](https://qiita.com/nomurasan/items/7cff5b7816eb4d660a05)
- [カレンダーページ](https://qiita.com/advent-calendar/2022/oreno_nomurasan2022)
