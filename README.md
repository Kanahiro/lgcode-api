## What is this
都道府県市町村コードからメッシュコードなどを取得出来るAPIです
リクエストとレスポンスの対応は以下の表のとおりです

## API URL
```
https://kanahiro.github.io/lg-meshcode-api/lgcode-to-meshcodes/{都道府県市町村コード}/{nameかmeshcodes}
https://kanahiro.github.io/lg-meshcode-api/lgcode-to-lgname/{都道府県市町村コード}
```

## Request and Response
|  Req  |  Res  |
| ---- | ---- |
|  https://kanahiro.github.io/lg-meshcode-api/lgcode-to-meshcodes/  |  lgcode-to-meshcodesの全データ  |
|  https://kanahiro.github.io/lg-meshcode-api/lgcode-to-meshcodes/01  |  { "name":自治体名(str), "meshcodes":2次メッシュコード一覧(array) }  |
|  https://kanahiro.github.io/lg-meshcode-api/lgcode-to-meshcodes/01/meshcodes/  |  都道府県市町村コード01:北海道の2次メッシュコード一覧(array)  |
|  https://kanahiro.github.io/lg-meshcode-api/lgcode-to-lgname/  |  lecode-to-lgnameの全データ { lgname:自治体名(str) }  |
|  https://kanahiro.github.io/lg-meshcode-api/lgcode-to-lgname/01  |  自治体名(str)  |

## DataSource
- 市町村別メッシュコード一覧: https://www.stat.go.jp/data/mesh/m_itiran.html