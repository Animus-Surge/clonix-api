-- CloNIX Schema
-- MySQL dialect

create table Notifications (
  notif_id bigint auto_increment primary key,

  target_type varchar(20) not null,
  target_id varchar(50) not null,
  severity varchar(20) not null,
  title varchar(100) not null,

  metadata json,
  emit_stamp datetime(6) not null,
  created_at timestamp default current_timestamp,

  index idx_target_emit (target_id, emit_stamp desc)
);

create table Scopes (
  scope_id integer auto_increment primary key,
  name varchar(256) not null
);
 
create table UserContact (
  contact_id integer auto_increment primary key,

  name varchar(512) not null,
  email varchar(512) not null,
  phone varchar(10)
);

create table Users (
  user_id integer auto_increment primary key,
  contact integer not null,

  constraint fk_user_contact foreign key (contact) references UserContact(contact_id)
);

create table UserScopes (
  scope_id integer not null,
  user_id integer not null,

  primary key (scope_id, user_id),
  constraint fk_us_scope foreign key (scope_id) references Scopes(scope_id),
  constraint fk_us_user foreign key (user_id) references Users(user_id)
);

create table AuditLogs (
  log_id bigint auto_increment primary key,

  user_id integer not null,
  action varchar(256) not null,
  status varchar(256) not null,
  stamp timestamp default current_timestamp,

  index idx_auditlog_creation (log_id, stamp desc),
  constraint fk_auditlog_user foreign key (user_id) references Users(user_id)
);

create table Units (
  unit_id integer auto_increment primary key,

  unit_name varchar(256) not null,
  parent integer,
  manifest_id varchar(256),
  assigned_admin integer not null

  constraint fk_unit_parent foreign key (parent) references Units(unit_id),
  constraint fk_unit_admin foreign key (assigned_admin) references Users(user_id)
);

create table UnitContacts (
  unit_id integer not null,
  contact_id integer not null,

  primary key (unit_id, contact_id),
  constraint pkfk_unc_unit foreign key (unit_id) references Units(unit_id),
  constraint pkfk_unc_user foreign key (contact_id) references Contacts(contact_id)
);

create table UserUnits (
  unit_id integer not null,
  user_id integer not null,

  primary key (unit_id, user_id),
  constraint pkfk_uu_unit foreign key (unit_id) references Units(unit_id),
  constraint pkfk_uu_user foreign key (user_id) references Users(user_id)
);

create table Devices (
  device_uuid binary(16) primary key,
  hostname varchar(32) unique not null,
  serial_number varchar(32) unique not null,
  provision_stamp timestamp not null default current_timestamp,
  last_check_in timestamp not null default current_timestamp,
  metrics_url varchar(256),
  unit integer not null,

  constraint fk_device_unit foreign key (unit) references Units(unit_id)
);

create table DeviceContacts (
  device_uuid binary(16) not null,
  contact_id integer not null,

  primary key(device_uuid, contact_id),
  constraint pkfk_dc_device foreign key (device_uuid) references Devices(device_uuid),
  constraint pkfk_dc_contact foreign key (contact_id) references Contacts(contact_id)
);

create table DeviceLogs (
  log_id bigint auto_increment primary key,

  device_uuid binary(16) not null,

  source varchar(100) not null,
  message varchar(255) not null,
  stamp timestamp default current_timestamp,

  index idx_log_creation (log_id, created_at desc),
  constraint fk_log_device foreign key (device_uuid) references Devices(device_uuid)
);

create table DeviceKeys (
  key_id integer not null,
  device_uuid integer not null,

  value varchar(128) unique not null,
  expiry timestamp not null,
  type varchar(256) not null,

  primary key (device_uuid, key_id),
  constraint fk_keys_device foreign key (device_uuid) references Devices(device_uuid)
);






