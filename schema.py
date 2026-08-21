"""
Database schema definition
"""

from sqlalchemy import JSON, DateTime, BigInteger, ForeignKey, MetaData, Table, Column, Integer, String, func

# Metadata object
metadata_obj = MetaData()

# Table decl

notification = Table("Notifications", metadata_obj,
                     Column("notif_id", BigInteger, autoincrement=True, primary_key=True),
                     
                     # Target information
Column("target_type", String(20), nullable=False),
                     Column("target_id", String(50), nullable=False),
                     
                     # Notification information
                     Column("severity", String(20), nullable=False),
                     Column("title", String(128), nullable=False),
                     Column("metadata", JSON, nullable=False),

                     # Timestamps
                     Column("emit_stamp", DateTime(True), nullable=False),
                     Column("create_stamp", DateTime(True), nullable=False))

scope = Table("Scopes", metadata_obj,
              Column("scope_id", Integer, autoincrement=True, primary_key=True),
              Column("name", String(256), nullable=False))

user_contact = Table("Contacts", metadata_obj,
                     Column("contact_id", Integer, autoincrement=True, primary_key=True),
                     Column("name", String(512), nullable=False),
                     Column("email", String(512), nullable=False),
                     Column("phone", String(10), nullable=True))

user = Table("Users", metadata_obj,
             Column("user_id", Integer, autoincrement=True, primary_key=True),
             Column("contact", Integer, ForeignKey("Contacts.contact_id"), nullable=False))

user_scope = Table("UserScopes", metadata_obj,
                   Column("scope_id", Integer, ForeignKey("Scopes.scope_id"), primary_key=True),
                   Column("user_id", Integer, ForeignKey("Users.user_id"), primary_key=True))

audit_log = Table("AuditLogs", metadata_obj,
                  Column("log_id", BigInteger, autoincrement=True, primary_key=True),

                  Column("user_id", Integer, ForeignKey("Users.user_id"), nullable=False),
                  Column("action", String(256), nullable=False),
                  Column("status", String(256), nullable=False),
                  Column("stamp", DateTime(True), nullable=False))

unit = Table("Units", metadata_obj,
             Column("unit_id", Integer, autoincrement=True, primary_key=True),
             Column("unit_name", String(256)),
             Column("parent", Integer, ForeignKey("Units.unit_id"), nullable=True),
             Column("manifest_id", String(256), nullable=True),
             Column("admin", Integer, ForeignKey("Users.user_id")))

unit_contact = Table("UnitContacts", metadata_obj,
                     Column("unit_id", Integer, ForeignKey("Units.unit_id"), primary_key=True),
                     Column("contact_id", Integer, ForeignKey("Contacts.contact_id"), primary_key=True))

user_unit = Table("UserUnits", metadata_obj,
                  Column("user_id", Integer, ForeignKey("Users.user_id"), primary_key=True),
                  Column("unit_id", Integer, ForeignKey("Units.unit_id"), primary_key=True))

device = Table("Devices", metadata_obj,
               Column("device_uuid", String(32), primary_key=True),
               Column("hostname", String(256), unique=True),
               Column("serial_number", String(32), unique=True),
               Column("unit", Integer, ForeignKey("Units.unit_id")),

               Column("provision_stamp", DateTime(True), server_default=func.now()),
               Column("checkin_stamp", DateTime(True), server_default=func.now()),

               Column("metrics_url", String(256), nullable=True))

device_contact = Table("DeviceContacts", metadata_obj,
                       Column("device_uuid", String(32), ForeignKey("Devices.device_uuid"), primary_key=True),
                       Column("contact_id", Integer, ForeignKey("Contacts.contact_id"), primary_key=True))

device_log = Table("DeviceLogs", metadata_obj,
                   Column("log_id", BigInteger, autoincrement=True, primary_key=True),
                   Column("device_uuid", String(32), ForeignKey("Devices.device_uuid"), primary_key=True),

                   Column("source", String(100)),
                   Column("message", String(256)),
                   Column("stamp", DateTime(True), server_default=func.now()))

device_key = Table("DeviceKeys", metadata_obj,
                   Column("key_id", Integer, autoincrement=True, primary_key=True),
                   Column("device_uuid", String(32), ForeignKey("Devices.device_uuid"), primary_key=True),

                   Column("value", String(128), unique=True),
                   Column("expiry", DateTime(True)),
                   Column("type", String(256)))

