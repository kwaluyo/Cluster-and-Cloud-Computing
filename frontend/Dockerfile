# Stage build
FROM node:12 as builder

# use proxy
ENV http_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV HTTP_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV HTTPS_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV no_proxy localhost,127.0.0.1,localaddress,172.16.0.0/12,.melbourne.rc.nectar.org.au,.storage.u nimelb.edu.au,.cloud.unimelb.edu.au

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
