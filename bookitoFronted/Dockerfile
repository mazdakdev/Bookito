FROM node:16

RUN mkdir -p /var/www/web
WORKDIR /var/www/web

ADD . /var/www/web


ENV HOST 0.0.0.0
EXPOSE 3000

RUN yarn install

RUN yarn build
# start command
CMD [ "yarn", "start" ]
