# infrastructure/platforms/discord_adapter.py
import asyncio
import discord
from discord.ext import commands

from application.ports.platform_adapter import IMessageSender, IMessageReceiver

class DiscordAdapter(IMessageSender, IMessageReceiver):
    def __init__(self, bot: commands.Bot):
        self._bot = bot

    async def send_message(self, channel_id: int, text: str) -> None:
        channel = self._bot.get_channel(channel_id) # It gets it firstly from cache
        if channel is None:                         # but it may not be there!
            try:
                channel = await self._bot.fetch_channel(channel_id) # If it's so, it gets it directly
            except (discord.NotFound, discord.Forbidden) as e:
                # logger.warning(f"Couldn't fetch channel {action.channel_id}: {e}")
                return
        await channel.send(text)
    
    """Self care stuff"""
    async def start(self, token) -> None:
        # logger.info("Starting the bot...")
        await self._bot.start(token)
    
    async def stop(self) -> None:
        # logger.info("Closing the bot.")
        await self._bot.close()
    