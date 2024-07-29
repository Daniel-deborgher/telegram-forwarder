from telethon import TelegramClient, events

# Remplacez par votre API ID et API hash
api_id = '26210305'
api_hash = '34cbab68b08112262fa311a7affdd9d6'

# Identifiant du groupe et du canal
group_id = 'testreplysol'  # Remplacez par l'identifiant ou le nom d'utilisateur de votre groupe
channel_id = 'solana_trojanbot'  # Remplacez par le nom d'utilisateur de votre canal

# Créer une nouvelle session Telethon
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=group_id))
async def handler(event):
    print(f"New message in {group_id}: {event.message.message}")
    # Transférer le message au canal
    await client.forward_messages(channel_id, event.message)
    print(f"Message forwarded to {channel_id}")

async def main():
    await client.start()
    print("Client started. Listening for messages...")
    await client.run_until_disconnected()

# Démarrer le client
with client:
    client.loop.run_until_complete(main()
