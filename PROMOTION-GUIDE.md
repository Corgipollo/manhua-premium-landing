# Guía de Promoción — Manhua Premium Pack

**Fecha**: 2026-06-05  
**Objetivo**: Publicar en 5 comunidades seleccionadas con posts genuinos que ofrezcan valor  
**Estrategia**: NO spam — engagement primero, promoción segundo  

---

## 🎯 CHECKLIST RÁPIDO

### Pre-requisitos (ANTES de postear)
- [ ] **Muestras gratis subidas**: Sube los 3 episodios demo a Google Drive (público, sin email)
- [ ] **Link de Drive obtenido**: Copia el link público
- [ ] **Waitlist configurado**: Elige una opción (Formspree/Google Forms/Apps Script)
- [ ] **Landing testeada**: Verifica que https://corgipollo.github.io/manhua-premium-landing/ carga bien
- [ ] **Cuentas preparadas**:
  - Reddit: 100+ karma + participación previa en r/manhwa o r/webtoons
  - Discord: Únete a servers 3-7 días ANTES de postear

### Configurar Scripts
- [ ] **reddit_poster.py**: Edita credenciales de Reddit
- [ ] **discord_poster.py**: Edita Discord token

### Ejecución
- [ ] **Día 1**: Postear en Discord (Club Español)
- [ ] **Día 3**: Postear en Discord (Webtoon Central)
- [ ] **Día 7**: Postear en Novel Updates Forum
- [ ] **Día 10**: Postear en Reddit (r/webtoons)
- [ ] **Día 14**: Postear en Reddit (r/manhwa)

### Post-Posting
- [ ] **Engagement**: Responder TODOS los comentarios en 24h
- [ ] **Tracking**: Monitorear upvotes, comments, waitlist signups
- [ ] **Ajustes**: Si algo falla, analizar por qué + iterar

---

## 📦 PASO 1: PREPARAR MUESTRAS GRATIS

### Opción A: Google Drive (Recomendado)
1. Crea una carpeta en Google Drive: "Manhua Narrado - Muestra Gratis"
2. Sube los 3 primeros episodios (Capitulo_1_Video.mp4, Capitulo_2_Video.mp4, Capitulo_3_Video.mp4)
3. Right-click carpeta → Share → "Anyone with the link"
4. Copia el link público
5. Pega el link en:
   - `reddit_poster.py` → `GOOGLE_DRIVE_LINK`
   - `discord_poster.py` → `GOOGLE_DRIVE_LINK`
   - `COMMUNITY-POSTS.md` → Reemplazar `GOOGLE_DRIVE_LINK`

### Opción B: Mega.nz
1. Sube los 3 episodios a Mega
2. Crea link público
3. Pega el link igual que arriba

### Verificar
```bash
# Testea que el link funcione en navegador incognito
# Debe descargar SIN pedir login
```

---

## ⚙️ PASO 2: CONFIGURAR WAITLIST

### Opción 1: Formspree (Más fácil)
1. Ve a https://formspree.io
2. Crea cuenta gratis
3. Crea un nuevo form
4. Copia tu Form ID (ej: `xyzabc123`)
5. Edita `index.html`:
   ```html
   <!-- Busca esta línea (línea ~362) -->
   <form id="waitlist-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   
   <!-- Reemplaza YOUR_FORM_ID con tu ID real -->
   <form id="waitlist-form" action="https://formspree.io/f/xyzabc123" method="POST">
   ```
6. Commit y push:
   ```bash
   cd C:/Users/Emmanuel/Documents/manhua-premium-landing
   git add index.html
   git commit -m "Configure Formspree waitlist form"
   git push origin main
   ```
7. Testea: Ve a tu landing y envía un email de prueba
8. Verifica en Formspree dashboard que llegó

### Opción 2: Google Forms (Mejor para análisis)
1. Ve a https://forms.google.com
2. Crea nuevo formulario
3. Agrega campos:
   - Email (requerido)
   - Nombre (opcional)
