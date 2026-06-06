# Manhua Narrado Premium - Landing Page

Landing page profesional para la venta del Pack Premium de Manhua Narrado.

## 🎯 Características

- Hero section con CTA destacado
- Sección de features (6 características clave)
- Preview section para demo
- Pricing con oferta especial ($4.99)
- FAQ completa
- Diseño premium con Tailwind CSS
- Animaciones sutiles
- Responsive mobile-first
- SEO optimizado

## 🚀 Deploy

Esta página está desplegada en GitHub Pages:
**URL:** https://corgipollo.github.io/manhua-premium-landing/

## ⚙️ Configuración

### Configurar Waitlist (Captura de Emails)

**Opción 1: Google Forms (Recomendado)**
1. Ve a https://forms.google.com y crea un nuevo formulario
2. Agrega campo "Email" y "Nombre (opcional)"
3. Click en "Enviar" → pestaña "< >" (Embed)
4. Copia el iframe embed code
5. En `index.html`, busca `<!-- Opción 2: Google Form embed -->`
6. Reemplaza `TU_GOOGLE_FORM_EMBED_URL_AQUI` con tu URL
7. Descomenta esa sección y comenta la Opción 1

**Opción 2: Formspree (Más fácil)**
1. Ve a https://formspree.io (gratis, sin registro)
2. Crea una cuenta y un nuevo form
3. Copia tu Form ID
4. En `index.html`, busca `action="https://formspree.io/f/YOUR_FORM_ID"`
5. Reemplaza `YOUR_FORM_ID` con tu ID de Formspree

**Opción 3: Google Sheets via Apps Script**
1. Crea una Google Sheet nueva
2. Extensions → Apps Script
3. Pega este código:
```javascript
function doPost(e) {
  const sheet = SpreadsheetApp.getActiveSheet();
  const data = JSON.parse(e.postData.contents);
  sheet.appendRow([data.timestamp, data.email, data.name]);
  return ContentService.createTextOutput(JSON.stringify({result: "success"}));
}
```
4. Deploy → New deployment → Web app → Deploy
5. Copia el URL y pégalo en `GOOGLE_SCRIPT_URL` en `index.html`

### Agregar Stripe Payment Link

1. Crea tu Payment Link en Stripe Dashboard
2. Abre `index.html`
3. Busca la línea: `const STRIPE_PAYMENT_LINK = 'TU_STRIPE_PAYMENT_LINK_AQUI';`
4. Reemplaza `'TU_STRIPE_PAYMENT_LINK_AQUI'` con tu URL de Stripe
5. Commit y push los cambios

Ejemplo:
```javascript
const STRIPE_PAYMENT_LINK = 'https://buy.stripe.com/test_xxxxxxxxxxxxx';
```

## 📦 Estructura

```
manhua-premium-landing/
├── index.html          # Página principal
└── README.md          # Este archivo
```

## 🎨 Stack

- HTML5
- Tailwind CSS v3 (CDN)
- Vanilla JavaScript
- Google Fonts (Inter)

## 📝 Siguientes pasos

1. ✅ Deploy a GitHub Pages
2. ⏳ Crear Stripe Payment Link
3. ⏳ Agregar Payment Link al HTML
4. ⏳ (Opcional) Agregar video preview real
5. ⏳ (Opcional) Agregar dominio custom

---

Creado con ❤️ para Emmanuel Pedraza
