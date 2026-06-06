"""
Reddit Auto-Poster para Manhua Premium Pack
Usa PRAW (Python Reddit API Wrapper) para publicar automáticamente

Instalación:
pip install praw

Setup:
1. Ve a https://www.reddit.com/prefs/apps
2. Crea una app (script type)
3. Copia client_id, client_secret
4. Pega tus credenciales abajo
"""

import praw
import time
from datetime import datetime

# ============================================
# CONFIGURACIÓN (Emmanuel: llena esto)
# ============================================
REDDIT_CONFIG = {
    'client_id': 'TU_CLIENT_ID_AQUI',
    'client_secret': 'TU_CLIENT_SECRET_AQUI',
    'user_agent': 'ManhuaPremiumBot/1.0',
    'username': 'TU_USERNAME_AQUI',
    'password': 'TU_PASSWORD_AQUI'
}

GOOGLE_DRIVE_LINK = 'TU_GOOGLE_DRIVE_LINK_AQUI'  # 3 episodios gratis

# ============================================
# POSTS CONTENT
# ============================================
POSTS = {
    'r/manhwa': {
        'title': "I've been experimenting with AI voice narration for manhwa — here's what 100+ episodes sound like [Free Sample]",
        'body': f"""Hey r/manhwa! 👋

I've spent the last few months experimenting with AI voice narration for manhwa episodes in Spanish. Started as a personal project (I love manhwa but hate reading on my phone while commuting), and it evolved into something I think the community might find interesting.

**What I learned:**
- Voice pacing matters WAY more than I thought. Too fast = can't appreciate the art, too slow = boring
- Background music makes or breaks immersion
- Spanish narration has almost ZERO competition compared to English (huge gap in the market)

**Free sample pack** (3 episodes, 1080p HD):
👉 [{GOOGLE_DRIVE_LINK}]({GOOGLE_DRIVE_LINK})

If you're curious about the full collection (100+ episodes), I put together a landing page:
👉 https://corgipollo.github.io/manhua-premium-landing/

**Would love feedback** — especially on:
1. Voice tone (too robotic? too dramatic?)
2. Pacing (chapters/minute)
3. What titles would you want narrated next?

Not trying to sell anyone anything here — genuinely want to know if this format has legs. If it sucks, tell me. If it's cool, also tell me. 😅
""",
        'wait_days': 14  # Post on day 14 (después de participación)
    },

    'r/webtoons': {
        'title': "Creator Tool Experiment: I used AI voice narration on 100+ manhwa episodes — here's the workflow [Educational]",
        'body': f"""Hey r/webtoons creators! 🎨

I've been experimenting with an accessibility/distribution idea: **AI voice narration for webtoon/manhwa episodes**.

**The Problem I'm Solving:**
- Commuters can't read panels easily (I'm one of them)
- Visually impaired fans struggle with traditional formats
- Spanish-speaking market has almost zero narrated content

**My Workflow:**
1. Extract panels + dialogue from source
2. Script adaptation (conversational vs literal translation)
3. AI voice generation (tested 5+ models, settled on ElevenLabs + local alternatives)
4. Video assembly (1080p, chapter sync)
5. Background music layering (royalty-free)

**Results after 100+ episodes:**
- Average production time: 2-3 hours/episode (mostly manual editing)
- File size: ~70-100MB per episode (1080p MP4)
- Biggest challenge: Pacing. Too fast = art not appreciated, too slow = boring.

**Free sample** (3 episodes to test the format):
👉 [{GOOGLE_DRIVE_LINK}]({GOOGLE_DRIVE_LINK})

**For creators**: If you're interested in making your webtoon more accessible via narration, happy to share the tools/workflow I use. Not selling anything — just sharing what worked for me.

**Full collection** (if you want to see the finished product):
👉 https://corgipollo.github.io/manhua-premium-landing/

Would love to hear from other creators:
- Anyone tried similar accessibility formats?
- What's your take on AI narration vs human voice actors?
- Is this useful or just novelty?
""",
        'wait_days': 10  # Post on day 10
    }
}

