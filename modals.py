import discord
import traceback
import asyncio

class CreateRole(discord.ui.Modal, title='Create role'):
    name = discord.ui.TextInput(
        label='Название',
        placeholder='Введи название роли',
    )
    description = discord.ui.TextInput(
        label='Описание роли',
        style=discord.TextStyle.long,
        placeholder='Описание роли',
        required=False,
        max_length=300,
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f'`#Опрос` Пользователь {interaction.user.nick} предложил создать роль "{self.name.value}" с описанием: \n {self.description.value}'
            f'\n'
            f'Голосование за создание проходит реакциями :+1: и :-1: под этим сообщением')

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)

        # Make sure we know what the error actually is
        traceback.print_exception(type(error), error, error.__traceback__)