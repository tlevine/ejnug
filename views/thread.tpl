<html>
  <head>
    <!-- <link rel="stylesheet" href="/.css" type="text/css" /> -->
    <style>
    .body { white-space: pre; }
    html, body, article, .threads { margin: 0; padding: 0; }
    .threads { margin-top: 0.5em; margin-bottom: 0.5em; }
    .threads ul { margin-left: 1em; padding-left: 0.5em; }
    h1, h2, h3, h4, h5 { font-size: inherit; }
    </style>
  </head>
  <body>
    <article>
      <h1>Thread</h1>
      <ul class="threads">
        % for thread in threads:
          <ul>
          % for message in thread:
          % include('subthread.tpl', message = message)
          % end
          </ul>
        % end
      </ul>

      % if body != None:
      <hr/>
      <div class="body">{{body}}</div>
      <hr/>
      <h1>Attachments</h1>
      <ol>
      % for n, description in parts:
        <li><a href="{{n}}">{{description}}</a></li>
      % end
      </ol>
      % end

    </article>
  </body>
</html>
