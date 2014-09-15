#!/usr/bin/env python3
from notmuch import Database, Query
from bottle import Bottle, request, response, abort, redirect, view, TEMPLATE_PATH

TEMPLATE_PATH.append('views')
app = Bottle()
db = Database()

@app.route('/<identifier>')
def slash(identifier):
    redirect('/' + identifier.rstrip('/'))

@app.route('/')
def home():
    pass

@app.get('/:querystr/')
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
        'threads': query.search_threads(),
    }

@app.get('/:querystr/:num')
def attachment(querystr, num):
    query = Query(db, querystr)
    if query.count_messages() != 1:
        redirect('/%s/' % querystr)
    else:
        message = next(iter(query.search_messages()))
        parts = message.get_message_parts()
        i = int(num) - 1
        if i >= len(parts):
            redirect('/%s/' % querystr)
        else:
            part = parts[i]
            response.content_type = part.get_content_type()
         #  response.charset = part.get_content_charset()
            return part.get_payload()

if __name__ == '__main__':
    app.run(server = 'cherrypy', reloader = True)
