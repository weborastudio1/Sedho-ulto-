# WEBORA Studio — Round 2 Production Upgrade

This build preserves the supplied site as the base and adds production hardening requested by the Round 2 review.

## Included
- Original pages and original raster assets preserved.
- WebP derivatives and a dedicated 1200×630 OG image added.
- Self-hosted Font Awesome; no CDN dependency.
- Mobile navigation tap/overlay hardening, safe-area handling and overflow protection.
- Dependency-free interactive 3D hero background with pointer response and reduced-motion support.
- Portfolio keeps all existing cards and adds progressive “Load more” behaviour.
- Contact + career forms submit to `/api/submit`; career supports a PDF/DOC/DOCX resume up to 3 MB.
- Honeypot, consent and success/error states.
- Unique blog article pages with Article schema.
- Page-specific canonical/OG URLs, production sitemap and robots.
- Vercel security/cache headers.

## Form deployment
Set these Vercel environment variables before launch:
- `RESEND_API_KEY`
- `WEBORA_TO_EMAIL` (defaults to `weborastudiozz@gmail.com`)
- `WEBORA_FROM_EMAIL` (a verified Resend sender is recommended for production)

Without the mail environment variables, the site deliberately shows a clear fallback message instead of pretending that an enquiry was delivered.

## QA
Run `node --check js/main.js api/submit.js` and serve the folder with a local HTTP server before deployment. Then test Home, Portfolio, Contact and Career at 320/360/390/414px and on at least two real phones.
