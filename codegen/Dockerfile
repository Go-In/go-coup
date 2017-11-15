FROM golang:alpine
RUN mkdir /go/src/codegen
WORKDIR /go/src/codegen
RUN apk update
RUN apk add git
ADD . /go/src/codegen