4. Click "Send" → Pestaña `< >` (Embed)
5. Copia el iframe code
6. Edita `index.html`:
   ```html
   <!-- Busca el comentario "Opción 2: Google Form embed" (línea ~387) -->
   <!-- Descomenta esta sección y pega tu iframe -->
   <iframe
       src="https://docs.google.com/forms/d/e/TU_FORM_ID/viewform?embedded=true"
       width="100%"
       height="400"
       frameborder="0"
       class="rounded-xl"
   >Cargando…</iframe>
   ```
7. Comenta la sección de Formspree (Opción 1)
8. Commit y push

### Opción 3: Google Apps Script (Avanzado)
Ver `README.md` para instrucciones completas.

---

## 🔑 PASO 3: CONFIGURAR CUENTAS REDDIT

### Crear Reddit App
1. Ve a https://www.reddit.com/prefs/apps
2. Click "create app" o "create another app"
3. Llena:
   - **name**: ManhuaPremiumBot
   - **App type**: script
   - **description**: Bot para promoción de manhuas narrados
   - **about url**: https://corgipollo.github.io/manhua-premium-landing/
   - **redirect uri**: http://localhost:8080
4. Click "create app"
5. Guarda:
   - **client_id**: debajo de "personal use script"
   - **client_secret**: el que aparece

### Configurar reddit_poster.py
```python
# Edita estas líneas:
REDDIT_CONFIG = {
    'client_id': 'abcd1234xyz',  # Tu client_id
    'client_secret': 'xyz9876abcd',  # Tu client_secret
    'user_agent': 'ManhuaPremiumBot/1.0',
    'username': 'tu_username',  # Tu usuario de Reddit
    'password': 'tu_password'  # Tu contraseña
}

GOOGLE_DRIVE_LINK = 'https://drive.google.com/...'  # Link de paso 1
```

### Instalar dependencias
```bash
pip install praw
```

### Testear conexión
```bash
python reddit_poster.py
# Debe decir "Connected as: tu_username"
# Debe mostrar tu karma
```

---

## 💬 PASO 4: CONFIGURAR DISCORD

### Obtener Discord Token
⚠️ **IMPORTANTE**: Tu token es como tu contraseña. NO lo compartas.

1. Abre Discord (app desktop o web)
2. Settings (⚙️) → Advanced → Enable "Developer Mode"
3. Presiona `Ctrl+Shift+I` (abre DevTools)
4. Ve a la pestaña "Network"
5. Filtra por "api"
6. Refresca la página (F5)
7. Click en cualquier request
8. Headers → Request Headers → Busca "authorization"
9. Copia el valor (es tu token)

**Alternativa más fácil** (usar bot token en vez de user token):
1. Ve a https://discord.com/developers/applications
2. Click "New Application"
3. Nombra: "Manhua Premium Bot"
4. Ve a "Bot" → "Add Bot"
5. Click "Reset Token" → "Copy"
6. Ese es tu bot token

### Configurar discord_poster.py
```python
# Edita estas líneas:
DISCORD_TOKEN = 'YOUR_DISCORD_TOKEN_HERE'  # Pega tu token aquí

GOOGLE_DRIVE_LINK = 'https://drive.google.com/...'  # Link de paso 1
```

### Unirse a servers
1. **Club de Anime y Manga en Español**:
   - https://discord.com/invite/club-de-anime-y-manga-en-espanol-758717909521924107
   - Espera 3-7 días antes de postear

2. **Webtoon Central**:
   - https://discord.com/invite/FwxGPZr
   - Espera 3-7 días antes de postear

### Obtener IDs de servers
```python
# Ejecuta discord_poster.py
# Te mostrará lista de servers con sus IDs
# Copia el ID de "Webtoon Central" y pégalo en SERVERS['Webtoon Central']['server_id']
```

### Instalar dependencias
```bash
pip install discord.py
```

---

## 🚀 PASO 5: PUBLICAR

### Calendario Recomendado

