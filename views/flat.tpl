<html>
  <body>
    <h1>{{heading}}</h1>
    <article>
      <ul>
        % for href, description in list:
          <li><a href="{{href}}">{{description}}</a></li>
        % end
      </ul>
    </article>
  </body>
</html>
