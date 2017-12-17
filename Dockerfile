FROM node:latest

WORKDIR ./userManager

ADD ./userManager /userManager

ENV PORT=3000
ENV MONGO_URL='mongodb://127.0.0.1:27017/devOps'

EXPOSE ${PORT}

RUN npm i

CMD ["npm", "start"]