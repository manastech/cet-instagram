# cet-instagram
Utilitario para contactar inscriptas en Comunidad CET vía Instagram

## Utilización del script

```
$ python script.py <username> <password> <recipients.csv> <mensaje>
```

`mensaje` debe estar entre comillas para que se entienda como un sólo parámtro y funcione correctamente

## Empaquetamiento a un único script con dependencias

1. Installar pyinstaller
```
pip install pyinstaller
```
1. Desde el root del proyecto:
```
$ pyinstaller --onefile --console --clean --strip script.py
```

## Funcionamiento del script empaquetado

```
$ dist/script <username> <password> <recipients.csv> <mensaje>
```
