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

    # Link: https://www.grpc.io/docs/quickstart/go/
go get -u google.golang.org/grpc
go get -u github.com/golang/protobuf/protoc-gen-go
go get google.golang.org/grpc


go mod vendor

source ja_create_golang_env.sh
protoc -I proto proto/user_proto.proto --go_out=plugins=grpc:proto
# --go_out=paths=source_relative:.
protoc  proto/user_proto.proto --go_out=paths=source_relative:.

cd ja_go/log_test
go build
./log_test 
#Output:
    #  2020/02/27 16:12:46 [Jean]: I am backend.
    #  2020/02/27 16:12:46 [Jason]: I am api-layer
    #  2020/02/27 16:12:46 [Mary]: I am frontend.
    #  2020/02/27 16:12:46 -------logrus-----------
    #  INFO[0000] [Jean]: I am backend.                        
    #  WARN[0000] [Jason]: I am api-layer                      
    #  FATA[0000] [Mary]: I am frontend. 
    

