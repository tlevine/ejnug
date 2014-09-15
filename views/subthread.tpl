<li>
  <a href="/id:{{message.get_message_id()}}">
    % if message.is_match():
    <strong>
    % end
      {{message.get_header('subject')}}
    % if message.is_match():
    </strong>
    % end
  </a>
</li>
<ul>
  % for reply in message.get_replies():
  % include('subthread.tpl', message = reply)
  % end
</ul>
