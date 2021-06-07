from django.contrib.auth.models import User
from django.core.mail import send_mail


def change_form_parameters(form, user, article=None):
    """
    Изменяем параметры формы.
    Чтобы их изменять на данной стадии, нужно сделать параметр _mutable = True.
    """
    _mutable = form.data._mutable
    form.data._mutable = True
    form.data['author'] = user
    if article is not None:
        form.data['article'] = article.id
    form.data._mutable = _mutable


def send_mail_message(author, title_post, text_post):
    """
    Отправляем письмо по почте при создании поста, если пользователи подписаны на его автора.
    """
    heading_message = 'Новый пост от %s' % author
    message = '%s сделал следующий пост:\n\nЗаголовок:%s\nТекст:%s' % (author, title_post, text_post)
    emails_to_send = [User.objects.get(id=i).email for i in author.my_subscribers.split()]
    send_mail(heading_message, message, 'blog.fbv.2.1@gmail.com', emails_to_send)


def redirect_after_delete(referer_page):
    """
    Флаг определяет возможность редиректа на страницу, с которой удалили пост.
    """
    index_first_slash_from_end = referer_page.rfind('/')
    index_second_slash_from_end = referer_page[:index_first_slash_from_end].rfind('/')
    desired_part_of_url = referer_page[index_second_slash_from_end - 9:index_second_slash_from_end]
    if desired_part_of_url == '8000/post':
        return False
    else:
        return True


def change_article(post, form):
    """
    Изменяет атрибуты статьи по новым атрибутам, полученных из формы.
    """
    post.title = form.data['title']
    post.text = form.data['text']
    post.rubric = form.data['rubric']
    post.save()
