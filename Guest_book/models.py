from google.appengine.ext import ndb


class Oseba(ndb.Model):
    ime = ndb.StringProperty()
    priimek = ndb.StringProperty()
    email = ndb.StringProperty()
    sporocilo = ndb.StringProperty()
    nastanek = ndb.DateTimeProperty(auto_now_add=True)
