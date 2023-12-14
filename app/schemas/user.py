from pydantic import BaseModel
from typing import Optional

"""

Seme (models) u Pydanticu su Python klase koje opisuju strukturu podataka, definisu tipove podataka i dodatna ogranicenja.
Seme u Pydanticu nude nekoliko kljucnih mogucnosti:
- Tipovi podataka: Sema omogucava definisanje tipova podataka za svaki atribut unutar klase. Na primer,
 mozete precizirati da li je odredjeni atribut string, broj, datum, itd.

- Validacija: Pydantic automatski vrsi validaciju podataka prema definisanim tipovima i pravilima.
 Ako se podaci ne podudaraju sa ocekivanim tipovima ili pravilima, Pydantic generise odgovarajuce grsške.

- Serializacija i Deserializacija: Pydantic obezbedjuje automatsku serijalizaciju (pretvaranje objekta u JSON) i deserijalizaciju
 (pretvaranje JSON-a u objekat) podataka prema definisanim semama.

"""
class UserToReturn(BaseModel):
    id: int
    # Opcioni tip (moze biti null)
    email: Optional[str] = None
    age: int
    name: str

    class Config:
        orm_mode = True
"""
Ako je orm_mode ukljucen:
Automatski konvertuje ORM objekat u Pydantic model:
Kada kreirate Pydantic model sa orm_mode=True i prosledite mu
ORM objekat (na primer, SQLAlchemy model), Pydantic ce automatski konvertovati ORM objekat u Pydantic model.

Izvrsiti ORM transformacije: 
Pydantic će izvršiti odredjene transformacije specificne za ORM.
Preskace atribute koji nisu definisani ovde - ako model ima 10 elemenata samo one navedene ovde vrati iz baze
"""
