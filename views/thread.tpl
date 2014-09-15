<html>
  <head>
    <!-- <link rel="stylesheet" href="/.css" type="text/css" /> -->
    <style>
    .body { white-space: pre; }
    html, body, article, .threads { margin: 0; padding: 0; }
    .threads { margin-top: 0.5em; margin-bottom: 0.5em; }
    .threads ul { margin-left: 1em; padding-left: 0.5em; }
    </style>
  </head>
  <body>
    <article>
      <ul class="threads">
        % for thread in threads:
          <ul>
          % for message in thread.get_toplevel_messages():
          % include('subthread.tpl', message = message)
          % end
          </ul>
        % end
      </ul>
      <hr/>
      % if body != None:
      <div class="body">{{body}}</div>
      % end
    </article>
  </body>
</html>
