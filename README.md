## What is this
都道府県市町村コードからメッシュコードなどを取得出来るAPIです
リクエストとレスポンスの対応は以下の表のとおりです

## API URL
```
//1次、2次、3次メッシュコード
https://kanahiro.github.io/lgcode-api/1meshcodes/{都道府県市町村コード}
https://kanahiro.github.io/lgcode-api/2meshcodes/{都道府県市町村コード}
https://kanahiro.github.io/lgcode-api/3meshcodes/{都道府県市町村コード}

//自治体名
https://kanahiro.github.io/lgcode-api/name/{都道府県市町村コード}
```

## Request and Response
|  Req  |  Res  |
| ---- | ---- |
|  https://kanahiro.github.io/lgcode-api/1meshcodes/  |  to-meshcodesの全データ { lgcode:1次メッシュコード一覧(array) }  |
|  https://kanahiro.github.io/lgcode-api/2meshcodes/01  |  指定された都道府県の2次メッシュコード一覧(array)  |
|  https://kanahiro.github.io/lgcode-api/3meshcodes/01220  |  指定された市町村の3次メッシュコード一覧(array)  |
|  https://kanahiro.github.io/lgcode-api/name/  |  to-lgnameの全データ { lgcode:自治体名(str) }  |
|  https://kanahiro.github.io/lgcode-api/name/01  |  指定された自治体の名前(str)  |

## DataSource
- 市町村別メッシュコード一覧: https://www.stat.go.jp/data/mesh/m_itiran.html