# Instalação

 Dependencias:
- python
- virtualenv (https://virtualenv.pypa.io/en/stable/installation/)


```sh
# Crie uma virtualenv
$ virtualenv .vEnv

# Ative a virtualenv
$ source .vEnv/bin/activate

# Instale as dependencias
$ pip install -r requirements.txt

# Aplique as alterações no banco de dados
$ ./manage.py migrate

# Crie um superusuário
./manage.py createsuperuser


```

## Executando

```sh
$ ./manage.py runserver
```

## Adicionando dados de exemplo

```sh
$ ./manage.py loaddata initial_data
```# livemigration_modulo
# livemigration_modulo
