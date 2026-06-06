"""
Discord Auto-Poster para Manhua Premium Pack
Usa discord.py para publicar automáticamente en servers

Instalación:
pip install discord.py

Setup:
1. Únete manualmente a los servers (links en COMMUNITY-POSTS.md)
2. Espera 3-7 días (evitar new-account-spam flag)
3. Copia tu Discord token (Settings → Advanced → Developer Mode → Copy Token)
   NOTA: NO compartas tu token con nadie
4. Pega tu token abajo
"""

import discord
import asyncio
from datetime import datetime

# ============================================
# CONFIGURACIÓN (Emmanuel: llena esto)
# ============================================
DISCORD_TOKEN = 'TU_DISCORD_TOKEN_AQUI'
GOOGLE_DRIVE_LINK = 'TU_GOOGLE_DRIVE_LINK_AQUI'

# Servers y canales (ajusta según los IDs reales después de unirte)
SERVERS = {
    'Club de Anime y Manga en Español': {
        'server_id': 758717909521924107,  # ID público
        'channel_name': 'recomendaciones',  # o 'contenido-creadores'
        'message': f"""Hola comunidad! 👋

Les comparto un proyecto que vengo armando: **manhuas narrados en español con IA**.

**Por qué lo hice:**
Soy super fan de manhuas pero odio leerlos en el celular mientras voy en el transporte. Quería algo como audiolibros pero con los paneles visuales.

**Lo que incluye:**
- 100+ episodios narrados en español latino
- Calidad 1080p HD
- Audio limpio (no TTS genérico)
- Sin anuncios ni interrupciones

**Muestra GRATIS** (3 episodios completos):
👉 {GOOGLE_DRIVE_LINK}

**Pack completo** (si les gusta la muestra):
👉 https://corgipollo.github.io/manhua-premium-landing/

También armé una **lista VIP** para los que quieran acceso anticipado a nuevos episodios + descuentos exclusivos:
👉 https://corgipollo.github.io/manhua-premium-landing/#waitlist

**Me interesa mucho su feedback:**
- ¿La narración suena natural o muy robótica?
- ¿Qué títulos les gustaría ver narrados?
- ¿Alguien más consume manhuas de esta forma?

No es spam ni venta agresiva — genuinamente quiero saber si esto tiene sentido para la comunidad hispanohablante. Si es útil, sigo. Si es basura, me lo dicen sin filtro. 😅

¡Gracias por leer! 🙏""",
        'wait_days': 1  # Post on day 1 (most permissive)
    },

    'Webtoon Central': {
        'server_id': None,  # Emmanuel: obtén el ID después de unirte
        'channel_name': 'self-promotion',  # o 'general'
        'message': f"""Hey Webtoon Central! 🎬

I've been working on something niche: **AI-narrated manhwa episodes in Spanish** (think audiobooks but with visuals).

**What it is:**
- 100+ episodes narrated with AI voices
- 1080p HD video + clean audio
- No ads, no interruptions, just the story

**Why Spanish?**
The English market has tons of narrated content, but Spanish-speaking fans have almost nothing. Figured I'd fill that gap.

**Free sample** (3 full episodes to test the vibe):
👉 {GOOGLE_DRIVE_LINK}

**Full collection** (if you dig the sample):
👉 https://corgipollo.github.io/manhua-premium-landing/

Also just launched a **VIP waitlist** for early access to new episodes + exclusive discounts:
👉 https://corgipollo.github.io/manhua-premium-landing/#waitlist

**I'd love your honest take:**
1. Does the narration sound natural or too robotic?
2. Pacing good or too fast/slow?
3. What titles would you want next?

Not trying to spam — just sharing a passion project and looking for feedback from people who actually care about webtoons. If it's trash, roast me. If it's cool, let me know. 😄

Thanks for checking it out! 🙏""",
        'wait_days': 3  # Post on day 3
    }
}

