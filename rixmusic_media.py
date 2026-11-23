from pathlib import Path
from rixmusic_errors import ConfigurationError

class MediaManager:
    """Send already-created media to Rubika chats. It does not generate video."""
    def __init__(self, adapter):
        self.adapter = adapter

    async def music(self, chat_guid, file_path, caption=None):
        return await self.adapter.send_music(chat_guid, file_path, caption)

    async def video(self, chat_guid, file_path, caption=None):
        return await self.adapter.send_video(chat_guid, file_path, caption)

    async def voice(self, chat_guid, file_path):
        return await self.adapter.send_voice(chat_guid, file_path)

    async def round_video(self, chat_guid, file_path):
        return await self.adapter.send_video_message(chat_guid, file_path)
