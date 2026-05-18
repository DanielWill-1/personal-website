# Daniel Velladurai — Personal Website

A static personal portfolio and academic website built with HTML, Tailwind CSS (CDN), and Material Symbols. Designed with a polished dark theme and responsive layout across all devices.

## Project Structure

```
personal-website/
├── new/                          # Main website pages
│   ├── index.html                # Landing / home page
│   ├── about.html                # Bio, education, skills, technical stack
│   ├── research.html             # Research focus areas & current projects
│   ├── publications.html         # Publication timeline with paper cards
│   ├── blogs.html                # Blog listing page
│   ├── blog1.html                # Individual blog post
│   ├── contact.html              # Contact page with email & social links
│   └── Daniel's Resume.pdf       # Downloadable CV
├── index.html                    # Root redirect/entry point
├── blog-post-1.html              # Additional blog post
├── blog-post-2.html              # Additional blog post
├── .gitignore
├── .gitattributes
├── LICENSE
└── README.md
```

## Tech Stack

- **HTML5** — semantic, accessible markup
- **Tailwind CSS** — utility-first CSS via CDN (`https://cdn.tailwindcss.com`)
- **Material Symbols** — Google's icon font via CDN
- **Google Fonts** — Inter (body) and Space Grotesk (headings)

No build step, no dependencies, no JavaScript frameworks — just open the HTML files in a browser.

## Tailwind Configuration

The project defines a custom design system via `tailwind.config` inline in each page, including:

- **Colors** — full Material You-inspired palette (surface, primary, secondary, tertiary variants)
- **Typography** — responsive type scale from `body-sm` to `display-lg` with custom letter-spacing and line heights
- **Spacing** — mobile gutter (`20px`), desktop gutter (`24px`), section gaps, container max-width (`1200px`)
- **Border radius** — consistent rounded corners (`DEFAULT: 0.25rem`, `lg: 0.5rem`, `xl: 0.75rem`, `full: 9999px`)

## Pages

### Home (`index.html`)
Hero section with name, title, and a brief tagline introducing the research focus.

### Research (`research.html`)
- Hero header with "Advancing Clinical Intelligence through Precision AI" tagline
- Three focus area cards (Medical AI, Computer Vision, Explainable AI) with tag chips
- Single featured project (Neuro-Symbolic Pathway Analysis) with code block, collaborators section, and hover glow effect

### Publications (`publications.html`)
- Chronological timeline layout with year headers
- Publication cards with venue badges, performance tags (e.g., SOTA: 96.8%), author lists, abstracts, and action links (PDF, GitHub, DOI)
- Currently features a single 2026 ICLR Oral Presentation publication

### About (`about.html`)
- Bio section with professional narrative
- Education card (B.Tech in Computer Science, Alliance University, 2022–2026)
- Core focus areas in a bento grid
- Technical Arsenal: ML frameworks, programming languages, and infrastructure tools displayed as chip-style tags

### Blog (`blogs.html`)
Blog post listing page with cards linking to individual posts.

### Contact (`contact.html`)
Minimalist contact page centered around the email address with hover reveal arrow icon, plus social links (GitHub, LinkedIn, Google Scholar).

## Getting Started

Clone the repository and open any HTML file directly in your browser — no server required.

```bash
git clone https://github.com/DanielWill-1/personal-website.git
cd personal-website
# Open new/index.html in your browser
```

For local development with live reload, you can use any static server:

```bash
npx serve .
```

## License

This project is open source. See [LICENSE](LICENSE) for details.

---

**© 2024 Daniel Velladurai**