# ============================================
# BOT CLIENT
# ============================================
class ManhuaPosterBot(discord.Client):
    async def on_ready(self):
        print(f'\n✅ Logged in as {self.user} (ID: {self.user.id})')
        print('=' * 60)

        # Listar servers disponibles
        print("\n📋 Servers you're in:")
        for guild in self.guilds:
            print(f"   - {guild.name} (ID: {guild.id})")

        print("\n" + "=" * 60)
        print("🎯 POSTING")
        print("=" * 60)

        # Postear en cada server
        for server_name, config in SERVERS.items():
            if config['server_id'] is None:
                print(f"\n⚠️  {server_name}: No server_id configured. Skipping.")
                continue

            print(f"\n🎯 Target: {server_name}")
            print(f"   Server ID: {config['server_id']}")
            print(f"   Channel: #{config['channel_name']}")

            try:
                # Encontrar server
                guild = self.get_guild(config['server_id'])
                if not guild:
                    print(f"   ❌ Server not found. Make sure you've joined it.")
                    continue

                # Encontrar canal
                channel = discord.utils.get(guild.text_channels, name=config['channel_name'])
                if not channel:
                    print(f"   ❌ Channel #{config['channel_name']} not found.")
                    print(f"   Available channels:")
                    for ch in guild.text_channels:
                        print(f"      - #{ch.name}")
                    continue

                # Verificar permisos
                if not channel.permissions_for(guild.me).send_messages:
                    print(f"   ❌ No permission to send messages in #{channel.name}")
                    continue

                # Enviar mensaje
                print(f"   📤 Sending message...")
                message = await channel.send(config['message'])

                print(f"   ✅ Posted successfully!")
                print(f"   Message URL: {message.jump_url}")

                # Guardar log
                with open('discord_posts_log.txt', 'a', encoding='utf-8') as f:
                    f.write(f"{datetime.now()} | {server_name} | {message.jump_url}\n")

                # Wait entre posts
                await asyncio.sleep(10)

            except discord.Forbidden:
                print(f"   ❌ Forbidden: No permission to post in this channel")
            except discord.HTTPException as e:
                print(f"   ❌ HTTP Error: {e}")
            except Exception as e:
                print(f"   ❌ Unexpected error: {e}")

        print("\n" + "=" * 60)
        print("✅ DONE!")
        print("=" * 60)
        print("\n📝 Next steps:")
        print("   1. Check your posts for reactions/replies")
        print("   2. RESPOND to every reply")
        print("   3. Track metrics in discord_posts_log.txt")

        # Cerrar bot
        await self.close()

# ============================================
# MAIN
# ============================================
def main():
    print("=" * 60)
    print("🚀 Discord Auto-Poster - Manhua Premium Pack")
    print("=" * 60)

    # Verificar configuración
    if 'TU_DISCORD_TOKEN' in DISCORD_TOKEN:
        print("\n❌ ERROR: Debes configurar tu Discord token primero.")
        print("   Edita DISCORD_TOKEN en este archivo.")
        print("\n   Cómo obtener tu token:")
        print("   1. Abre Discord → Settings → Advanced")
        print("   2. Enable Developer Mode")
        print("   3. Right-click tu avatar → Copy Token")
        print("   ⚠️  NO compartas tu token con nadie")
        return

    if 'TU_GOOGLE_DRIVE' in GOOGLE_DRIVE_LINK:
        print("\n❌ ERROR: Debes agregar el link de Google Drive.")
        print("   Edita GOOGLE_DRIVE_LINK en este archivo.")
        return

    # Iniciar bot
    print("\n🔐 Connecting to Discord...")
    intents = discord.Intents.default()
    intents.message_content = True

    client = ManhuaPosterBot(intents=intents)

    try:
        client.run(DISCORD_TOKEN)
    except discord.LoginFailure:
        print("\n❌ ERROR: Invalid Discord token")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
