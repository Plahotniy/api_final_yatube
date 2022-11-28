# Api for YaTube
## Api based on Django_Rst_Framework

### This API is designed to work with the Youtube social network.
### With it, you can create and edit posts, leave comments and subscribe to other authors.

How to start a project:
Clone the repository and go to it on the command line:

git clone git@github.com:Plahotniy/api_final_yatube.git
cd api_final_yatube
Create and activate a virtual environment:

python3 -m venv env
If you have Linux/mac OS

source env/bin/activate
If you have windows

source env/scripts/activate
python3 -m pip install --upgrade pip
Install requirements from a file requirements.txt:

pip install -r requirements.txt
Make migrations:

python3 manage.py migrate
Start a project:

python3 manage.py runserver

request example:
+ GET http://127.0.0.1:8000/api/v1/posts/ - all posts
+ GET http://127.0.0.1:8000/api/v1/posts/{id}/ - one post
+ GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/ - all post's comments
+ GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/ - one post's comment
+ GET http://127.0.0.1:8000/api/v1/groups/ - all groups
+ GET http://127.0.0.1:8000/api/v1/groups/{id}/ - one group
+ GET http://127.0.0.1:8000/api/v1/follow/ - all follows
+ POST http://127.0.0.1:8000/api/v1/posts/ - create post
+ POST http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/ - create comment
+ POST http://127.0.0.1:8000/api/v1/follow/ - create follow
