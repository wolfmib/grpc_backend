#!/bin/bash
go run ja_go/main.go

go get "github.com/sirupsen/logrus"
go env GOPATH
    # [Air Device]: /Users/johnny_hung/Gitlab/ja_go
rm -rf /Users/johnny_hung/Gitlab/ja_go/src/github.com/sirupsen/
echo "rm -rf ~/go/pkg as well..."

go mod init
go run ja_go/main.go 
    # in go.mod
        # module github.com/wolfmib/grpc_backend
        # go 1.12
        # Add by running new code, download automatically
        # require github.com/sirupsen/logrus v1.4.2 // indirect
