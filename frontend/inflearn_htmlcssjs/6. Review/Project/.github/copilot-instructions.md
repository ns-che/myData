## Quick context

This is a small, static frontend demo (no build system). Key files:
- `Service.html` — single-page entry; links FontAwesome and Google fonts via CDN and includes `Service.css` and `Service.js`.
- `Service.css` — global styles and responsive rules (media queries use `min-width: 992px`).
- `Service.js` — plain global JS functions manipulating DOM by `id`/`class` (no modules or bundlers).
- `img/` — contains slide and profile images (e.g. `gpt-img1.jpg`...`gpt-img5.jpg`).

## Big picture / why

The project is intentionally minimal: a single HTML document, a stylesheet, and a script. Interactivity is implemented with global functions that target specific `id` values (e.g. `toggleBtn`, `menu`, `imageNext`, `firstDot`). Keep changes simple and local — avoid introducing a bundler or framework unless converting the whole repo.

## Important patterns and conventions (copyable examples)
- DOM targeting by ID: document.getElementById("menu") / `toggleBtn` / `imagePrev`, `imageNext`, `firstDot`... — prefer updating these exact IDs when changing markup.
- Slider API: `imageTimer = setInterval(imageSlideTimer, 3000)` controls auto-advance; change interval by editing this line in `Service.js`.
- Header behavior: `scrollFunction()` toggles the `navbar-fixed` class on `#header`. If you adjust spacing, check CSS rules for `.header-area.navbar-fixed` and the top margin logic in JS.
- Menu: `menuToggle()` toggles the `show` class on `#menu`; CSS `.navbar-menu.show` sets height to `200px` on small screens — change both JS and CSS together.
- CSS breakpoints: responsive behavior is done with `@media (min-width: 992px)`; desktop-first tweaks appear there.

## Files to edit for common tasks
- Change slide images: replace files in `img/` and update `<img src="...">` nodes in `Service.html`.
- Change nav links or labels: edit `Service.html` directly — JS hooks assume those elements exist with the current IDs.
- Tweak slider timing: edit `Service.js` (search for `setInterval(imageSlideTimer`).

## Integration points / external deps
- External CDNs used in `Service.html`: FontAwesome and Google Fonts. Offline environments must have these available or be replaced with local assets.

## Debugging tips (project-specific)
- Missing interactivity? Open DevTools console — errors will usually be from `document.getElementById(...)` returning null because an ID changed in `Service.html`.
- Layout differences across sizes: inspect the `.navbar-menu` element and its `.show` class — on desktop the menu becomes relative and uses different styles under `@media (min-width: 992px)`.
- Text sizing oddity: `* { font-size:0 }` is present in `Service.css`. Many elements explicitly reset font sizes (e.g., `a { font-size:14px }`). When adding new text elements, set an explicit font-size to avoid invisible text.

## What an AI agent should do first
1. Open `Service.html` to understand current DOM and IDs.
2. If changing behavior, update both `Service.html` (markup IDs/classes) and `Service.js` (matching selectors) together.
3. Prefer minimal, local edits: this is a single-page static site — avoid adding complex tooling.

## Example edits (explicit snippets to use)
- To change slider speed, update in `Service.js`:
  - Old: `var imageTimer = setInterval(imageSlideTimer, 3000);`
  - New: `var imageTimer = setInterval(imageSlideTimer, 5000);`  // 5s
- To add a new dot for slide 5, add `<span class="dot" id="fifthDot"></span>` to the `.dots` block in `Service.html` and wire it in `Service.js` with `document.getElementById("fifthDot").addEventListener("click", currentImageSlide.bind(null, 5));`

## Edits to avoid
- Introducing module bundlers, transpilers, or CSS-in-JS without a repo-wide plan — this repo is structured as a simple static prototype.
- Removing the global `font-size:0` without auditing all elements for explicit font sizes.

## When to ask the maintainer
- If you plan to convert to a component system, bundler, or test harness — get approval first.
- If you need to replace CDNs for offline hosting (provide the local asset replacements).

---
If you want, I can (a) add a short README documenting how to preview the page locally, or (b) convert the slider to a slightly more modular pattern. Which would you prefer? 