# ============================================
# FUNCIONES
# ============================================
def check_karma(reddit):
    """Verifica que la cuenta tenga suficiente karma (regla 90/10)"""
    user = reddit.user.me()
    print(f"\n📊 Karma Check:")
    print(f"   Post Karma: {user.link_karma}")
    print(f"   Comment Karma: {user.comment_karma}")
    print(f"   Total Karma: {user.link_karma + user.comment_karma}")

    total_karma = user.link_karma + user.comment_karma
    if total_karma < 100:
        print(f"\n⚠️  WARNING: Karma bajo ({total_karma}). Recomendado: 100+")
        print("   Participa más en la comunidad antes de postear.")
        return False
    return True

def post_to_reddit(reddit, subreddit_name, title, body):
    """Publica un post en un subreddit"""
    try:
        subreddit = reddit.subreddit(subreddit_name)

        print(f"\n📝 Posting to {subreddit_name}...")
        print(f"   Title: {title[:50]}...")

        submission = subreddit.submit(title=title, selftext=body)

        print(f"✅ Posted successfully!")
        print(f"   URL: {submission.url}")
        print(f"   ID: {submission.id}")

        return submission

    except praw.exceptions.RedditAPIException as e:
        print(f"\n❌ Error posting to {subreddit_name}:")
        print(f"   {e}")
        return None
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return None

def main():
    """Main execution"""
    print("=" * 60)
    print("🚀 Reddit Auto-Poster - Manhua Premium Pack")
    print("=" * 60)

    # Verificar configuración
    if 'TU_CLIENT_ID' in REDDIT_CONFIG['client_id']:
        print("\n❌ ERROR: Debes configurar tus credenciales de Reddit primero.")
        print("   Edita REDDIT_CONFIG en este archivo.")
        return

    if 'TU_GOOGLE_DRIVE' in GOOGLE_DRIVE_LINK:
        print("\n❌ ERROR: Debes agregar el link de Google Drive.")
        print("   Edita GOOGLE_DRIVE_LINK en este archivo.")
        return

    # Conectar a Reddit
    try:
        print("\n🔐 Connecting to Reddit...")
        reddit = praw.Reddit(**REDDIT_CONFIG)
        print(f"✅ Connected as: {reddit.user.me().name}")
    except Exception as e:
        print(f"\n❌ Error connecting to Reddit: {e}")
        return

    # Verificar karma
    if not check_karma(reddit):
        response = input("\n⚠️  Continue anyway? (y/n): ")
        if response.lower() != 'y':
            print("Aborted.")
            return

    # Postear
    print("\n" + "=" * 60)
    print("📤 POSTING")
    print("=" * 60)

    for subreddit_name, post_data in POSTS.items():
        print(f"\n🎯 Target: {subreddit_name}")
        print(f"   Recommended wait: {post_data['wait_days']} days")

        response = input(f"   Post now? (y/n): ")
        if response.lower() != 'y':
            print("   Skipped.")
            continue

        submission = post_to_reddit(
            reddit,
            subreddit_name,
            post_data['title'],
            post_data['body']
        )

        if submission:
            print(f"\n✅ SUCCESS! Post live at: {submission.url}")

            # Guardar URL para tracking
            with open('reddit_posts_log.txt', 'a', encoding='utf-8') as f:
                f.write(f"{datetime.now()} | {subreddit_name} | {submission.url}\n")

        # Wait entre posts para evitar spam detection
        if len(POSTS) > 1:
            print("\n⏳ Waiting 60 seconds before next post...")
            time.sleep(60)

    print("\n" + "=" * 60)
    print("✅ DONE!")
    print("=" * 60)
    print("\n📝 Next steps:")
    print("   1. Check your posts for engagement")
    print("   2. RESPOND to every comment within 24h")
    print("   3. Track metrics in reddit_posts_log.txt")

if __name__ == "__main__":
    main()
