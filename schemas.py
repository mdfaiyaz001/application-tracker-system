from pydantic import BaseModel

class ApplicationBase(BaseModel):
    company_name: str
    job_role: str
    status: str
    applied_date: str
    notes: str

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationResponse(ApplicationBase):
    id: int

    class Config:
        orm_mode = True