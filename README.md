# hmohanty

Personal site for **Hardhik Mohanty** — <https://hardhik-99.github.io/hmohanty/>

Editorial black-and-white single-page design, built with Jekyll and deployed on GitHub Pages.

## Repo layout

```
_config.yml             site-wide config
_data/
  news.yml              News section content (edit here)
  research.yml          Research Interests content (edit here)
_includes/              page partials (masthead, hero, photo, research, news)
_layouts/default.html   HTML shell (head, fonts, favicon, main, scripts)
assets/
  css/style.css         all site styles
  js/motion.js          subtle reveal animations
  img/                  favicon, original photo, B&W landscape crop
scripts/
  process_image.py      regenerate the B&W hero crop from the original
index.md                home page
```

## Local development

```bash
bundle install
bundle exec jekyll serve
```

Open <http://127.0.0.1:4000/hmohanty/> in a browser.

## Editing content

- **News** — edit [`_data/news.yml`](./_data/news.yml). Each entry takes `sort` (higher is newer), `date_year`, `date_month` (Roman numeral), `title`, and optional `body`, `link`, `link_label`. No HTML required beyond light inline tags in `body`.
- **Research interests** — edit [`_data/research.yml`](./_data/research.yml).
- **Profile photo** — replace `assets/img/hm_beach.jpeg` with any portrait photo, then run:

  ```bash
  pip install Pillow
  python scripts/process_image.py
  ```

  This regenerates `assets/img/hm_beach_bw.jpg` (the landscape B&W hero). Crop ratios live at the top of the script.

## Stack

- Jekyll + GitHub Pages
- [Fraunces](https://fonts.google.com/specimen/Fraunces) (display) + [EB Garamond](https://fonts.google.com/specimen/EB+Garamond) (body), served from Google Fonts
- [Font Awesome 6](https://fontawesome.com/) for social icons
- `jekyll-seo-tag` for meta / Open Graph / Twitter card tags
