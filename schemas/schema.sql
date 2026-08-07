-- CloNIX Schema
-- MySQL dialect

-- 
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

create table Logs (
  log_id bigint auto_increment primary key,

  system_uuid binary(16) not null,

  source_service varchar(100) not null,
  message varchar(255) not null,
  created_at timestamp default current_timestamp,

  index idx_log_creation (log_id, created_at desc)
);


create table Units (
  unit_id integer primary key,

  unit_name varchar(256) not null
);
create table Users (
  user_id integer primary key
);

create table AuditLogs (
  log_id bigint auto_increment primary key,
  
  user_id integer not null,


  constraint fk_audit_user foreign key user_id references (Users.user_id)  
);

create table Devices (
  -- Generated at provision time; STAYS WITH THE SYSTEM.
  device_uuid binary(16) primary key,
  
  -- Information given to the API, or set in the UI.
  hostname varchar(32) unique not null,
  serial_number varchar(32) unique not null,

  -- Handled by api calls
  provision_stamp timestamp not null default current_timestamp,
  last_check_in timestamp not null default current_timestamp,

  -- Websocket URI for metrics; e.g. ws://clonix/api/websocket/<uuid>
  metrics_uri varchar(256),

  -- Management
  unit integer not null,
  contact integer,

  constraint fk_contact_user foreign key contact references (Users.user_id),
  constraint fk_device_unit foreign key unit references (Units.unit_id)
);
