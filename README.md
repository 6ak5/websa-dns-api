# websa-dns-api
Предоставляет возможность выпуска бесплатных сертификатов let's encrypt с помощью DNS аутентификации
в сервисе - https://websa.advancedhosters.com

Необходимо сгенерировать ключ api в панели сервиса и добавить его в конфигурационный файл settings.ini
После чего можно выпустить сертификат для списка доменов указанных в domain-list.conf
Каждый новый домен добавлять с новой строки.

Использование:

sudo apt install python3

sudo apt install certbot

git clone https://github.com/6ak5/websa-dns-api
cd websa-dns-api
./certbot_dns.py

Если dry-run проходит успешно то достаточно поставить # перед строкой --dry-run для начала выпуска сертификатов.

created by ah_puf
