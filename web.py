from notmuch import Database, Query
from bottle import Bottle, request, response, abort, redirect, view, TEMPLATE_PATH

TEMPLATE_PATH.append('views')
app = Bottle()
db = Database()

@app.route('/<identifier>/')
def slash(identifier):
    redirect('/' + identifier)

@app.get('/searches/:querystr')
@view('flat')
def search(querystr):
    query = Query(db, querystr).search_threads()
    threads = [('/threads/' + t.get_thread_id(), t.get_subject()) \
               for t in query]
    return {
        'heading': 'Results for "%s"' % querystr,
        'list': threads
    }

def _get_thread(thread_id):
    querystr = 'thread:' + thread_id
    thread = next(iter(Query(db, querystr).search_threads()))
    return thread.get_subject()

@app.get('/threads/:thread_id')
@view('flat')
def thread(thread_id):
    query = Query(db, 'thread:%s' % thread_id)
    if not query.count_threads() == 1:
        return 'Thread not found', 404
    messages = [('/messages/' + m.get_message_id(), m.get_header('subject')) \
                for m in query.search_messages()]
    return {
        'heading': _get_thread(thread_id).get_subject(),
        'list': messages
    }

@app.get('/messages/:message_id')
@view('message')
def message(message_id):
    query = Query(db, 'id:%s' % message_id)
    if not query.count_messages() == 1:
        return 'Message not found', 404
    m = next(query.search_messages())
    return {
        'heading': m.get_header('subject'),
        'body': m.get_part(1),
    }

@app.get('/')
@view('flat')
def recent():
    query = Query(db, '')
    messages = []
    for i, m in enumerate(query.search_messages()):
        if i >= 30:
            break
        messages.append(('/messages/' + m.get_message_id(), m.get_header('subject')))
    return {
        'heading': 'Recent messages',
        'list': messages,
    }

app.run()
