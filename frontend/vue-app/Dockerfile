FROM node:14-alpine

WORKDIR /frontend

COPY . /frontend 

RUN npm install


RUN npm run build

EXPOSE 8080

CMD ["npm", "run", "serve"]
