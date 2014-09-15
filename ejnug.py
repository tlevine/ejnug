#!/usr/bin/env python3
from unidecode import unidecode
from lxml.html.clean import clean_html
from notmuch import Database, Query
from bottle import Bottle, request, response, abort, redirect, view, TEMPLATE_PATH

TEMPLATE_PATH.append('views')
app = Bottle()
db = Database()

@app.route('/<identifier>')
def slash(identifier):
    redirect('/' + identifier.rstrip('/') + '/')

@app.route('/')
def home():
    return 'Public messages'

@app.get('/!/:querystr/')
@view('thread')
def search(querystr):
    query = Query(db, querystr)
    if query.count_messages() == 1:
        message = next(iter(query.search_messages()))
        title = message.get_header('subject')
        try:
            parts = [(i + 1, part.get_filename('No description')) \
                     for i, part in enumerate(message.get_message_parts())]
            body = message.get_part(1)
        except UnicodeDecodeError:
            parts = []
            body = 'There was an encoding problem with this message.'
    else:
        title = 'Results for "%s"' % querystr
        parts = []
        body = None

    return {
        'title': title,
        'parts': parts,
        'body': body,
        'threads': list(hierarchy(query)),
    }

def hierarchy(query):
    for thread in query.search_threads():
        yield from (list(subhierarchy(message)) for message in thread.get_toplevel_messages())
           

def subhierarchy(message):
    for reply in message.get_replies():
        yield {
            'message_id': message.get_message_id(),
            'subject': message.get_header('subject'),
            'is_match': message.is_match(),
            'replies': list(subhierarchy(reply)),
        }

@app.get('/!/:querystr/:num')
def attachment(querystr, num):
    n = int(num)
    query = Query(db, querystr)
    if query.count_messages() != 1:
        redirect('/!/%s/' % querystr)
    else:
        message = next(iter(query.search_messages()))
        parts = message.get_message_parts()
        i = n - 1
        if i >= len(parts):
            redirect('/!/%s/' % querystr)
        else:
            part = parts[i]
            content_type = part.get_content_type()
            response.content_type = content_type
         #  response.charset = part.get_content_charset()

            fn = part.get_filename().replace('"', '')
            if fn != None:
                response.headers['content-disposition'] = 'filename="%s";' % unidecode(fn)

            payload = message.get_part(n)
            if 'html' in content_type.lower():
                return clean_html(payload)
            else:
                return payload

if __name__ == '__main__':
    app.run(server = 'cherrypy', reloader = True)
