FROM golang:alpine
RUN mkdir /go/src/coupon-qr-gen
WORKDIR /go/src/coupon-qr-gen
RUN apk update
RUN apk add git
ADD . /go/src/coupon-qr-gen
RUN go-wrapper download
