# MapReduce
## 1. После клонирования репозитория необходимо перейти в папку master

   1.1 Создать образ докер:
   
      > docker build -t master .
   
## 2. Перейти в папку fastapi_slave

   2.1 Создать образ докер:
   
   > docker build -t slave .
   
## 3. Запустить контейнеры:

   3.1 Запуск slave`ов:
   
   > docker run -d -p 8000:8000 --name slave1 slave
   
   > docker run -d -p 9000:8000 --name slave2 slave
   
   3.2 Запсука master:
   
   > docker run --network=host --name master -it master bash
   
## 4. Ввести в терминале:

   > python master.py https://en.wikipedia.org/wiki/Horizon_Zero_Dawn https://en.wikipedia.org/wiki/Guerrilla_Games
