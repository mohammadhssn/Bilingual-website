# SlideShow-OwlCarousel-Django

~~~
python -m venv venv
source .venv/bin/activate
~~~

pip install -r requirements.txt

cd SlideShow

mv .env-sample .env

python manage.py migrate

NOTE:
    ```python manage.py collectstatic
    ```

python manage.py createsuperuser
