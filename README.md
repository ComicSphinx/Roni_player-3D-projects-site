# TODO LIST && HOW WHAT SHOULD WORKS
## Как это должна работать карточка презентации с т.з. фронта
1. Пользак переходит на карточку презентации, в url есть параметр - id.
2. Фронт отправляет GET запрос на бэк с параметром Id из урла и подтягивает все необходимые данные (заголовок, описание, картинки)
3. Отрисовывает данные

## Как должна работать карточка презентации т.з. бэка
1. Бэк получает запрос GET presentation/{id}
2. Делает запрос В БД в таблицы presentation/image и тянет оттуда все изображения и их идентификаторы (где какая картинка должна располагаться), примерно такой запрос:
SELECT imagePosition, image FROM presentations WHERE presentationId={id}
3. Делает запрос в БД и тянет оттуда текстовые данные
SELECT description, title FROM presentation.texts WHERE presentation_id={id}
4. Возвращает их в ответе на запрос

## Как должен работать список презентаций с т.з. фронта
1. Пользак переходит на карточку презентации
2. Фронт отправляет GET запрос на получение осн. информации о списке сущностей(необходимые поля - count, listPresentationIds)
3. Фронт отправляет GET /presentationImage/id/mainImage запрос на получение изображений (в зависимости от count, сколько count, столько и запросов, где id(i++))
4. Отображение карточек - сколько карточек пришло с бэка, столько отобразили
5. Плюс надо подумать, как реализовать роутинг и привязку отображаемых картинок к самим презентациям

## Как должен работать список презентаций с т.з. бэка
1. Получает запрос GET presentationsList
2. Делает запрос в БД:
SELECT presentationId, count(presentationId) FROM presentation WHERE active=true
3. Возвращает ответ в JSON формате
4. Получает запрос GET /presentationImage/id/mainImage
5. Делает запрос в БД:
SELECT mainImage FROM presentations WHERE presentationId={id} AND active=true
6. Возвращает

## MVP TODO:
1. Отрегулировать изображения в адмнике
2. Надо сделать уникальными записи по полю presentation_id и можно сделать это поле первичным ключом
3. Под каждую карточку презентации можно создавать отдельную папку, чтобы изображения не валялись в куче. Плюс, не надо будет хранить в базе пути к изображениям. Ты просто загружаешь их по-очереди, от первого к последнему, они именуются как 1.jpg, 2.jpg ... И в таком же порядке возвращаются на фронт. И админить так проще будет (это как вариант. Обдумать его)
4. Добавить обработку тегов в описании, типа <i>, <b> и т.д. в описании
6. Реализовать механизм удаления(деактивации) и редактирования постов, проставлять active=false либо через UI, либо через бэк, если это будет удобно (можно замутить через бэк безопасным способом - принимать поле password, если в запросе пришел корректный пароль - деактивировать. Сойдет для начала)


## Todo
1. Сделать красивое отображение урла и обновление странички при изменении аргумента (Id презентации)
2. Сделать presentationId первичным ключом
3. Реализовать систему обработки ошибок на бэке (если данные не найдены и прочее)
4. Адаптация под мобильные устройства
5. Как делать бэкап, когда сайт будет лежать в облаке?
6. Почему createPresentation открывается с "?" - он не должен принимать никаких аргументов. Хотя, мб это из-за того, что метод может принимать POST, хотя сам браузер отправляет такой запрос

## Задачи на рефакторинг
1. Метод GET presentationsList - он ведь не возвращает список презентаций - он возвращает id[] и count
2. Функция в admin-service.previewImage.js readAndSetImage

## Задачи на промышленную эксплуатацию
1. Провести нагрузочное тестирование
2. Отключить debug=True
3. При запуске в пром запустить GeneratePassword.py, пароль для админки сгенерится в файл - password.txt