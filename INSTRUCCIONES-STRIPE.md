# 🚀 Instrucciones para Activar el Payment Link de Stripe

## ✅ LANDING PAGE LISTA

Tu landing page ya está publicada en:
**https://corgipollo.github.io/manhua-premium-landing/**

## 📝 SIGUIENTE PASO: Agregar Stripe Payment Link

### 1. Crear Payment Link en Stripe

1. Ve a tu dashboard de Stripe: https://dashboard.stripe.com/
2. Click en **"Products"** → **"Add product"**
3. Configura el producto:
   - **Name:** Pack Premium Manhua Narrado
   - **Description:** Más de 100 episodios premium narrados en español
   - **Price:** $4.99 USD (one-time)
   - **Image:** (opcional, sube una imagen del pack)
4. Click **"Save product"**
5. En la página del producto, click en **"Create payment link"**
6. Configuración del link:
   - **Quantity:** No permitir que el cliente cambie cantidad
   - **Success message:** "¡Gracias por tu compra! Revisa tu email para acceder al contenido."
   - **Collect customer email:** ✅ Activado (IMPORTANTE para enviar el contenido)
7. Click **"Create link"**
8. Copia la URL del payment link (algo como: `https://buy.stripe.com/xxxxxxxxxxxxx`)

### 2. Agregar el Link a la Landing Page

Tienes 2 opciones:

#### Opción A: Editar en GitHub (más rápido)

1. Ve a: https://github.com/Corgipollo/manhua-premium-landing
2. Click en `index.html`
3. Click en el ícono de lápiz (Edit)
4. Busca la línea **595** (aprox):
   ```javascript
   const STRIPE_PAYMENT_LINK = 'TU_STRIPE_PAYMENT_LINK_AQUI';
   ```
5. Reemplaza `'TU_STRIPE_PAYMENT_LINK_AQUI'` con tu link de Stripe:
   ```javascript
   const STRIPE_PAYMENT_LINK = 'https://buy.stripe.com/test_xxxxxxxxxxxxx';
   ```
6. Scroll abajo y click **"Commit changes"**
7. Espera 1-2 minutos y la página se actualizará automáticamente

#### Opción B: Editar local

1. Abre `index.html` en tu editor
2. Busca la línea 595 (o busca: `TU_STRIPE_PAYMENT_LINK_AQUI`)
3. Reemplaza con tu link de Stripe
4. Guarda el archivo
5. Abre terminal en la carpeta del proyecto:
   ```bash
   cd "C:\Users\Emmanuel\Documents\manhua-premium-landing"
   git add index.html
   git commit -m "Add Stripe Payment Link"
   git push
   ```
6. Espera 1-2 minutos para que GitHub Pages se actualice

## 🎯 VERIFICAR QUE FUNCIONA

1. Ve a: https://corgipollo.github.io/manhua-premium-landing/
2. Click en cualquier botón "Obtener Acceso Ahora"
3. Debe abrirse tu página de pago de Stripe
4. ✅ Si abre Stripe, ¡está funcionando!

## 📧 SIGUIENTE PASO: Automatizar Entrega de Contenido

Una vez que recibas pagos, necesitarás enviar el link de descarga. Opciones:

### Opción 1: Manual (rápido para empezar)
- Cuando recibas notificación de pago en Stripe
- Envía email manualmente con el link de descarga

### Opción 2: Automático con Zapier/Make (recomendado)
1. Stripe Webhook → Trigger cuando hay nuevo pago
2. Enviar email automático con link de descarga
3. (Puedo ayudarte a configurar esto después)

### Opción 3: Stripe Email Automation (built-in)
- En Stripe, puedes configurar un email automático post-compra
- Dashboard → Settings → Emails → Receipt emails
- Personaliza el mensaje para incluir instrucciones de descarga

## 🔗 LINKS IMPORTANTES

- **Landing Page:** https://corgipollo.github.io/manhua-premium-landing/
- **Repositorio:** https://github.com/Corgipollo/manhua-premium-landing
- **Stripe Dashboard:** https://dashboard.stripe.com/

## ❓ TROUBLESHOOTING

**P: Los botones no abren Stripe**
R: Verifica que el link en `index.html` esté correcto (sin comillas extras)

**P: La página no se actualiza después del commit**
R: GitHub Pages tarda 1-2 minutos. Limpia caché (Ctrl+Shift+R)

**P: Quiero cambiar el precio**
R: Edita `index.html` en las secciones de pricing (busca `$4.99`)

---

**¿Necesitas ayuda?** Pídemelo y te guío paso a paso.
