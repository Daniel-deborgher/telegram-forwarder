from telethon import TelegramClient, events
from telethon.sessions import StringSession
import logging

# Configuration du logging
logging.basicConfig(level=logging.DEBUG)

# Remplacez par votre API ID et API hash
api_id = '26210305'
api_hash = '34cbab68b08112262fa311a7affdd9d6'

# Identifiant du groupe et du canal (utilisez les ID numériques si possible)
group_id = 'testreplysol'
channel_id = 'solana_trojanbot'

# Utiliser une session temporaire en mémoire
session = StringSession()

client = TelegramClient(session, api_id, api_hash, connection_retries=None, timeout=30)

print("Client created")

@client.on(events.NewMessage(chats=group_id))
async def handler(event):
    print(f"New message in {group_id}: {event.message.message}")
    # Transférer le message au canal
    try:
        await client.forward_messages(channel_id, event.message)
        print(f"Message forwarded to {channel_id}")
    except Exception as e:
        print(f"Failed to forward message: {e}")

async def main():
    print("Starting client...")
    await client.start()
    print("Client started. Listening for messages...")
    me = await client.get_me()
    print(f"Logged in as {me.username}")
    await client.run_until_disconnected()
    print("Client disconnected")

# Démarrer le client
with client:
    print("Running the client")
    client.loop.run_until_complete(main())
    print("Client has been run")
