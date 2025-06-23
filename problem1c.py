from datetime import datetime, time

class RoleBasedAccessControl:
    def __init__(self):
        self._roles = []
        self._permissions = {}
    
    def list_roles(self) -> list:
        """Retrieve a list of all roles."""
        return self._roles        

    def add_role(self, role: str) -> None:
        """Add a new role if it doesn't already exist."""
        if role not in self._roles:
            self._roles.append(role)
            self._permissions[role] = set()
            
    def assign_permission(self, role: str, permission: str) -> None:
        """Assign a permission to a specific role."""
        if role in self._roles:
            self._permissions[role].add(permission)

    def display_permissions(self, role: str) -> None:
        """Display the permissions of a role, considering special conditions."""
        if role in self._roles:
            if role == "Teller" and not self._is_within_work_hours():
                print(
                    "Access denied: It is outside the working hours (09:00 - 17:00)."
                )
            else:
                print("Available permissions:")
                for permission in self._permissions[role]:
                    print(f"\t- {permission}")

    def _is_within_work_hours(self) -> bool:
        """Check if the current time is within the allowed working hours."""
        now = datetime.now().time()
        start, end = time(9, 0), time(17, 0)
        return start <= now <= end