#### Día 0 (HOY)
- [ ] Subir muestras a Google Drive
- [ ] Configurar waitlist
- [ ] Instalar dependencias (`pip install praw discord.py`)
- [ ] Configurar credenciales en scripts

#### Día 1
- [ ] **Postear en Discord: Club Español**
  ```bash
  python discord_poster.py
  # Cuando pregunte, selecciona solo "Club de Anime y Manga en Español"
  ```
- [ ] Responder comentarios/replies

#### Día 3
- [ ] **Postear en Discord: Webtoon Central**
  ```bash
  python discord_poster.py
  # Selecciona solo "Webtoon Central"
  ```
- [ ] Responder replies

#### Día 7
- [ ] **Postear en Novel Updates Forum** (manual)
  - URL: https://novelupdatesforum.com/forums/manhwa.35/
  - Click "Post New Thread"
  - Título: `[Discussion] Audio adaptations of manhwa — like audiobooks but with visuals?`
  - Cuerpo: Ver `COMMUNITY-POSTS.md` → POST #5
  - Postear

#### Día 10
- [ ] **Postear en Reddit: r/webtoons**
  ```bash
  python reddit_poster.py
  # Cuando pregunte, selecciona solo "r/webtoons"
  ```
- [ ] Responder TODOS los comentarios en 24h

#### Día 14
- [ ] **Postear en Reddit: r/manhwa**
  ```bash
  python reddit_poster.py
  # Selecciona solo "r/manhwa"
  ```
- [ ] Responder TODOS los comentarios en 24h

### Qué hacer DESPUÉS de cada post

#### Engagement (CRÍTICO)
- [ ] Revisar post cada 2-4 horas el primer día
- [ ] Responder CADA comentario (personalizados, no copy-paste)
- [ ] Agradecer feedback positivo
- [ ] Admitir críticas válidas ("Good point, I'll work on that")
- [ ] NO defenderse agresivamente
- [ ] NO pedir likes/subscribes en replies

#### Tracking
- [ ] Anotar en spreadsheet:
  - Upvotes/reactions
  - Número de comentarios/replies
  - Sentiment (positivo/neutral/negativo)
  - Waitlist signups ese día
  - Ventas ese día

#### Red Flags (STOP si ves esto)
- ❌ Post removido por moderadores → NO repostear, contacta mods
- ❌ Shadowban en Reddit → Chequea en r/ShadowBan
- ❌ Zero engagement después de 48h → Analiza por qué
- ❌ Comments negativos >70% → Detén promoción, analiza feedback

---

## 📊 METRICAS DE EXITO

### Mínimo Viable
- 50+ engagements combinados (upvotes + comments + replies)
- 5+ waitlist signups
- 0 posts removidos

### Objetivo Bueno
- 100+ engagements
- 15+ waitlist signups
- 1+ sale

### Objetivo Excelente
- 200+ engagements
- 30+ waitlist signups
- 5+ sales
- 1+ post con >500 upvotes o viral

---

## ⚠️ REGLAS ANTI-SPAM (NO ROMPER)

### Reddit
- ✅ Regla 90/10: 90% participación, 10% promoción
- ✅ Espaciar posts 7+ días entre subreddits
- ✅ Responder comentarios en tus posts
- ❌ NO postear mismo contenido en múltiples subs el mismo día
- ❌ NO usar cuentas nuevas (<30 días) o con karma bajo (<100)
- ❌ NO ignorar comentarios (marca como spam)

### Discord
- ✅ Leer reglas del server ANTES de postear
- ✅ Usar canales apropiados (self-promo si existe)
- ✅ Esperar 3-7 días después de unirte
- ❌ NO postear en múltiples canales del mismo server
- ❌ NO DM a miembros con promoción
- ❌ NO spam repetitivo

### General
- ✅ Ofrecer valor (samples gratis, feedback, educación)
- ✅ Ser genuino ("si es basura, díganmelo")
- ✅ Responder críticas constructivamente
- ❌ NO "like and subscribe" language
- ❌ NO overselling ("best ever", "you NEED this")
- ❌ NO mentir sobre el producto

