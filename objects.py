# CloNIX API objects.py
# Common structures for data handling.

from typing import List, Union

import pydantic

# Hardware Representation Objects
class HardwareDiskReprObject(pydantic.BaseModel):
    vendor: str = "N/A"
    serial_number: str = "N/A"
    capacity_gb: float = 0.0

class HardwareNICReprObject(pydantic.BaseModel):
    interface_name: str = "N/A" # i.e. eno1, enp1s32p2, etc.
    ipv4_addr: str = "..."
    ipv6_addr: str = ":::::"
    mac_address: str = ":::::"

class HardwareCPUReprObject(pydantic.BaseModel):
    vendor: str = "N/A" # Intel, AMD
    model: str = "N/A" # Core 9 Ultra, i9-13900k, etc.
    freq_mhz: float = 0.0 # 2333.0
    cores: int = 0 # 8
    threads: int = 0 # 16

class HardwareGPUReprObject(pydantic.BaseModel):
    vendor: str = "N/A"
    model: str = "N/A"
    driver: str = "N/A"

class HardwareMemoryReprObject(pydantic.BaseModel):
    main_memory: float = 0.0
    swap_memory: float = 0.0

class ContactReprObject(pydantic.BaseModel):
    contact_id: int = 0
    name: str = ""
    email: str = ""
    phone: str = ""

class UserReprObject(pydantic.BaseModel):
    user_id: int = 0
    contact: dict = {}

class UnitReprObject(pydantic.BaseModel):
    unit_id: int = 0
    unit_name: str = ""
    parent_unit: dict | None = None
    manifest_id: str = ""
    admin: dict = {}

class DeviceReprObject(pydantic.BaseModel):
    # Database-stored attributes
    uuid: str = ""
    hostname: str = "" # Contains the domain suffix, so if the hostname stored is 'some-hostname', this field returns 'some-hostname.<suffix>'. i.e. 'some-hostname.example.adp.net'
    serial_number: str = ""
    unit: dict = {}

    provision_timestamp: str = "" # THIS IS NOT DEVICE CREATION DATE. This is when clonix starts receiving information from the actual device.
    checkin_timestamp: str = "" # Puppet's last check in

    metrics_url: str = "" # Allows the frontend to automatically listen to the metrics websocket

    # Hardware information; gathered by Facter
    os_version: str = "" # Ubuntu 24.04.4, Rocky Linux 9.8

    cpus: List[HardwareCPUReprObject] = []
    gpus: List[HardwareGPUReprObject] = [] 
    networking: List[HardwareNICReprObject] = []
    memory: HardwareMemoryReprObject = HardwareMemoryReprObject()
    disks: List[HardwareDiskReprObject] = []
    

# Response Objects
class ErrorResponseObject(pydantic.BaseModel):
    error_code: int = 0
    message: str = ""

class DeviceListResponseObject(pydantic.BaseModel):
    count: int = 0
    devices: List[DeviceReprObject] = []

