# Описание базы данных

Для хранения данных было решено использовать NoSQL базу данных MongoDB.

## Схема

![Scheme](figs/instadb.png)

## Описание коллекций

### Users

В коллекции Users хранится информация о пользователях

```jsonc
{
    _id: ObjectId,     // _id объекта

    instaId: str,      // id пользозователя в Instagram
    instaName: str,    // имя пользозователя в Instagram
    imageThumb: str,   // превью аватарки (Base64)

    isPremium: bool,   // есть ли платная подписка
    isAdmin: bool,     // является ли администратором

    statsId: ObjectId, // _id статистики пользователя
    imageId: ObjectId, // _id аватарки
}
```

### Stats

В коллекции Stats хранится информация о постах пользователя

```jsonc
{
    _id: ObjectId,             // _id объекта

    posts_count: int,          // Общее количество постов
    posts_w_com_count: int,    // Количество постов с комментариями
    posts_positive_count: int, // Количество позитивных постов
    posts_frequency: int,      // Частота постов
    posts_emotion: float,      // Средняя эмоциональная окраска постов
    words_top_n: [             // N часто используемых слов
        str
    ]
}
```

### Images

В коллекции Images хранятся изображения

```jsonc
{
    _id: ObjectId, // _id объекта

    image: str,    // изображение (Base64)
    size: [        // размеры изображения
        int
    ]
}
```
