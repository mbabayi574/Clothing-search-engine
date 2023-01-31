# Dockerize a Vite React app

# Node 18
FROM node:18-slim
WORKDIR /app
COPY package.json .
RUN npm i
COPY . .
EXPOSE 5173
CMD ["npm", "run", "dev"]