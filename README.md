# kanobu

Для старта проекта выполните docker-compose up
При работе на локальной машине для работы с запущенным проектом доступны команды:
 - http://127.0.0.1:8000/likes/allposts/ - просмотреть всех новостей и постов (метод GET)
 - http://127.0.0.1:8000/likes/allposts/int/ - просмотреть 1 запись, у которой id = int
 - http://127.0.0.1:8000/likes/allposts/int/action/ - для записи, у которой id = int:
 - - поставить like, если action = like
 - - поставить dislike, если action = dislike
