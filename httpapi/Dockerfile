FROM alpine:latest

COPY ./app/ /myApp/
RUN apk update && apk add py-flask uwsgi uwsgi-http uwsgi-python 

EXPOSE 5000

STOPSIGNAL SIGINT
CMD ["uwsgi","--plugins-dir","/usr/lib/uwsgi/plugins/","--plugins","python,http","--http","0.0.0.0:5000","--chdir","/myApp/","--wsgi-file","httoAPI.py","--callable","app","--master","--processes","4"]

