# Stage build
FROM node:12 as builder

WORKDIR /app/frontend

#Copy Package 
COPY package*.json ./

RUN npm install

# Bundle app source
COPY . .

EXPOSE 3000
CMD ["npm", "run", "start"]