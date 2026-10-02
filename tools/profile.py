"""
Candidate profiles and job relevance matching.

The active profile is selected from ~/.job-apply-mcp/config.json and controls
target roles, search keywords, skills, title gating and exclusion rules.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from difflib import SequenceMatcher
from typing import Any

from config import load_config


@dataclass(frozen=True)
class CandidateProfile:
    title: str
    skills: tuple[str, ...]
    target_roles: tuple[str, ...]
    default_search_keywords: tuple[str, ...]
    title_must_contain: tuple[str, ...]
    avoid_keywords: tuple[str, ...]


def get_active_profile() -> CandidateProfile:
    cfg = load_config()
    p = cfg.profile
    return CandidateProfile(
        title=cfg.active_profile,
        skills=tuple(p.get("skills", [])),
        target_roles=tuple(p.get("target_roles", [])),
        default_search_keywords=tuple(p.get("default_search_keywords", [])),
        title_must_contain=tuple(p.get("title_must_contain", [])),
        avoid_keywords=tuple(p.get("avoid_keywords", [])),
    )


def _normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9 /+#.-]", " ", text.lower()).strip()


def _fuzzy_ratio(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def _token_overlap(tokens_a: set[str], tokens_b: set[str]) -> float:
    if not tokens_a or not tokens_b:
        return 0.0
    return len(tokens_a & tokens_b) / len(tokens_a)


def compute_match_score(
    job_title: str,
    job_description: str,
    job_location: str,
    required_skills: list[str] | None = None,
    profile: CandidateProfile | None = None,
) -> float:
    profile = profile or get_active_profile()
    norm_title = _normalize(job_title)
    norm_desc = _normalize(job_description)
    combined_text = f"{norm_title} {norm_desc}"

    role_scores: list[float] = []
    for role in profile.target_roles:
        norm_role = _normalize(role)
        role_scores.append(1.0 if norm_role in norm_title else _fuzzy_ratio(norm_role, norm_title))
    role_score = max(role_scores) if role_scores else 0.0

    profile_skills_norm = {_normalize(s) for s in profile.skills}
    if required_skills:
        job_skills_norm = {_normalize(s) for s in required_skills}
        skill_score = _token_overlap(job_skills_norm, profile_skills_norm)
    else:
        matched = sum(1 for s in profile_skills_norm if s in combined_text)
        skill_score = min(matched / max(len(profile_skills_norm) * 0.3, 1), 1.0)

    # Any location is acceptable; location remains a relevance signal when a
    # job is explicitly remote, in India, or in one of the common Indian hubs.
    norm_location = _normalize(job_location)
    location_score = 1.0 if (
        "remote" in norm_location
        or "india" in norm_location
        or any(x in norm_location for x in (
            "bangalore", "bengaluru", "hyderabad", "pune", "delhi",
            "mumbai", "noida", "gurgaon", "gurugram", "chennai",
        ))
    ) else 0.5

    avoid_penalty = 1.0 if any(_normalize(kw) in combined_text for kw in profile.avoid_keywords) else 0.0

    score = 0.35 * role_score + 0.40 * skill_score + 0.15 * location_score - 0.10 * avoid_penalty
    return round(max(0.0, min(score, 1.0)), 3)


def should_exclude(
    job_title: str,
    job_description: str,
    required_skills: list[str] | None = None,
    profile: CandidateProfile | None = None,
) -> bool:
    profile = profile or get_active_profile()
    combined = _normalize(f"{job_title} {job_description}")
    return any(_normalize(kw) in combined for kw in profile.avoid_keywords)


def title_is_relevant(job_title: str, profile: CandidateProfile | None = None) -> bool:
    profile = profile or get_active_profile()
    norm = _normalize(job_title)
    return any(_normalize(kw) in norm for kw in profile.title_must_contain)
