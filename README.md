# wedding_ioan_warua
wedding.conf

    server {

    listen 80;
    server_name weddding.ru;  # Ваш IP-адрес
    location / {
        proxy_pass http://localhost:8080;  # Проксирование на ваше приложение
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    proxy_connect_timeout 60s;
    proxy_read_timeout 90s;
    client_max_body_size 100M;
    
    }

    sudo certbot --nginx -d weddding.ru     --register-unsafely-without-email
