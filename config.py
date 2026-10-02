"""
Configuration loader for job-apply-mcp.

Secrets and browser sessions stay outside git under ~/.job-apply-mcp.
Candidate profiles live in the repo configuration so the correct resume,
search terms and autofill answers can be selected automatically.
"""

from __future__ import annotations

import json
import platform
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

APP_DIR = Path.home() / ".job-apply-mcp"
CONFIG_PATH = APP_DIR / "config.json"
SESSIONS_DIR = APP_DIR / "sessions"
DB_PATH = APP_DIR / "applications.db"
PROJECT_DIR = Path(__file__).resolve().parent


def _default_profile(
    *,
    resume_path: str,
    target_roles: list[str],
    search_keywords: list[str],
    title_gate: list[str],
    skills: list[str],
    avoid_keywords: list[str],
    experience: dict[str, str],
) -> dict[str, Any]:
    return {
        "resume_path": resume_path,
        "target_roles": target_roles,
        "default_search_keywords": search_keywords,
        "title_must_contain": title_gate,
        "skills": skills,
        "avoid_keywords": avoid_keywords,
        "autofill": {
            "gender": "Male",
            "date_of_birth": "05/10/1995",
            "preferred_locations": [
                "Remote", "Bangalore", "Bengaluru", "Hyderabad",
                "Pune", "Delhi", "Mumbai", "Noida", "Gurgaon", "Gurugram",
                "India",
            ],
            "any_location": True,
            "experience": experience,
            "notice_period": "90 days",
            "current_ctc": "20.56",
            "expected_ctc": "35",
            "total_experience": "7",
            "primary_cloud": "AWS",
            "current_status": "Currently Working",
            "last_working_day": "Currently Working",
            "contract_based": "Yes",
            "willing_to_relocate": "Yes",
            "willing_to_work_hybrid": "Yes",
            "willing_to_work_onsite": "Yes",
            "certifications": [],
            "avoid_companies": ["coditas"],
        },
    }


DEFAULT_CONFIG: dict[str, Any] = {
    "active_profile": "backend",
    "name": "Divyanshu Mishra",
    "email": "mishradivyanshu05@gmail.com",
    "phone": "+91-7015973134",
    "location": "India",
    "experience_years": 7,
    "platforms": ["indeed", "instahyre", "hirist", "cutshort", "foundit"],
    "credentials": {
        "indeed": {"email": "", "password": ""},
        "instahyre": {"email": "", "password": ""},
        "hirist": {"email": "", "password": ""},
        "cutshort": {"email": "", "password": ""},
        "foundit": {"email": "", "password": ""},
    },
    "profiles": {
        "backend": _default_profile(
            resume_path="resumes/Divyanshu_Mishra_Backend_Engineer_Resume.pdf",
            target_roles=[
                "Python Backend Engineer",
                "Backend Engineer",
                "Backend Software Engineer",
                "Software Engineer Backend",
                "Python Developer",
                "Django Developer",
                "Django REST Framework Developer",
                "SDE 2 Backend",
                "API Engineer",
                "Microservices Engineer",
            ],
            search_keywords=[
                "Python Backend Engineer",
                "Backend Engineer Python",
                "Python Developer Django",
                "Django REST Framework",
                "Backend Software Engineer",
                "SDE 2 Backend",
                "Python API Engineer",
                "Microservices Engineer Python",
            ],
            title_gate=[
                "backend", "python", "django", "api engineer",
                "software engineer", "microservices",
            ],
            skills=[
                "Python", "Django", "Django REST Framework", "FastAPI",
                "Node.js", "Express.js", "REST", "GraphQL", "gRPC",
                "Microservices", "AWS", "Lambda", "API Gateway", "EKS",
                "S3", "RDS", "ECR", "PostgreSQL", "MySQL", "MongoDB",
                "Redis", "Celery", "RabbitMQ", "Elasticsearch", "Docker",
                "Kubernetes", "Terraform", "GitHub Actions", "Jenkins",
                "GitLab CI", "pytest", "Jest", "SQL", "TypeScript",
            ],
            avoid_keywords=[
                "frontend", "react developer", "angular developer",
                "vue developer", "android", "ios", "swift", "kotlin",
                "flutter", "data scientist", "machine learning researcher",
                "deep learning researcher", "helpdesk", "help desk",
                "desktop support", "service desk", "l1 support", "l2 support",
            ],
            experience={
                "python": "7",
                "django": "7",
                "django rest framework": "7",
                "drf": "7",
                "rest": "7",
                "sql": "7",
                "postgresql": "5",
                "mysql": "5",
                "aws": "5",
                "lambda": "5",
                "api gateway": "5",
                "docker": "5",
                "kubernetes": "5",
                "eks": "5",
                "redis": "3",
                "celery": "3",
                "rabbitmq": "3",
                "typescript": "5",
                "node.js": "5",
            },
        ),
        "data_engineer": _default_profile(
            resume_path="resumes/Divyanshu_Mishra_Data_Engineer_Resume.pdf",
            target_roles=[
                "Data Engineer",
                "Senior Data Engineer",
                "Big Data Engineer",
                "Data Platform Engineer",
                "Spark Engineer",
                "ETL Engineer",
                "Data Pipeline Engineer",
                "Data Engineering",
                "Analytics Engineer",
            ],
            search_keywords=[
                "Data Engineer",
                "Senior Data Engineer",
                "Big Data Engineer",
                "Apache Spark Engineer",
                "PySpark Engineer",
                "Scala Data Engineer",
                "ETL Engineer",
                "AWS Data Engineer",
                "Data Platform Engineer",
            ],
            title_gate=[
                "data engineer", "data engineering", "big data",
                "spark engineer", "pyspark", "etl engineer",
                "data platform", "data pipeline", "analytics engineer",
            ],
            skills=[
                "Apache Spark", "Spark", "PySpark", "Scala", "SQL",
                "ETL", "ELT", "AWS", "EMR", "Glue", "S3", "Athena",
                "Step Functions", "Apache Airflow", "Airflow", "Hudi",
                "Parquet", "Data Lake", "Data Pipeline", "Data Transformation",
                "Schema Design", "Lambda", "API Gateway", "EKS", "RDS",
                "ECR", "Terraform", "Python", "Django", "Django REST Framework",
                "PostgreSQL", "MySQL", "MongoDB", "Elasticsearch", "Docker",
                "Kubernetes", "GitHub Actions", "Jenkins", "GitLab CI",
                "TypeScript", "JavaScript",
            ],
            avoid_keywords=[
                "frontend", "react developer", "angular developer",
                "vue developer", "android", "ios", "swift", "kotlin",
                "flutter", "data scientist", "machine learning researcher",
                "deep learning researcher", "research scientist",
                "helpdesk", "help desk", "desktop support", "service desk",
                "l1 support", "l2 support", "backend developer only",
            ],
            experience={
                "python": "7",
                "sql": "7",
                "etl": "5",
                "spark": "5",
                "apache spark": "5",
                "pyspark": "5",
                "scala": "5",
                "aws": "5",
                "emr": "5",
                "s3": "5",
                "glue": "5",
                "athena": "5",
                "step functions": "5",
                "airflow": "5",
                "apache airflow": "5",
                "lambda": "5",
                "terraform": "5",
                "postgresql": "5",
                "docker": "5",
                "kubernetes": "5",
            },
        ),
    },
}


