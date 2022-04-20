# comments system
***

### settings

#### Install dependencies from requirements.txt

```
pip install -r requirements.txt
```

#### Run migrations
```
python manage.py migrate
```

#### Run project
```
python manage.py runserver
```
***
## API

### Users
##### get_users_list
```
GET api/users 
```
##### create_user
```
POST api/users
```

***
### JWT Token Authorization
```
Authorization: Bearer <token>
```

### Articles
##### get_articles_list
```
GET api/articles 
```
##### get_comments_by_article
```
GET api/articles/<int:id>/comments
```
***

### Comments system
##### get_nested_comments_by_parent_comment
```
GET api/comments/nested/<int:id>
```
##### create_comment
```
POST api/comments
```
***

### Authors 👨‍💻

Contributors names and contact info

ex. gdetam  
ex. [@gdetam](https://t.me/onlygdetam)

### License

This project is licensed under the [MIT License](LICENSE.txt)