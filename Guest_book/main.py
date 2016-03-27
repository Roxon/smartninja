#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Oseba


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))

class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("guest_book.html")
    def post(self):
        gost=Oseba(ime=self.request.get("ime",),priimek=self.request.get("priimek",),email=self.request.get("email",),sporocilo=self.request.get("sporocilo",))
        if gost.ime=="":
            gost.ime="neznano ime"
        if gost.priimek=="":
            gost.priimek="neznan priimek"
        gost.put()
        return self.render_template("guest_book.html")

class SeznamHandler(BaseHandler):
    def get(self):
        seznam = Oseba.query().fetch()
        params={"seznam": seznam}
        return self.render_template("seznam-oseb.html",params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/seznam', SeznamHandler)
], debug=True)
