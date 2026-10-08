import os
import discord

CHANNEL_ID = 1555739448283627671

RA_EVENTS_ROLE_ID = 1556634761785638982
BLESSED_ROLE_ID = 1542203222536618085

ROLAS_WEBHOOK_ID = 1556625703896875079

TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f"✅ CONECTADO: {bot.user}")


@bot.event
async def on_message(message):

    # Solo nuestro canal de eventos
    if message.channel.id != CHANNEL_ID:
        return

    # Detectar exclusivamente mensajes del webhook de Rolas.es
    if message.webhook_id != ROLAS_WEBHOOK_ID:
        return

    print("🎉 ¡EVENTO DE ROLAS.ES DETECTADO!")
    print(f"Contenido: {message.content}")

    # Buscar los roles
    ra_events = message.guild.get_role(RA_EVENTS_ROLE_ID)
    blessed = message.guild.get_role(BLESSED_ROLE_ID)

    if ra_events is None:
        print("❌ No encuentro el rol RA Events")
        return

    if blessed is None:
        print("❌ No encuentro el rol Blessed")
        return

    # Mencionar ambos roles
    await message.channel.send(
        f"{ra_events.mention} {blessed.mention}",
        allowed_mentions=discord.AllowedMentions(
            roles=[ra_events, blessed]
        )
    )

    print("🔔 @RA Events + @Blessed mencionados")


bot.run(TOKEN)
