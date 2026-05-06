from sqlalchemy import Column, Integer, String
from database import Base

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    job_role = Column(String)
    status = Column(String)
    applied_date = Column(String)
    notes = Column(String)