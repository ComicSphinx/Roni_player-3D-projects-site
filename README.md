# TODO LIST && HOW WHAT SHOULD WORKS
## MVP TODO:
1. Восстановление удаленных постов
2. Добавить возможность отмечать главную картинку (по аналогу с инпутом отображать чекбокс или вроде того. Там, где чекбокс активен - ту картинку и загружать, в main поле(есть вариант отправлять картинку в 8 индексе, чтобы не париться с кодом, это задача чисто JS))
3. Сделать: либо, чтобы при создании/удалении/редактировании карточки презентации админа не кидало на сервис db, либо, чтобы из него можно было вернуться обратно в админскую панель
4. У меня сервис базы данных доступен кому угодно. Это небезопасно. (Мб сделать его по sessionId или еще как)

## Задачи на рефакторинг
1. deletePresentations
2. updatePresentation
2. Сделать, чтобы нельзя было перейти по id в карточку не активной презентации

## Задачи на промышленную эксплуатацию
1. Провести нагрузочное тестирование
2. Отключить debug=True
3. Поменять ссылки методов на относительные, типа /createPresentation вместо http://127.0.0.1:80/CreatePresentation, или вообще всё это как-то переделать

## Как запустить в пром
1. При запуске в пром запустить GeneratePassword.py, пароль для админки сгенерится в файл - password.txt
2. В admin service (там же, где и password.txt), положить файл username.txt, в него записать логин админа входа в админку
3. Запустить initDb.py в database
4. Отключить debug=True во всех сервисах