---

## 🆘 TROUBLESHOOTING

### "Post removido por moderadores"
1. NO repostear inmediatamente
2. Lee mensaje de remoción (si hay)
3. Revisa reglas del subreddit/server
4. Contacta moderadores educadamente:
   ```
   Hi mods, my post about [topic] was removed. I read the rules and thought it followed [rule X]. Could you clarify what I did wrong? Happy to adjust for future posts. Thanks!
   ```
5. Si regla es clara, acéptalo y no insistas

### "Shadowban en Reddit"
1. Ve a r/ShadowBan
2. Postea "Am I shadowbanned?"
3. Si sí:
   - Contacta admins de Reddit (no mods de subreddit)
   - https://www.reddit.com/appeals
   - Explica situación honestamente
4. Mientras tanto, NO postees más

### "Zero engagement después de 48h"
1. Analiza:
   - ¿Título clickbait o confuso?
   - ¿Post demasiado largo o corto?
   - ¿Timing malo? (ej: 3am hora de la comunidad)
   - ¿Comunidad no es target correcto?
2. NO borres el post
3. Ajusta para siguiente comunidad

### "Comentarios 100% negativos"
1. NO defensivo
2. Lee feedback honestamente
3. Agradece críticas:
   ```
   Thanks for the honest feedback. You're right about [issue]. I'll work on that.
   ```
4. Si crítica es sobre AI ethics/quality:
   - Admite limitaciones
   - Explica por qué AI (accesibilidad, costo)
   - Pregunta qué mejoraría su opinión
5. Si crítica es válida, DETÉN promoción y arregla primero

---

## 📝 LOGS Y TRACKING

### Archivos generados automáticamente
- `reddit_posts_log.txt`: URLs de posts de Reddit + timestamps
- `discord_posts_log.txt`: URLs de mensajes de Discord + timestamps

### Spreadsheet recomendado
Crea un Google Sheet con estas columnas:

| Fecha | Comunidad | URL | Upvotes/Reactions | Comments/Replies | Sentiment | Waitlist Signups | Sales | Notas |
|-------|-----------|-----|-------------------|------------------|-----------|------------------|-------|-------|
| 2026-06-06 | Club Español Discord | https://... | 12 👍 | 5 | Positivo | 3 | 0 | "Pidieron más títulos" |
| 2026-06-10 | r/webtoons | https://... | 47 ⬆️ | 23 | Mixto | 7 | 1 | "Debate AI ethics" |

---

## ✅ CHECKLIST FINAL

Antes de ejecutar, verifica:

- [ ] Muestras gratis subidas y link funciona en incognito
- [ ] Waitlist form funcional (testeado con email real)
- [ ] Landing page carga correctamente
- [ ] `reddit_poster.py` configurado con credenciales reales
- [ ] `discord_poster.py` configurado con token real
- [ ] Te uniste a Discord servers 3+ días antes
- [ ] Tienes 100+ karma en Reddit
- [ ] Has participado en r/manhwa o r/webtoons recientemente
- [ ] Leíste reglas de cada comunidad
- [ ] Preparaste tiempo para responder comments/replies diariamente

---

## 🎯 SIGUIENTE PASO

**AHORA**:
```bash
# 1. Sube las muestras a Google Drive
# 2. Configura el waitlist
# 3. Edita reddit_poster.py y discord_poster.py
# 4. Testea conexiones:
python reddit_poster.py  # Debe conectar y mostrar tu karma
python discord_poster.py  # Debe listar tus servers
```

**Día 1** (mañana o cuando estés listo):
```bash
python discord_poster.py  # Postea en Club Español
```

**Después**:
- Sigue el calendario
- Responde TODOS los comments
- Trackea métricas
- Ajusta según feedback

---

**Creado por**: Claude (Grop meta-agent)  
**Para**: Emmanuel Pedraza  
**Proyecto**: Manhua Premium Pack Launch  
**Última actualización**: 2026-06-05
