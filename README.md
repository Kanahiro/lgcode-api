## What is this
都道府県市町村コードからメッシュコードなどを取得出来るAPIです
リクエストとレスポンスの対応は以下の表のとおりです

## API URL
```
https://kanahiro.github.io/lgcode-api/to-meshcodes/{都道府県市町村コード}
https://kanahiro.github.io/lgcode-api/to-lgname/{都道府県市町村コード}
```

## Request and Response
|  Req  |  Res  |
| ---- | ---- |
|  https://kanahiro.github.io/lgcode-api/to-meshcodes/  |  to-meshcodesの全データ { lgcode:2次メッシュコード一覧(array) }  |
|  https://kanahiro.github.io/lgcode-api/to-meshcodes/01  |  指定された自治体の2次メッシュコード一覧(array)  |
|  https://kanahiro.github.io/lgcode-api/to-lgname/  |  to-lgnameの全データ { lgcode:自治体名(str) }  |
|  https://kanahiro.github.io/lgcode-api/to-lgname/01  |  指定された自治体の名前(str)  |

## DataSource
- 市町村別メッシュコード一覧: https://www.stat.go.jp/data/mesh/m_itiran.html