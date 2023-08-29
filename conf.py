# sphinxでビルドするために必要なファイル

# ドキュメントの言語を指定（日本語の場合は'ja'）
language = 'ja'

# プロジェクトのタイトル
project = 'Qiita to Zenn'

# プロジェクトの著者
author = 'nomuraya'

# ドキュメントのバージョン
version = '1.0'
release = '1.0'

# -- Extensions ----------------------------------------------------------

# autodoc拡張機能を有効にする
extensions = ['sphinx.ext.autodoc']

# -- Options for HTML output ----------------------------------------------

# テーマの設定（例えばsphinx_rtd_themeを使用する場合）
html_theme = 'sphinx_rtd_theme'

# インデックスページのドキュメント
master_doc = 'index'

# -- Options for autodoc extension ----------------------------------------

# ドキュメント化するモジュールのパスを追加
# ファイル名は拡張子を除いたものを指定
# 例: 'backup_qiita_articles' と 'publish_to_zenn'
autodoc_mock_imports = ['backup_qiita_articles', 'publish_to_zenn']
