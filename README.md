EN:
This is a standard blog.

The following models were used:
1) Django.User for authentication, registration.
2) Profile related OneToOneField to django.User.
3) Article related ForeignKey to Profile.
4) Comment related ForeignKey to Profile and Article.

Blog functionality:
1) Getting a list of posts in the amount of all posts / user posts / individual post.
2) Create / modify / delete a post.
3) Create comments to the post.
4) Authentication (login, logout), registration.
5) Displaying a page of a specific user with his posts.
6) Conclusion of all users.
7) Subscription to users.
8) Display of posts of your subscriptions.
9) Sending a letter to the mail with the post of the author to which you are subscribed.


RU:
Это стандартный блог.

Были использованы следующие модели:
1) Django.User для аутентификации, регистрации.
2) Profile, связанные OneToOneField с django.User.
3) Article, связанный ForeignKey с Profile.
4) Comment, связанный ForeignKey с Profile and Article.

Функционал блога:
1) Получение списка постов в количестве все посты/посты пользователя/отдельный пост.
2) Создание/изменение/удаление поста.
3) Создание комментариев к посту.
4) Аутентификация (вход, выход), регистрация.
5) Вывод страницы конкретного пользователя с его постами.
6) Вывод всех пользователей.
7) Подписка на пользователей.
8) Вывод постов своих подписок.
9) Отправка письма на почту с постом автора, на которого вы подписаны.
