# telesender
Скрипт для массовой рассылки в Telegram

## Установка
### Переместиться в директорию проекта
`cd telesender`
### Установить виртуальное окружение
`python3 -m venv venv`
### Активировать виртуальное окружение
`source venv/bin/activate`
### Установить зависимости
`pip install -r requirements.txt`
## Использование
### Скопировать пример файла конфигурации
Не забудь убрать `example` из названия.

`cp config/input.example.yaml config/input.yaml`
### Настроить конфигурацию
Изменить содержание файла `input.yaml` на собственные данные:
```yaml
# Персональные Telegram API ключи
api_keys:
  api_id: your_api_id_here
  api_hash: your_api_hash_here

# Имя пользователя в Telegram, от лица которого будут идти сообщения
sender: username

# Список адресатов в виде username-ов пользователей Telegram
target_users:
  - user_1
  - user_2

# Текст отправляемого сообщения
message: The message you want to send
```
### Запустить скрипт командой
`python telesender.py run`

При первом запуске скрипта, телеграм запросит номер пользователя и код, 
который будет выслан. Например:
```shell
>> python telesender.py run
Please enter your phone (or bot token): 89991117733
Please enter the code you received: 88855
Signed in successfully as Имя Фамилия
```
После первого запуска, скрипт создаст файл сессии `username.session`. 
Пока есть файл сессии пользователя, повторная авторизация не потребуется.

Скрипт разошлёт сообщение по списку пользователей из файла `input.yaml` и остановится.
### Несколько файлов входных данных
Можно создать несколько копий файла `input.yaml` и при запуске указывать нужный файл
с входными данными. Тогда команда будет выглядеть так:

`python telesender.py run путь/к_файлу/input.yaml`

Название файла `input.yaml` конечно же может быть любым, главное соблюсти формат, именования и типы данных.