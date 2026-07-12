from html import escape

from aiogram.types import Message


def extract_userinfo_from_message(message: Message) -> str:
    """
    Extract information from message.from_user
    :param message:
    :return:
    """
    user = message.from_user
    if user is None:
        return "unknown"

    username = escape(user.username or "")
    first_name = escape(user.first_name or "")
    last_name = escape(user.last_name or "")
    language = escape(user.language_code or "")
    return f"""
           #id{user.id}
           <br/>
           #msgid{message.message_id}
           <br/>
           <kbd>
           username: {username}
           <br/>
           first_name: {first_name}
           <br/>
           last_name: {last_name}
           <br/>
           language_code: {language}
           <br/>
           </kbd>
           <br/>
            """


__all__ = ["extract_userinfo_from_message"]
