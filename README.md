# cet-instagram
Utilitario para contactar inscriptas en Comunidad CET vía Instagram

## Utilización del script

```
$ python script.py <username> <password> <recipients.csv> <mensaje.txt>
```


## Empaquetamiento a un único script con dependencias

1. Installar pyinstaller
```
pip install pyinstaller
```
1. Desde el root del proyecto:
```
$ pyinstaller --console --clean --strip script.py
```

## Funcionamiento del script empaquetado

```
$ dist/script <username> <password> <recipients.csv> <mensaje.txt>
```
