# Local setup for the two candidate profiles

The repository is preconfigured for two application profiles:

- `backend` — Python/Django backend roles
- `data_engineer` — Spark/Scala/AWS data-engineering roles

Personal resumes are intentionally **not committed** to the public repository.

## 1. Put the resumes in the repo

Create `resumes/` and place these files there:

```text
resumes/
├── Divyanshu_Mishra_Backend_Engineer_Resume.pdf
└── Divyanshu_Mishra_Data_Engineer_Resume.pdf
```

The configured paths already point to these filenames.

## 2. Install and start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install firefox
python run.py
```

The first run creates:

```text
~/.job-apply-mcp/config.json
~/.job-apply-mcp/sessions/
~/.job-apply-mcp/applications.db
```

## 3. Add portal credentials

Edit only the `credentials` section of:

```text
~/.job-apply-mcp/config.json
```

Configured portals:

- Indeed
- Instahyre
- Hirist
- Cutshort
- Foundit

Passwords are optional if you use the browser-based `save_session` login flow. Do not commit the generated config.

## 4. Select the resume/profile

The default is:

```json
"active_profile": "backend"
```

For Data Engineering:

```json
"active_profile": "data_engineer"
```

The active profile controls:

- resume
- target job titles
- search keywords
- skill matching
- title gate
- technology-specific experience answers
- common application answers
- excluded companies

## 5. Your configured application facts

- Name: Divyanshu Mishra
- Experience: 7 years
- Current CTC: 20.56 LPA
- Expected CTC: 35 LPA
- Notice period: 90 days
- Current status: Working
- DOB: 05/10/1995
- Gender: Male
- Location preference: Any location
- Remote: acceptable
- Hybrid: acceptable
- Onsite/relocation: acceptable
- Contract/C2H: acceptable
- Company exclusion: Coditas

## 6. Important: preview before real applications

Use search/filter first and inspect the shortlist. For actual submissions, explicitly use:

```text
dry_run=false
```

Applications cannot be withdrawn through this tool.

## 7. Sessions

The recommended workflow is to use `save_session` and log in manually in the browser. This keeps portal passwords out of the repository/config whenever the portal supports session login.

Foundit support has been added to search/session/apply. Its current public search pages use URLs such as `/search/data-engineer-jobs`; the adapter uses that public search structure and the common matcher for relevance filtering.
