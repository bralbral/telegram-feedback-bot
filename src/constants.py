import os

ROOT_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

START_MESSAGE: str = """
<h1>
👋 Hello!
</h1>
<p>
    I can redirect to recipient <b>text, audios, voice messages, images, files</b> to recipient.
</p>

<p>
 Just send your message and wait for a response! 
</p>

"""

__all__ = ["ROOT_DIR", "START_MESSAGE"]
