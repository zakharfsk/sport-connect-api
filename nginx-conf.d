upstream app {
    server server:8000;
}

server {
    listen 80;
    server_name localhost;
    location / {
        proxy_pass http://app;
    }

    location /static/ {
        autoindex on;
        alias /static;
    }

    location /media/ {
        autoindex on;
        alias /media;
    }
}
