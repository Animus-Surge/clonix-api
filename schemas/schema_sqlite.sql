-- SQlite schema

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS Roles (
    RoleID INTEGER NOT NULL,
    RoleName TEXT NOT NULL,

    CONSTRAINT PK_Role PRIMARY KEY (RoleID)
);

CREATE TABLE IF NOT EXISTS Scopes (
    ScopeID INTEGER NOT NULL,
    ScopeName TEXT NOT NULL,
    ScopePermissionString TEXT NOT NULL,

    CONSTRAINT PK_Scope PRIMARY KEY (ScopeID)
);

CREATE TABLE IF NOT EXISTS RoleScopes (
    Role INTEGER NOT NULL,
    Scope INTEGER NOT NULL,

    CONSTRAINT PK_RoleScope PRIMARY KEY (Role, Scope),
    CONSTRAINT FK_RoleScope_Role FOREIGN KEY (Role) REFERENCES Roles(RoleID),
    CONSTRAINT FK_RoleScope_Scope FOREIGN KEY (Scope) REFERENCES Scopes(ScopeID)
);

CREATE TABLE IF NOT EXISTS Units (
    UnitID INTEGER NOT NULL,
    DepartmentName TEXT NOT NULL,
    PointOfContact TEXT,
    Parent INTEGER,

    CONSTRAINT PK_Unit PRIMARY KEY (UnitID),
    CONSTRAINT FK_Unit_Parent FOREIGN KEY (Parent) REFERENCES Units(UnitID)
);

CREATE TABLE IF NOT EXISTS Devices (
    SerialNumber TEXT NOT NULL,
    Hostname TEXT NOT NULL,
    Unit INTEGER NOT NULL,
    ProvisionDate TEXT NOT NULL,
    LastCheckIn TEXT NOT NULL,

    CONSTRAINT PK_Device PRIMARY KEY (SerialNumber),
    CONSTRAINT FK_Device_Unit FOREIGN KEY (Unit) REFERENCES Units(UnitID)
);

CREATE TABLE IF NOT EXISTS DeviceKeys (
    KeyID INTEGER NOT NULL,
    Device TEXT NOT NULL,
    Value TEXT NOT NULL,
    KeyType INTEGER NOT NULL,
    ExpiryDate TEXT,
    KeyComment TEXT,

    CONSTRAINT PK_Key PRIMARY KEY (KeyID),
    CONSTRAINT UQ_Key_Value UNIQUE (Value),
    CONSTRAINT FK_Key_Device FOREIGN KEY (Device) REFERENCES Devices(SerialNumber)
);
