#!/usr/bin/env python3
from notmuch import Database, Query
from bottle import Bottle, request, response, abort, redirect, view, TEMPLATE_PATH

TEMPLATE_PATH.append('views')
app = Bottle()
db = Database()

@app.route('/<identifier>/')
def slash(identifier):
    redirect('/' + identifier)

@app.route('/')
def home():
    pass

@app.get('/:querystr')
@view('thread')
def search(querystr):
    query = Query(db, querystr)
    if query.count_messages() == 1:
        message = next(iter(query.search_messages()))
        title = message.get_header('subject')
        try:
            body = message.get_part(1)
        except UnicodeDecodeError:
            body = 'There was an encoding problem with this message.'
    else:
        title = 'Results for "%s"' % querystr
        body = None

    return {
        'title': title,
        'body': body,
        'threads': query.search_threads(),
    }

@app.get('/:querystr/:num')
def attachment(querystr, num):
    query = Query(db, querystr)
    if query.count_messages() != 1:
        redirect('/' + querystr)
    else:
        message = next(iter(query.search_messages()))
        parts = message.get_message_parts()
        i = int(num) - 1
        if i >= len(parts):
            redirect('/' + querystr)
        else:
            part = parts[i]
            response.content_type = part.get_content_type()
         #  response.charset = part.get_content_charset()
            return part.get_payload()

if __name__ == '__main__':
    app.run()
