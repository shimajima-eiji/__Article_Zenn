---
title: "pythonで任意の場所に文字を挿入したい！（関数・ラムダ式でも書いてみた）"
emoji: "📝"
type: "tech"
topics: ["Python"]
published: true
---

:::message
この記事はQiitaから移行しています。
:::

https://qiita.com/items/d68ed63a7dae897eda7c

-----

## お詫び
Qiitaの元記事にて、区切り線を「---」で書いている場所があり、これがZennの記法に干渉して一部うまく表示できない記事がある事を認識しています。
全ての記事を精査しきれていないため、お手数ですがお見かけの際は教えていただけると大変喜びます。

-----

``` code
base_string = 'test'
INSERT_POINT = 2  #分かりやすくするために大文字
insert_string = '--hoge--'

# 2文字目から挿入したい場合
print '{0}{1}{2}'.format(base_string[:INSERT_POINT], insert_string, base_string[INSERT_POINT:])
```

これの結果は
**te--hoge--st**
となります。

# 応用
``` code
def insert_string_to_base(target_string, insert_point, insert_string):
    return target_string[:insert_point] + insert_string + target_string[insert_point:]
```

とすると関数で使えるし、

``` code
insert_string_to_base = lambda base_string, insert_point, insert_string : base_string[:insert_point] + insert_string + base_string[insert_point:]
```

とするとラムダ式になります。
どちらも、

``` code
base_string = 'test'
INSERT_POINT = 2  #分かりやすくするために大文字
insert_string = '--hoge--'

# lambdaで見たい場合は予め上記コードをここに書いておく

# 出力
print insert_string_to_base(base_string, INSERT_POINT, insert_string)
```

で結果を参照できます。

