from pydantic import BaseModel

from backend.src.vacancy.models import WorkFormat, Experience, Education, EmploymentType


class VacancyCreate(BaseModel):
    job_title: str
    city: str | None
    company: str
    experience: Experience | None
    work_format: WorkFormat | None
    salary: int | None
    education: Education | None
    employment_type: EmploymentType | None
    skills: list[str] | None
    description: str | None


class VacancyRead(BaseModel):
    job_title: str | None
    city: str | None
    company: str
    experience: Experience | None
    work_format: WorkFormat | None
    salary: int | None
    education: Education | None
    employment_type: EmploymentType | None
    skills: list[str] | None
    description: str | None


class VacanciesRead(BaseModel):
    vacancies: list[VacancyRead]


class VacancyUpdate(VacancyCreate):
    pass
