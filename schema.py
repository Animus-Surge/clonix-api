"""
Database schema definition
"""

import datetime
from enum import Enum

from sqlalchemy import JSON, DateTime, BigInteger, ForeignKey, MetaData, Table, Column, Integer, String, func, null
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from typing import Literal

# Metadata object
metadata_obj = MetaData()

# Enum/Literal decl
NotificationTargetType = Literal['User', 'Group', 'System']
NotificationSeverity = Literal['Normal', 'Increased', 'Severe', 'Critical']

AuditLogStatus = Literal["Allowed", "Blocked", "Other"]

KeyType = Literal["Encryption", "BIOS", "Other"]

# Table decl

class ClonixTableBase(DeclarativeBase):
    type_annotation_map = {
        dict: JSON
    }
    pass

class Notification(ClonixTableBase):
    __tablename__="Notifications"

    notification_id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)

    target_type: Mapped[NotificationTargetType] = mapped_column(nullable=False)
    target_id: Mapped[str] = mapped_column(String(50), nullable=True)

    severity: Mapped[NotificationSeverity] = mapped_column(nullable=False)
    notification_title: Mapped[str] = mapped_column(String(256))
    notification_metadata: Mapped[dict]

    timestamp: Mapped[datetime.datetime] = mapped_column(DateTime(True))

class Scope(ClonixTableBase):
    __tablename__="Scopes"

    scope_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    scope_name: Mapped[str] = mapped_column(String(256))

class Contact(ClonixTableBase):
    __tablename__="Contacts"

    contact_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128))
    email: Mapped[str] = mapped_column(String(128))
    phone: Mapped[str] = mapped_column(String(10), nullable=True)

class User(ClonixTableBase):
    __tablename__="Users"

    user_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    contact: Mapped[int] = mapped_column(ForeignKey("Contacts.contact_id"))

class UserScope(ClonixTableBase):
    __tablename__="UserScopes"

    user_id: Mapped[int] = mapped_column(ForeignKey("Users.user_id"), primary_key=True)
    scope_id: Mapped[int] = mapped_column(ForeignKey("Scopes.scope_id"), primary_key=True)

class AuditLog(ClonixTableBase):
    __tablename__="AuditLogs"

    log_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)

    user_id: Mapped[int] = mapped_column(ForeignKey("Users.user_id"))
    action: Mapped[str] = mapped_column(String(512))
    status: Mapped[AuditLogStatus]
    timestamp: Mapped[datetime.datetime] = mapped_column(DateTime(True))

class Unit(ClonixTableBase):
    __tablename__="Units"

    unit_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    unit_name: Mapped[str] = mapped_column(String(128))
    parent: Mapped[int] = mapped_column(ForeignKey("Units.unit_id"), nullable=True)
    manifest_id: Mapped[str] = mapped_column(String(128), nullable=True)
    administrator: Mapped[int] = mapped_column(ForeignKey("Users.user_id"))

class UserUnit(ClonixTableBase):
    __tablename__="UserUnits"

    user_id: Mapped[int] = mapped_column(ForeignKey("Users.user_id"), primary_key=True)
    unit_id: Mapped[int] = mapped_column(ForeignKey("Units.unit_id"), primary_key=True)

class Configuration(ClonixTableBase):
    __tablename__="Configurations"

    configuration_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    configuration_name: Mapped[str] = mapped_column(String(128))
    filepath: Mapped[str] = mapped_column(String(512))
    timestamp: Mapped[datetime.datetime] = mapped_column(DateTime(True))

class Image(ClonixTableBase):
    __tablename__="Images"

    image_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    image_name: Mapped[str] = mapped_column(String(128))
    image_type: Mapped[str]
    filepath: Mapped[str] = mapped_column(String(512))
    timestamp: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    pass

class Device(ClonixTableBase):
    __tablename__="Devices"

    device_id: Mapped[str] = mapped_column(String(36), primary_key=True, unique=True)
    device_hostname: Mapped[str] = mapped_column(String(128), unique=True)
    device_sn: Mapped[str] = mapped_column(String(256), unique=True)
    device_unit: Mapped[int] = mapped_column(ForeignKey("Units.unit_id"))

    provision_timestamp: Mapped[datetime.datetime] = mapped_column(DateTime(True))

class AutoProvision(ClonixTableBase):
    __tablename__="Autoprovision"

    serial_number: Mapped[str] = mapped_column(String(256), ForeignKey("Devices.device_sn"), primary_key=True)

class DeviceContact(ClonixTableBase):
    __tablename__="DeviceContacts"

    device_id: Mapped[str] = mapped_column(String(36), ForeignKey("Devices.device_id"), primary_key=True)
    contact_id: Mapped[int] = mapped_column(ForeignKey("Contacts.contact_id"), primary_key=True)

class DeviceLog(ClonixTableBase):
    __tablename__="DeviceLogs"

    log_id: Mapped[int] = mapped_column(BigInteger, autoincrement=True, primary_key=True)
    device_id: Mapped[str] = mapped_column(String(36), ForeignKey("Devices.device_id"), primary_key=True)

    source: Mapped[str] = mapped_column(String(128))
    message: Mapped[str] = mapped_column(String(512))
    timestamp: Mapped[datetime.datetime]

class DeviceKey(ClonixTableBase):
    __tablename__="DeviceKeys"

    key_id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    device_id: Mapped[str] = mapped_column(String(36), ForeignKey("Devices.device_id"), primary_key=True)

    value: Mapped[str] = mapped_column(String(256), unique=True)
    expiry: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    key_type: Mapped[KeyType]

