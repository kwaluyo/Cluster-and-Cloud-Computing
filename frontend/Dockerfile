# Stage build
FROM node:12 as builder

WORKDIR /app/frontend

#Copy Package 
COPY  . .

RUN npm install 

RUN npm run build 

# Stage runtime application
FROM nginx:stable-alpine
COPY --from=builder /app/frontend/build /usr/share/nginx/html
COPY --from=builder /app/frontend/nginx.conf /etc/nginx/conf.d/default.conf
RUN touch /var/run/nginx.pid && \
  chown nginx:nginx /var/run/nginx.pid &&\
  chown  -R nginx:nginx /var/cache/nginx
USER nginx
EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
