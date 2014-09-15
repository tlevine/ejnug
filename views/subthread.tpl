<li><a href="/id:{{message.get_message_id()}}">{{message.get_header('subject')}}</a></li>
<ul>
  % for reply in message.get_replies():
  % include('subthread.tpl', message = reply)
  % end
</ul>
