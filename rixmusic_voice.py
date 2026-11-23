from pathlib import Path
from rixmusic_errors import ConfigurationError

class VoiceChatManager:
    """Group voice-chat helpers; does not fake call/stream success."""
    def __init__(self, adapter):
        self.adapter = adapter
        self.players = {}

    async def create(self, group_guid):
        return await self.adapter.create_group_voice_chat(group_guid)

    async def play(self, chat_guid, media_path):
        if not Path(media_path).is_file():
            raise FileNotFoundError(media_path)
        player = await self.adapter.voice_chat_player(chat_guid, media_path)
        self.players[str(chat_guid)] = player
        return player

    async def stop(self, chat_guid):
        player = self.players.pop(str(chat_guid), None)
        if player is None:
            return False
        stop = getattr(player, "stop", None)
        if callable(stop):
            result = stop()
            if hasattr(result, "__await__"):
                await result
        return True
