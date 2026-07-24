-- CloNIX Schema

create table if not exists Roles (
  RoleID number not null,
  RoleName varchar not null,

  constraint PK_Role primary key (RoleID)
);

create table if not exists Scopes (
  ScopeID number not null,
  ScopeName varchar not null,
  ScopePermissionString varchar not null,

  constraint PK_Scope primary key (ScopeID)
);

create table if not exists RoleScopes (
  Role number not null,
  Scope number not null,

  constraint PK_RoleScope primary key (Role, Scope),
  constraint FK_RoleScope_Role foreign key (Role) references Roles(RoleID),
  constraint FK_RoleScope_Scope foreign key (Scope) references Scopes(ScopeID)
);

create table if not exists Units (
  UnitID number not null,
  DepartmentName varchar not null,
  PointOfContact varchar,
  Parent number,

  constraint FK_Unit_Parent foreign key (Parent) references Units(UnitID)
);

create table if not exists Devices (
  SerialNumber number not null,
  Hostname varchar not null,
  Unit number not null,
  ProvisionDate timestamp not null,
  LastCheckIn timestamp not null,

  constraint PK_Device primary key (SerialNumber),
  constraint FK_Device_Unit foreign key (Unit) references Units(UnitID)
);

create table if not exists DeviceKeys (
  KeyID number not null,
  Device number not null,
  Value varchar not null,
  KeyType number not null,
  ExpiryDate timestamp,
  KeyComment varchar,

  constraint PK_Key primary key (KeyID),
  constraint UQ_Key_Value unique (Value),
  constraint FK_Key_Device foreign key (Device) references Devices(SerialNumber)
);
