# tg-new-pairs-listener-repo

## Start Project

```bash
cp example.telegram.env telegram.env
```
Enter the values of your variables in telegram.env:

```
API_ID=
API_HASH=
PHONE_NUMBER=
```

---

---

Start docker-compose:

```bash
docker-composwe up -d
```

```bash
docker exec -it tg-new-pairs-listener-repo-tg_listener bash
```

```bash
python connect_to_tg.py
# Enter code from TG...
exit
```


```bash
docker-compose restart
```


MAKE better input TG code!
