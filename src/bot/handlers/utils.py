from aiogram.types import Message


def extract_userinfo_from_message(message: Message) -> str:
    """
    Extract information from message.from_user
    :param message:
    :return:
    """
    return f"""
           #id{message.from_user.id}
           <br/>
           #msgid{message.message_id}
           <br/>
           <kbd>
           username: {message.from_user.username}
           <br/>
           first_name: {message.from_user.first_name}
           <br/>
           last_name: {message.from_user.last_name}
           <br/>
           language_code: {message.from_user.language_code}
           <br/>
           </kbd>
           <br/>
            """


__all__ = ["extract_userinfo_from_message"]
