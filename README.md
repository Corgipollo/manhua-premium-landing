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
