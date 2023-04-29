'''DRF -> django rest framework'''
# API -> (application programming interface)
# место соприкосновения клиента и сервер, предназначена для взатодействия между программами

'''REST (representational state transfer) - стиль API, стандарт, которому следует API'''

# принципы REST
# 1. разграничение клиента и сервера
# 2. отсутствие состояния (нет сохранения состояния) - сервер не должен хранить какую либо информацию о клиенте
# 3. кэширование
# 4. многоуровневая система
# 5. единый интерфейс
# 6. код предоставляется по запросу

#   RESTfull API -> API которое соответсвует принципам REST


# 1. Создаем виртуальное окружение Python3 -m venv venv

# 2 активируем виртуальное окружение . venv/bin/activate

# 3.создаем фаил req.txt
# записываем : Django, djangorestframework, psycopg2-binary

# 4. устанавливаем: pip3 install -r req.txt

# 5. djang-admin startproject <название> . -> создаем проект, если не поставим точку то у нас будет вложенность директрий

# 6. python3 manage.py startapp <app_name> - создание приложения

# 7. открываем файл settings.py в INSTALL_APPS -> регистрируем rest_framework, <app_name>

# 8. в файле settings.py настраиваем базу данных

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'test',
        'USER': 'user1',
        'PASSWORD': 123,
        'HOST': 'localhost',
        'PORT': 5432
    }
}
'''

# python3 manage.py makemigrations -> создает фаил миграций
# python3 manage.py migrate
# python3 manage.py createsuperuser - создание суперпользователя
# python3 manage.py runserver -> запуск проекта
# python3 manage.py runserver 8001

'''Models'''

# как проходит запрос
# 1. asgi/wsgi -> (те кто принимают запрос и возвращают отет)
# 2.  settings -> middlewares
# 3. urls -> маршутизаторы
# 4. views -> представления (функции, которые возвращают данные в нужном формате)
# 5. serializers (классы, которые переводят данные из json в python и наоборот)
# 6. models (классы, которые обозночают как будет выглядеть наша таблица в бд)
# 7. managers -> классы, которые работают с ORM
# 8. db -> база данных


#======= Поля =========
# 'CharField' -> для строкового значения(обязательно нужно указывать max_length)
# 'SlugField' -> для хранения slug (обычно используется в url) содержит только буквы, числа, -, _
# 'TextField' -> для хранения текста
# 'DecimalField' -> для дробных чисел(max_digit: кол-во цифр целой части, decimal_places (кол-во цифр после запятой))
# 'IntegerField' -> для чисел
# 'BooleanField' -> для bool значений
# 'DateField' -> для дат(datetime.date)(можно передать аргументы: auto_now -> обновляется при изменений, auto_now_add -> задается только один раз при создании
# 'TimeField' -> для времени (auto_now, auto_now_add)
# 'DateTimeField' -> для даты и времени
# 'EmailField' -> для email
# 'FileField' -> для файлов (upload_to -> указания директории где будет хранится фаил)
# 'ImageField' -> для картинок
# 'JSONField' -> для храниния строк в формате json

'''Ключевые параметры для полей (опциональные)'''
# null -> если True, будет в бд записывать null, если данные не переданы
# blank -> если True, будет ствыить пустую строку в бд, не обязательно для заполнения
# default -> значение по умолчанию
# unique -> если True, в колонке могут хранится только уникальные значения
# primary_key -> если True, первичный ключ - идентификатор
 # choices -> список с tuple (ограничеваем возможные варианты для заполнения)
 

'''fuser -k 8000/tcp'''

'''========== связи ========'''
#ForeignKey -> связи один ко многим (обязательно указать модельна которую мы будем ссылаться, on_delete, 
# related_name - для обратной связи)

#ManyToManyField - многие ко многим (все тоже самое, что и ForeignKey)


'''========== on_delete - обязательный параметр ========='''
# models.CASCADE -> каскадное удаление(если удаляется главный обьект, то удаляется и зависящие от него)
# models.PROTECT -> вызывает ошибку при попытке удалить главный обект
# models.SET_NULL -> не удаляет зависящие обьекты, а ставит null (null=True)
# models.SET_DEFAULT -> если определен default, то ставится его
# models.DO_NOTHING -> ничего не делает, вызывается ошибка

# c = Category(title = 'sport')
# c.save()
# p = Post(title='hello', text='', category=c)
# p.save()

# p1 = Post.objects.create(title='hello2', text='', category=c)

# SELECT * FROM test2_post WHERE id =1;
# SELECT * from test2_post;
# SELECT text FROM test2_post;

# SELECT COUNT(*) FROM test2_post

# Product.objects.all()
# # SELECT * FROM products;

# Product.objects.get(id=1)
# SELECT * FROM products WHERE id = 1;

# Product.objects.filter(условие1, условие2)
# SELECT * FROM products WHERE условие AND условие2;

# Product.objects.filter(Q(условие)|Q(условие2))
# SELECT * FROM products WHERE условие1 OR условие2;

# Product.objects.filter(~Q(условие))
# Product.objects.exclude(условие)
# SELECT * FROM products WHERE NOT условие;

# Product.objects.filter(price__gt=50000) #больше
# SELECT * FROM products WHERE price > 50000;

# Product.objects.filter(price__lt=50000) #меньше
# SELECT * FROM products WHERE price < 50000;

# Product.objects.filter(price=50000) #равно
# SELECT * FROM products WHERE price = 50000;

# Product.objects.filter(~Q(price=50000))
# SELECT * FROM products WHERE NOT price = 50000;

# Product.objects.filter(price__gte=50000)
# SELECT * FROM products WHERE price >= 50000;

# Product.objects.filter(price__lte=50000)
# # SELECT * FROM products WHERE price <= 50000;

# # Product.objects.filter(category_id__in=['phones', 'notebooks'])
# # SELECT * FROM product WHERE category_id IN ('phones', 'notebooks');

# # Product.objects.filter(price__range=[20000, 50000])
# # SELECT * FROM products WHERE price BETWEEN 20000 AND 50000;

# Product.objects.filter(name__exact='Iphone')
# # SELECT * FROM products WHERE name LIKE 'Iphone';
# Product.objects.filter(name__iexact='Iphone')
# # SELECT * FROM products WHERE name ILIKE 'Iphone';

# Product.objects.filter(name__startswith='Iphone')
# # SELECT * FROM products WHERE name LIKE 'Iphone%';
# Product.objects.filter(name__istartswith='Iphone')
# # SELECT * FROM products WHERE name ILIKE 'Iphone%';

# Product.objects.filter(name__contains='Iphone')
# # SELECT * FROM products WHERE name LIKE '%Iphone%';
# Product.objects.filter(name__icontains='Iphone')
# # SELECT * FROM products WHERE name ILIKE '%Iphone%';

# Product.objects.filter(name__endswith='Iphone')
# # SELECT * FROM products WHERE name LIKE '%Iphone';
# Product.objects.filter(name__iendswith='Iphone')
# # SELECT * FROM products WHERE name ILIKE '%Iphone';

# Product.objects.order_by('price')
# # SELECT * FROM products ORDER BY price ASC;

# Product.objects.order_by('-price')
# # SELECT * FROM products ORDER BY price DESC;

# Product.objects.only('name')
# # SELECT name FROM products;

# Product.objects.only('name', 'price') #запрашивает указанные поля
# # SELECT name, price FROM products;

# Product.objects.defer('name', 'price') #исключает указанные поля
# # SELECT id, description, category_id FROM products;

# Product.objects.count()
# # SELECT COUNT(*) FROM products;

# Product.objects.filter(...).count()
# # SELECT COUNT(*) FROM products WHERE ...;

# Product.objects.create(name='Apple Iphone 12',
#                        description='awddwdawd',
#                        price=78000,
#                        category_id='phones')
# # INSERT INTO products (name, description, price, category_id) VALUES \
#     # ('Apple Iphone 12', 'dwadaafafaw', 78000, 'phones');

# Product.objects.bulk_create([
#     Product(...),
#     Product(...)
# ]) #множественное создание

# Product.objects.update(price=50000)
# # UPDATE products SET price=50000;

# Product.objects.filter(...).update(price=50000)
# #UPDATE products SET price=50000 WHERE ...;

# Product.objects.filter(id=1).update(price=50000)
# #UPDATE products SET price=50000 WHERE id=1;

# product = Product.objects.get(id=1)
# product.price = 50000
# product.save()

# Product.objects.delete()
# DELETE FROM products;

# Product.objects.filter(category_id='phones').delete()
# DELETE FROM products WHERE category_id = 'phones';

# Product.objects.filter(id=1).delete()
# DELETE FROM products WHERE id=1;

# product = Product.objects.get(id=1)
# product.delete()


'''related_name'''
# позволяет обращаться из связанных обьектов к тем, от которых эта связь создана (для обратного поиска) 
# related_name -> создает связь с обратной стороной 

# cat = Category.objects.get(id=1)
# cat.posts.all() -> получение всех постов, относящихся к данной категории.

'''related_query_name = post'''
# создает именнованный атрибут, который позволяет делать запросы с импользованием 
# метода perfetfh_related - загружает связвнные обьекты (оптимизирует запросы в бд)

# cat.post.all()

# QuerySet -> обьекты полученный с базы данных, благодаря manager'y (objects)
# Manager - > класс, предоставляет методы для доступа к ORM Django(отправляет запросы в бд)
# default (manager) = objects
# (обновляем, получаем, удаляем, фильтруем данные из таблиц)
