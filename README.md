# test-httpserver-py

受け取ったヘッダーを返すだけのサーバー

[httpbin.org](https://hub.docker.com/r/kennethreitz/httpbin/) は便利なのだけれど
`X-Forwarded-For` や `X-Forwarded-Proto` が消えてしまって確認できないためこれを書いた
