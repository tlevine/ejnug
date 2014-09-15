<html>
  <body>
    <h1>{{heading}}</h1>
    <article>
      <div style="white-space: pre;">{{body}}</div>
      <ul>
        % for message in thread.get_toplevel_messages():
        % include('message.tpl', message = message)
        % end
      </ul>
    </article>
  </body>
</html>
