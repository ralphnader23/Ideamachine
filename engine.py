"""  This bad boy will run the web server.

If we actually getsomewhere, we can can add some proper comments.

Author: Jessie Yeagle, Brett Scarborugh
Date: 7-1-2012


"""


import tornado.ioloop
import tornado.web
from mako.template import Template
import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()

class MainHandler (tornado.web.RequestHandler):
    def get(self):
        contacts = c.execute('''SELECT * from contacts''')

        rows = []

        for contact in contacts:
            ct = {
                    'name': contact[0],
                    'age': contact[1]
                    }
            rows.append(ct)

        self.write(Template(filename="templates/index.html").render(rows=rows))

application = tornado.web.Application([
    (r"/", MainHandler),
])



if __name__ == "__main__":
    # hit http://localhost:8888
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


