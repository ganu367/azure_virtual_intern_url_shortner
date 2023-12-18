from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, BIGINT, ForeignKey, DateTime, TIMESTAMP, UniqueConstraint, TEXT, FLOAT, Numeric, CheckConstraint
from database import Base
from sqlalchemy.orm import relationship
current_date = datetime.today()
# format_date = current_date.strftime("%Y-%m-%d")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    username = Column(String, unique=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_by = Column(String)
    created_on = Column(DateTime, default=current_date)
    modified_by = Column(String)
    modified_on = Column(DateTime, default=current_date)

    # # Constraints
    # __table_args__ = (UniqueConstraint(
    #     'username', 'email_address', name='unq_1'),)

    url = relationship("URL", back_populates="user")
    contact_us_user = relationship(
        "CONTACTUS", back_populates="contact_us_onwer")


class URL(Base):
    __tablename__ = "url"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(
        "users.id"))  # refer from Plant id
    # random string
    key = Column(String, nullable=False)
    # secret for manage url
    # secrete_key = Column(String, nullable=False)
    click_count = Column(Integer, default=0)
    target_url = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_by = Column(String)
    created_on = Column(DateTime, default=current_date)
    modified_by = Column(String)
    modified_on = Column(DateTime, default=current_date)

    user = relationship("User", back_populates="url")


class CONTACTUS(Base):
    __tablename__ = "contact_us"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(
        "users.id"))
    name = Column(String)
    email = Column(String, nullable=False)
    mobile_number = Column(Numeric)
    messages = Column(String, nullable=False)
    created_by = Column(String)
    created_on = Column(DateTime, default=current_date)
    modified_by = Column(String)
    modified_on = Column(DateTime, default=current_date)

    contact_us_onwer = relationship("User", back_populates="contact_us_user")
