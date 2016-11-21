#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
from google.appengine.ext.webapp import template
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates")
    )


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_vars = {
            'title': 'Login',
            'error': ''
        }
        template = JINJA_ENVIRONMENT.get_template('login.htm')
        self.response.out.write(template.render(template_vars))

    def post(self):
        u = self.request.get('username')
        p = self.request.get('password')
        t = self.request.get('phone')
        if u != 'Colleen' or p != 'pass':
            logging.info('Username: ' + u)
            logging.info('Password: ' + p)
            logging.info('Phone: ' + t)
            template_vars = {
                'title': 'Login',
                'error': 'BAD CREDENTIALS! Try again'
            }
            template = JINJA_ENVIRONMENT.get_template('login.htm')
            self.response.out.write(template.render(template_vars))
        else:
            template_vars = {
                'title': 'Back to login',
                'error': ''
            }
            template = JINJA_ENVIRONMENT.get_template('loggedin.htm')
            self.response.out.write(template.render(template_vars))

app = webapp2.WSGIApplication([
    ('/login', MainHandler)
], debug=True)
