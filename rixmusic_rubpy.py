import inspect
from pathlib import Path
from rixmusic_errors import ConfigurationError, UnsupportedFeature

class RubpyAdapter:
    """Safe adapter for documented methods on an authenticated Rubpy Client."""
    def __init__(self, client):
        if client is None:
            raise ConfigurationError("An authenticated Rubpy Client is required.")
        self.client = client

    async def call(self, method_name, *args, **kwargs):
        method = getattr(self.client, method_name, None)
        if not callable(method):
            raise UnsupportedFeature(
                f"Rubpy client has no method {method_name!r} in this installation."
            )
        result = method(*args, **kwargs)
        return await result if inspect.isawaitable(result) else result

    async def send_message(self, chat_guid, text, **kwargs):
        return await self.call("send_message", chat_guid, text, **kwargs)

    async def send_music(self, chat_guid, path, caption=None, **kwargs):
        return await self.call("send_music", chat_guid, Path(path), caption, **kwargs)

    async def send_video(self, chat_guid, path, caption=None, **kwargs):
        return await self.call("send_video", chat_guid, Path(path), caption, **kwargs)

    async def send_voice(self, chat_guid, path, **kwargs):
        return await self.call("send_voice", chat_guid, Path(path), **kwargs)

    async def send_video_message(self, chat_guid, path, **kwargs):
        return await self.call("send_video_message", chat_guid, Path(path), **kwargs)

    async def get_me(self):
        return await self.call("get_me")

    async def create_group_voice_chat(self, group_guid):
        return await self.call("create_group_voice_chat", group_guid)

    async def voice_chat_player(self, chat_guid, media_path):
        method = getattr(self.client, "voice_chat_player", None)
        if not callable(method):
            raise UnsupportedFeature("voice_chat_player is unavailable in this Rubpy build.")
        result = method(chat_guid, Path(media_path))
        result = await result if inspect.isawaitable(result) else result
        if result is None:
            from rixmusic_errors import VoiceChatUnavailable
            raise VoiceChatUnavailable(
                "Rubpy did not create a voice player. RTC dependencies/platform support "
                "may be missing (for example aiortc/PyAV)."
            )
        return result

    async def account_voice_call(self, user_guid, *args, **kwargs):
        raise UnsupportedFeature(
            "Account-to-account voice calling is not exposed by the documented Rubpy API."
        )

    async def account_video_call(self, user_guid, *args, **kwargs):
        raise UnsupportedFeature(
            "Account-to-account video calling is not exposed by the documented Rubpy API."
        )
