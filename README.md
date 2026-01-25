# blogi

## Ominaisuudet

- [x] käyttäjä voi luoda tilin
- [x] käyttäjä voi kirjautua tilille
- [ ] käyttäjä voi julkaista artikkelin omalla tilillä
- [ ] kayttäjä voi suodattaa artikkelit aiheella
- [ ] käyttäjä voi suodattaa artikkelit kirjoittajalla
- [ ] etusivulla listataan uusimmat artikkelit

## Asennus
Asenna flask-kirjasto:
```bash
$ pip install flask
```
Luo sqlite tietokanta:
```bash
$ sqlite3 database.db < schema.sql
```

Luo salausavain istuntoevästeille:
```bash
$ python -c 'import secrets; print(f"secret_key = \"{secrets.token_hex(16)}\"")' > blogi/config.py
```

## Käynnistys
```bash
$ flask --app blogi run
```
