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
        title = message.get_header('subject')
        body = next(iter(query.search_messages())).get_part(1)
    else:
        title = 'Results for "%s"' % querystr
        body = None

    return {
        'title': title,
        'body': body,
        'threads': query.search_threads(),
    }

@app.get('/:querystr/:part')
@view('message')
def attachment(querystr, part):
    query = Query(db, querystr)
    if query.count_messages() != 1:
        redirect('/' + querystr)
    else:
        message = next(iter(query.search_messages()))
        parts = message.get_message_parts()
        i = part - 1
        if i >= len(parts):
            redirect('/' + querystr)
      # else:
      #     content type
      #     message.get_part(part)

if __name__ == '__main__':
    app.run()
