FROM node:latest

WORKDIR ./userManager

ADD ./userManager /userManager

ENV MONGO_URL='mongodb://127.0.0.1:27017/devOps'

EXPOSE 3000

RUN npm i

CMD ["npm", "start"]