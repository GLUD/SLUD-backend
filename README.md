# SLUD_API

Backend para la [SEMANA LINUX](http://semana.glud.org). Es una API REST para comunicar en datos JSON. Se complementa con el [frontend](https://github.com/GLUD/SLUD-frontend/)

Ej:

Petición:
```bash
$ curl -X GET http://sludapi.glud.org/api/speakers/
```
Respuesta:
```json
[{"nombre":"Tux","trabajo":"Mascota del Kernel Linux","foto":"https://upload.wikimedia.org/wikipedia/commons/a/af/Tux.png", "prioridad": "0"}]
```

**No olvidar el último '/' en la petición**

## Uso

### Local
Se ha configurado la API para que utilize variables de entorno para las contraseñas y el host público (ya que las contraseñas no deberían publicarse en Github).
Se recomienda usar un archivo *.env* (que es ignorado por git gracias a *.gitignore*) para guardar las variables de entorno así:

```bash
## ej. ./misconfiguraciones.env
export SECRET_KEY='contraseña super segura'
export PUBIC_HOST='localhost' # ej. sludapi.glud.org
export ADMIN_USER='admin'
export ADMIN_PASSWORD='secreto'
#...
```

y usarlo de esta manera:

```bash
$ source ./misconfiguraciones.env # archivo de variables de entorno
$ ./run.sh # Para hacer las migraciones, crear el usuario administrador y ejecutar el servidor.
```
Ó se puede manualmente:

```bash
$ source ./misconfiguraciones.env # archivo de variables de entorno
$ python manage.py createsuperusper #crea el usuario administrativo interactivamente
$ python manage.py migrate # aplica migraciones
$ python manage.py collectstatic # crea el directorio ./static para los archivos estáticos
$ python manage.py runserver 0.0.0.0:8000 # ejecuta el servidor en el puerto :8000
```
### Docker

Se puede usar docker para administrar el backend:

```bash
$ docker run -p "8000:8000" \ 
	-e SECRET_KEY="super secreto" \ 
	-e PUBLIC_HOST="sludapi.glud.org" \ 
	-e ADMIN_USER="admin" \ 
	-e ADMIN_PASSWORD="secreto" \ 
	-e ADMIN_EMAIL="miembro@glud.org" glud/slud-backend:latest
```

O Docker swarm con el archivo *docker-stack.yml* de ejemplo para ejecutar el [frontend](https://github.com/GLUD/SLUD-backend/) y el backend:
```bash
$ docker swarm init # si no se ha hecho antes
$ docker stack deploy -c docker-stack.yml slud
```

## Variables de entorno:

Las variables de entorno generales son:

- SECRET_KEY (obligatorio, Para la contraseña de la API).
- PUBLIC_HOST (obligatorio, para autorizar el host público en /admin)


Para docker/run.sh, las variables de entorno adicionales son:

- ADMIN_USER (usuario para la interfaz /admin, default:root)
- ADMIN_PASSWORD (contraseña del usuario administrador, obligatorio si no se está usando ADMIN_PASSWORD_FILE)
- ADMIN_PASSWORD_FILE (archivo que contiene la contraseña para el usuario administrador, obligatorio si no se está usando ADMIN_PASSWORD, tiene prioridad frente a ADMIN_PASSWORD).
- ADMIN_EMAIL (obligatorio, email del usuario administrador)


## TODO

- [x] hacer que Django sirva archivos estáticos en /admin/ (se logró con el plugin [whitenoise](https://devcenter.heroku.com/articles/django-assets))
- [ ] hacer equivalente /api/<test> a /api/<test>/
- [ ] responder en /api/speakers/ con el campo prioridad adicional