@dataclass
class AppConfig:
    active_profile: str = "backend"
    name: str = ""
    email: str = ""
    phone: str = ""
    location: str = "India"
    experience_years: int = 7
    platforms: list[str] = field(default_factory=list)
    credentials: dict[str, dict[str, str]] = field(default_factory=dict)
    profiles: dict[str, dict[str, Any]] = field(default_factory=dict)

    @property
    def profile(self) -> dict[str, Any]:
        return self.profiles.get(self.active_profile, {})

    @property
    def resume_path(self) -> str:
        return self.resolved_resume_path()

    @property
    def autofill(self) -> dict[str, Any]:
        return self.profile.get("autofill", {})

    @property
    def resume_exists(self) -> bool:
        path = Path(self.resume_path).expanduser()
        if not path.is_absolute():
            path = PROJECT_DIR / path
        return path.is_file()

    def resolved_resume_path(self) -> str:
        path = Path(self.resume_path).expanduser()
        if not path.is_absolute():
            path = PROJECT_DIR / path
        return str(path.resolve())


def ensure_dirs() -> None:
    APP_DIR.mkdir(parents=True, exist_ok=True)
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)


def load_config() -> AppConfig:
    ensure_dirs()
    if not CONFIG_PATH.exists():
        CONFIG_PATH.write_text(json.dumps(DEFAULT_CONFIG, indent=2))

    raw = json.loads(CONFIG_PATH.read_text())
    # Merge newly-added defaults without overwriting user credentials/customisations.
    merged = json.loads(json.dumps(DEFAULT_CONFIG))
    merged.update({k: v for k, v in raw.items() if k not in {"profiles", "credentials"}})
    merged["credentials"].update(raw.get("credentials", {}))
    for profile_name, profile in raw.get("profiles", {}).items():
        merged["profiles"].setdefault(profile_name, {}).update(profile)
        if "autofill" in profile:
            merged["profiles"][profile_name].setdefault("autofill", {}).update(profile["autofill"])

    return AppConfig(
        active_profile=merged.get("active_profile", "backend"),
        name=merged.get("name", ""),
        email=merged.get("email", ""),
        phone=merged.get("phone", ""),
        location=merged.get("location", "India"),
        experience_years=merged.get("experience_years", 7),
        platforms=merged.get("platforms", ["indeed", "instahyre", "hirist", "cutshort", "foundit"]),
        credentials=merged.get("credentials", {}),
        profiles=merged.get("profiles", {}),
    )


def save_config(config: AppConfig) -> None:
    ensure_dirs()
    data = {
        "active_profile": config.active_profile,
        "name": config.name,
        "email": config.email,
        "phone": config.phone,
        "location": config.location,
        "experience_years": config.experience_years,
        "platforms": config.platforms,
        "credentials": config.credentials,
        "profiles": config.profiles,
    }
    CONFIG_PATH.write_text(json.dumps(data, indent=2))


def get_user_agent() -> str:
    os_name = platform.system()
    if os_name == "Windows":
        return "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0"
    if os_name == "Darwin":
        return "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:128.0) Gecko/20100101 Firefox/128.0"
    return "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
