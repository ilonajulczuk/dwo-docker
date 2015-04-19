# DWO - docker workshops

## Wstęp o co chodzi z dockerem.

Docker to technologia kontenerowa, zestaw narzędzi do tworzenia, dzielenia i uruchamiania kontenerów.

## Co to jest kontener?

Kontener:
kawałek systemu, który jest odizolowany od reszty i można mu ograniczyć przywileje
aplikacja wraz ze wszystkim co jest jej potrzebne do działania
coś co można startować, stoppować, monitorować, łączyć z innymi kontenerami (unikalny interfejs obsługi, nieważne co w środku jest)
kontenery są tworzone na podstawie obrazu

Obraz:

szablon od którego startowane są kontenery

Obraz można wypychać (push) / ściągać  (pull) za pomocą docker registry.

http://www.slideshare.net/atteroTheGreatest/introduction-to-docker-39816311

Jak korzystamy z Dockera?

Używając Docker CLI

```
$ docker --help
```

## Ściąganie obrazu z internetu

Żeby uruchomić kontener musimy mieć obraz na podstawie którego będziemy tworzyć kontener.

Obrazy ściągamy w następujący sposób:

```
$ docker pull busybox
$ docker pull ubuntu
$ docker pull python:3.4
```


Coś się stało, pościągaliśmy trochę obrazów, gdzie one są?
https://docs.docker.com/introduction/understanding-docker/

Jak zobaczyć jakie mamy obrazy dockerowe?

```
$ docker images
```

## Prosta komenda w kontenerze
Jak uruchomić coś w kontenerze?

```
$ docker run busybox echo “hello docker”
```

## Komenda Run

```
$ docker run -it ubuntu bash
```

ls, etc

## Montowanie wolumenów, forwardowanie portów, uruchamianie kontenerów w trybie zdemonizowanym


````
#!/bin/bash

for i in `seq 10`; do
    echo $i
    sleep 2
done
```
https://docs.docker.com/reference/commandline/cli/#run
Montowanie wolumenów - montujemy taki skrypt i próbujemy go odpalić.

Forwardowanie portów na podstawie obrazu python:3.4

```
$ python3 -m http.server
```

## Utrwalanie kontenerów na podstawie commitowania kontenera

```
$ docker commit container_name my-org/new_name
```


## Wstęp do Dockerfile'a (specyfikacji budowy obrazów dockerowych)

Przykład: Flask app - zbudujemy dla niej Dockerfile.

Dockerfile

```
# let's start from the image with python installed
FROM python:3.4

# Add file with dependencies to the container
ADD requirements.txt /code/requirements.txt

# Run a command inside a container
RUN pip install -r /code/requirements.txt

# set working diretory
WORKDIR /code

# copy code from current directory to /code
COPY . /code

# expose port from container
EXPOSE 5000

# default command that will be run in container
CMD python app.py
```

```
$ docker build -t attero/dwo-docker .
```

## Pierwsza aplikacja w Dockerowym kontenerze - linki.

Aplikacja wymaga do prawidłowego działania redisa. Połączymy redisa z naszym kontenerem za pomocą linków:

https://docs.docker.com/userguide/dockerlinks/

```
$ docker run -it -p 5000:5000 -v `pwd`:/code --link redis:redis attero/dwo-docker
```
