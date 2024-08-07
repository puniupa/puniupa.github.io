# [puniupa.github.io](https://puniupa.github.io)

![Publish](https://github.com/puniupa/puniupa.github.io/actions/workflows/publish.yml/badge.svg)
![Size](https://img.shields.io/github/repo-size/puniupa/puniupa.github.io.svg)
![License](https://img.shields.io/github/license/puniupa/puniupa.github.io.svg)

本リポジトリは，研究者の「ぷに」と法律家の「うぱ」の日々の勉強を綴ったブログです．

## ブログの更新方法

1. `/posts/20XX/Category` ディレクトリの中に新しいファイルを `blog.qmd` という形で作成し，記事を書き込む．
2. `git add .` で変更を追加する．
3. `git commit -m "added new posts"` で変更をコミットする．コメント "added new posts" は適宜変更．
4. `git push` で変更をプッシュする．

変更がプッシュされると，GitHub Actions により自動的にブログが更新され，公開されます．