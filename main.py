import discord
from discord.ext import commands
from discord import app_commands
import asyncio
import traceback
from modals import CreateRole

# constants
token = 'token here'
command_prefix = '>'
creating_mode = [
    572841572438245377
]
positive_vote = '👍'
negative_vote = '👎'
admin_role_id = 918398920391004201

TEST_GUILD = discord.Object(572841572438245377)

async def summarizing():
    pass

async def check_reactions(reactions):
    """
    возвращает True или False В зависимости от того каких голосов было больше
    :param ctx:
    :param reaction:
    :return:
    """
    try:

        for reaction in reactions:
            async for user in reaction.users(): # перебираем юзеров на наличие админов
                for role in user.roles:
                    if role.id == admin_role_id:
                        pass

    except Exception as err:
        print(err)



        # await ctx.channel.send(f'{user} has reacted with {reaction.emoji}!')
    # Если их нет, то считаем голоса
    pass
class MyClient(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.content.startswith('`#Опрос`') and message.interaction:
            await asyncio.sleep(10.0)
            await check_reactions(message.reactions)
            # await message.edit(content='40')

    async def setup_hook(self) -> None:
        await self.tree.sync(guild=TEST_GUILD)

    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        pass

client = MyClient()


@client.tree.command(guild=TEST_GUILD, description="Submit feedback")
async def create_role(interaction: discord.Interaction):
    await interaction.response.send_modal(CreateRole())


async def main():
    await client.start(token)

asyncio.run(main())