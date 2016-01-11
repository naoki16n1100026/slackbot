slack_bot.py  
====
  
## 紹介  

Slackを使って画像を投稿。  
詳細はこちらのブログで。  
  
http://qiita.com/kinpira/items/bf1df2c1983ba79ba455
  
### 準備

プロジェクト内にTOKEN定数を持った「private.py」を作成します。

slackbot/private.py

```python

TOKEN="xxxxxxx-xxxxxxx-xxxxxxxx-xxxxxxxx"

```

### コマンド
第一引数に対象となるfile pathを指定してください。

```
python slackbot/slack_bot.py "file/to/path"
```

***

こちらを参考にしています。
https://github.com/umentu/slackbot/
