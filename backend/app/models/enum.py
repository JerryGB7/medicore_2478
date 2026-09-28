from enum import Enum

class equipment_status(str, Enum):
    AVAILABLE = "Available",
    IN_USE = "In-Use",
    MAINTENANCE = "Maintenance",
    OFFLINE = "Offline"

class work_order_priority(str, Enum):
    LOW = "Low",
    MEDIUM = "Medium",
    CRITICAL = "Critical"

class work_order_status(str, Enum):
    PENDING = "Pending",
    IN_PROGRESS = "In-Progress",
    COMPLETED = "Completed",
    FAILED = "Failed"