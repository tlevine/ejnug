<html>
  <head>
    <!-- <link rel="stylesheet" href="/.css" type="text/css" /> -->
    <style>
    .body { white-space: pre; }

    html { background-color: black; color: white; }

    html, body, article, nav, nav ul, nav li,
    .threads, .threads > ul,
    .heading p, h1, h2, h3, h4, h5
      { margin: 0; padding: 0; }

    nav > ul > li {
      float: left; list-style-type: none;
      margin-right: 1em;
    }
    nav { height: 2em; }

    .threads > ul ul { margin-left: 1em; padding-left: 0.5em; }
    h1, h2, h3, h4, h5 { font-size: inherit; }
    .attachments, .threads { color: grey; }
    .body, .heading { color: white; }
    .heading {
      border-top: solid 1px grey;
      margin-top: 0.5em;
      padding-top: 0.5em;
      border-bottom: solid 1px grey;
      margin-bottom: 0.5em;
      padding-bottom: 0.5em;
    }
    a, a:visited, a:hover { color: #fe57a1; }
    a:hover { text-decoration: underline; }
    </style>
  </head>
  <body>
    <article>
      <nav>
        <ul>
          <li><a href="/">Home</a></li>
          <li><a href="/!/date:3D../">Recent</a></li>
          <!-- <li><a href="/!/from:message['/"> -->
        </ul>
      </nav>

      <div class="threads">
        <ul>
          % for thread in threads:
            <ul>
            % for message in thread:
            % include('subthread.tpl', message = message)
            % end
            </ul>
          % end
        </ul>
      </div>

      % if body != None:
      <div class="heading">
        <h3>{{message['subject']}}</h3>
        <p><emph>{{message['date']}})</emph></p>
        <p><a href="{{message['mailto']}}" target="_blank">Reply to this message</a></p>
      </div>
      <div class="body">{{body}}</div>
      <div class="attachments">
        <h3>Attachments</h3>
        <ol>
        % for n, description in parts:
          <li><a href="{{n}}">{{description}}</a></li>
        % end
        </ol>
      </div>
      % end
    </article>
  </body>
</html>
