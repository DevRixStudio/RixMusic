"""Minimal example. Replace session and identifiers with your own values."""
import asyncio
from rubpy import Client
from rixmusic import RixMusic, Track

async def main():
    async with Client(name="my_rubika_session") as client:
        music = RixMusic(client, owner_ids=["YOUR_USER_GUID"])
        await music.add(
            "YOUR_GROUP_GUID",
            Track("Example track", "https://example.com/audio.mp3")
        )
        print("Queued:", music.queue("YOUR_GROUP_GUID").items)

if __name__ == "__main__":
    asyncio.run(main())
