# Daniel Willson Velladurai — Personal Website

A premium single-page research portfolio built with HTML and Tailwind CSS (CDN). Dark mode, editorial typography, calm blue accent — designed to feel like a modern AI research lab homepage.

## Project Structure

```
personal-website/
├── index.html              # Single-page portfolio (hero, research, about, projects, publications, timeline, skills, writing, contact)
├── blogs.html              # Blog listing page
├── blog1.html              # Individual blog post
├── Daniel's Resume.pdf     # Downloadable CV
├── .gitignore
├── .gitattributes
├── LICENSE
└── README.md
```

## Tech Stack

- **HTML5** — semantic markup
- **Tailwind CSS** — utility-first CSS via CDN
- **Google Fonts** — Inter (body) + Space Grotesk (headings)
- **Intersection Observer** — subtle fade-up animations on scroll

No build step, no JavaScript frameworks.

## Design System

- **Background**: `#121417` (charcoal, not black)
- **Accent**: `#4f8cff` (calm blue)
- **Cards**: `#1a1f2b` with `rgba(255,255,255,0.07)` borders
- **Max width**: 1200px, generous whitespace
- **Animations**: fade-up only, 400ms

## Sections

| Section | Description |
|---------|-------------|
| Hero | Name, title, mission, CTAs, credibility metrics |
| Research | Three focus area cards (Medical AI, Computer Vision, Explainable AI) |
| About | Professional bio + focus areas sidebar |
| Projects | Featured paper with metrics |
| Publications | 3 conference papers, 3 journal papers, 1 in prep, 2 upcoming |
| Timeline | Education (B.Tech CSE AI & ML, Alliance University 2022–2026) |
| Skills | ML frameworks, languages, infrastructure (grouped by domain) |
| Writing | Blog preview linking to full posts |
| Contact | Email + social links |

## Getting Started

Open `index.html` directly in a browser — no server required.

```bash
git clone https://github.com/DanielWill-1/personal-website.git
cd personal-website
# Open index.html
```

For local development with live reload:

```bash
npx serve .
```

## License

See [LICENSE](LICENSE).
