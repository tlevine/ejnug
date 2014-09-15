<html>
  <body>
    <h1>{{title}}</h1>
    <article>
      % if body != None:
      <div style="white-space: pre;">{{body}}</div>
      % end
      <ul>
        % for thread in threads:
          <li><ul>
          % for message in thread.get_toplevel_messages():
          % include('message.tpl', message = message)
          % end
          </ul></li>
        % end
      </ul>
    </article>
  </body>
</html>
