##Каталог отелей

###Запуск проекта:
docker-compose build, docker-compose up


###Описание запросов
  POST /api/accounts/users/login/ - вход юзера
  POST /api/accounts/users/logout/ -выход юзера из системы
  POST /api/accounts/users/register/ - регистрация юзера
  GET /api/hotels/?city_id=<city_id>&from_id=<hotle_id>&limit=<number>/ - получение списка отелей

