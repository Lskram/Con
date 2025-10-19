# ProfileV2 - Django + Tailwind + Vercel Starter

Modern Django 5 starter prewired with Tailwind CSS, Whitenoise static handling, and a Vercel-ready serverless entry point. Ideal for a personal profile or portfolio launch.

## Requirements

- Python 3.12+
- Node.js 18+ (includes npm)
- Git

## 1. Setup & Local Development

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows PowerShell
source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
npm install
npm run tailwind:build
python manage.py migrate
python manage.py runserver
```

### Tailwind workflow

- `npm run tailwind:watch` - rebuild CSS on file changes.
- Source file lives in `assets/css/input.css`.
- Generated CSS output is written to `static/css/tailwind.css` and consumed via `{% load static %}` in templates.

## 2. Environment Variables

Local development uses `.env` (already added to `.gitignore`). Adjust values as needed:

```
DEBUG=True
SECRET_KEY=...
ALLOWED_HOSTS=127.0.0.1,localhost,.vercel.app
CSRF_TRUSTED_ORIGINS=https://*.vercel.app
DATABASE_URL=sqlite:///db.sqlite3            # optional override
```

For Vercel, add the same keys through **Project Settings -> Environment Variables** and set `DEBUG=False`.

## 3. Deployment on Vercel

1. Install the CLI and authenticate:
   ```bash
   npm i -g vercel
   vercel login
   ```
2. Inside the project folder:
   ```bash
   vercel link                  # create or connect to a Vercel project
   vercel env add               # add SECRET_KEY, DEBUG, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS, DATABASE_URL (if any)
   vercel --prod                # first production deploy
   ```

The provided `vercel.json` config runs:

```bash
pip install -r requirements.txt \
&& npm install \
&& npm run tailwind:build \
&& python manage.py collectstatic --noinput
```

and exposes `api/index.py` as the serverless WSGI entry point. Static assets are collected into `staticfiles/` and served with Whitenoise.

## 4. Useful Extras

- `git status` - confirm clean working tree before commits.
- `python manage.py createsuperuser` - create admin user if needed.
- `npm run build` - one-off Tailwind build (invoked automatically by Vercel).

---

Thai quick start (สรุปย่อ):

1. `python -m venv .venv` แล้ว activate
2. `pip install -r requirements.txt`
3. `npm install` และ `npm run tailwind:build`
4. `python manage.py migrate` แล้ว `python manage.py runserver`
5. เตรียม environment บน Vercel (`vercel login`, `vercel link`, `vercel --prod`)

ปรับเนื้อหาใน `templates/core/home.html` เพื่อให้ตรงกับโปรไฟล์ของคุณ แล้ว deploy ได้ทันที
