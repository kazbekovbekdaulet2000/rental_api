
# API для аренды товаров разного вида (камеры, машины для разных нужд и тд)

# Class Diagram
![alt text](https://github.com/kazbekovbekdaulet2000/rental_api/blob/master/materials/class_diagram.png)

# Авторизация
JWT (Simple JWT) - так как там встроен токены для access/refresh
Django roles - tenant, landlord (арентодатор, арентодатель )
Поля для usera - email, name, surname, firstname, birthdate 
Сброс пароля через email

![alt text](https://github.com/kazbekovbekdaulet2000/rental_api/blob/master/materials/auth_openapi.png)

# Вход
Арендатор и Арендодатель проходят авторизацию в одном окне, без переключения режима авторизаций (tentor или lessor), вводится Email, Пароль. Отличия tentor от lessor проявляются в user permissions и типе доступных запросов после авторизаций. 

# Добавление в Избранные, лайк
У tenant и у landlord будет свой список избранных объявлении и лайков, для всех записей должен быть created_at, updated_at чтобы определить когда был лайк или когда запись была добавлена в список моделька через Contenttypes чтобы не только товар можно было добавлять в эти списки

# Товар 
У товара должна быть категория, фотографии, название, описание, и запись для хранения время аренды и ее деталей чтобы определять по дате свободен ли этот товар для аренды, человек который отправил запрос, храниться в отдельно чтобы lessor мог просматривать этот список для отдельного товара, и при добавлении запроса на аренду (фактическая аренда) записи остаются но принятый запрос уходит в архив
	Только Lessor может добавлять удалять и менять товар (если это его товар)

# Категория 
Для построения иерархии категории будут поле для foreign key родительского класса, также название, описание, количество товаров который будет меняться через signal при появлении или удалении товаров, а также рекурсия чтобы менять количество и у родительских если они есть

# Комментарий
Так как комментарии через contenttypes то можно отвечать на комментарии (как в форумах), можно оставлять лайк, добавлять в избранное, полная crud операция если комментарии является его

# Похожие обновления
Товары берутся от категории и/или ее родительских категории если количество товаров в категории меньше чем 10

# Отзыв и рейтинг
Человек который брал товар может оставить отзыв и рейтинг, который через signal будет менять profile landlord то есть меняется поле рейтинг

![alt text](https://github.com/kazbekovbekdaulet2000/rental_api/blob/master/materials/shop_openapi.png)
