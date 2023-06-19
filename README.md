# websa-dns-api
Предоставляет возможность выпуска бесплатных сертификатов let's encrypt с помощью DNS аутентификации
в сервисе - https://websa.advancedhosters.com<br>

Необходимо сгенерировать ключ api в панели сервиса и добавить его в конфигурационный файл settings.ini<br>
После чего можно выпустить сертификат для списка доменов указанных в domain-list.conf<br>
Каждый новый домен добавлять с новой строки.<br>
<br>
Использование:<br>
<br>
sudo apt install python3<br>
sudo apt install certbot<br>
<br>
git clone https://github.com/6ak5/websa-dns-api<br>
cd websa-dns-api<br>
./certbot_dns.py<br>
<br>
Если dry-run проходит успешно то достаточно поставить # перед строкой --dry-run для начала выпуска сертификатов.<br>
<br>
Requirements:
Python 3.6 or higher.
<br>

created by puf
