#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Sporocilo


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
        return self.render_template("hello.html")

class VnosHandler(BaseHandler):
    def get(self):
        return self.render_template("vnos-sporocila.html")
    def post(self):
        shranjeno_sporocilo=Sporocilo(vnos=self.request.get("sporocilo"))
        shranjeno_sporocilo.put()

        return self.render_template("vnos-sporocila.html")

class SeznamHandler(BaseHandler):
    def get(self):
        seznam = Sporocilo.query().fetch()
        params={"seznam": seznam}
        return self.render_template("seznam-sporocil.html",params=params)

class PosameznoHandler(BaseHandler):
    def get(self,shranjeno_sporocilo_id):
        shranjeno_sporocilo=Sporocilo.get_by_id(int(shranjeno_sporocilo_id))
        params={"shranjeno_sporocilo":shranjeno_sporocilo}
        return self.render_template("posamezno-sporocilo.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/vnos-sporocila', VnosHandler),
    webapp2.Route('/seznam-sporocil', SeznamHandler),
    webapp2.Route('/sporocilo/<shranjeno_sporocilo_id:\d+>', PosameznoHandler)
], debug=True)
