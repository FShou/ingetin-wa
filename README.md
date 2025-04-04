# IngetinWA
A simple whatsapp message scheduler, you can schedule your whatsapp message with ease. This project powered by [WAHA](https://github.com/devlikeapro/waha) for whatsapp connection.

![Screenshot 2025-04-04 at 13-30-35 IngetinWA](https://github.com/user-attachments/assets/8d678103-f12f-41eb-9314-4c7d53f386eb)

see demo here: [http://103.59.160.35/](http://103.59.160.35/)
- Username: `admin`
- password: `admin`

> **Warning:** Right now only support one whatsapp account for the whole project i.e your whatsapp account **might be used by others** in this demo!


## Usage
1. run the required service
   
   ```
   docker compose up
   ```
1. run django app and huey for the task queue

   ```sh
   python3 ./manage.py run_server &
   python3 ./manage.py run_huey
   ```

## TODOS
- [ ] Support for per User Whatsapp account
