FROM node:6
RUN mkdir /application
WORKDIR /application
ADD . /application
RUN chmod +x /application/entrypoint.sh
RUN npm i
