# pyFlora

PyFloraPosude
SEMINARSKI RAD


Finalni projekt

Upute za instalaciju

U željeni direktorij klonirati ovaj repozitorij
Nakon toga u terminalu izvršiti sljedeću liniju koda kako bi stvorili novu virtualnu okolinu:
  python -m venv venv

Odvesti terminal u folder aplikacije:
  cd pyflora_site
  
Zatim instalirati sve potrebne pip pakete za normalan rad web aplikacije linijom koda u terminalu:
  pip install -r requirements.txt

Pripremiti migracije za kreiranje baze podataka
   python manage.py makemigrations

Kreirati bazu podataka:
  python manage.py migrate
  
Kreirati inicijalnog superusera:
  python manage.py createsuperuser
  
Instancirati server
  python manage.py runserver
  
Za pregled i korištenje aplikacije posjetite http://algebra.pythonanywhere.com/
