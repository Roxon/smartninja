#!/usr/bin/env python
import os
import jinja2
import webapp2


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
class OmeniHandler(BaseHandler):
    def get(self):
        return self.render_template("o_meni.html")
class KontaktHandler(BaseHandler):
    def get(self):
        return self.render_template("kontakt.html")
class BlogHandler(BaseHandler):
    def get(self):
        return self.render_template("blog.html")
class KalkulatorHandler(BaseHandler):
    def get(self):
      return self.render_template("kalkulator.html")
    def post(self):
        stevilo1=self.request.get("stevilo1")
        stevilo2=self.request.get("stevilo2")
        operacija=self.request.get("operacija")
        stevilo1=int(stevilo1)
        stevilo2=int(stevilo2)
        rezultat=0
        if operacija == "+":
            rezultat=stevilo1 + stevilo2
        elif operacija == "-":
            rezultat=stevilo1-stevilo2
        elif operacija == "*":
            rezultat=stevilo1*stevilo2
        elif operacija == "/":
            rezultat=stevilo1/stevilo2

        spremenljivka={
            "stevilo1":(stevilo1),
            "stevilo2":(stevilo2),
            "operacija":operacija,
            "rezultat":rezultat,
        }

        return self.render_template("kalkulator.html",params=spremenljivka)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/o_meni', OmeniHandler),
    webapp2.Route('/kontakt', KontaktHandler),
    webapp2.Route('/blog', BlogHandler),
    webapp2.Route('/kalkulator', KalkulatorHandler),
], debug=True)
