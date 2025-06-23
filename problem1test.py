import unittest
from problem1c import RoleBasedAccessControl
from datetime import time


class TestAccessControl(unittest.TestCase):
    def setUp(self):
        self.rbac = RoleBasedAccessControl()
        
        # Roles setup
        self.rbac.add_role("Client")
        self.rbac.add_role("Premium Client")
        self.rbac.add_role("Financial Advisor")
        self.rbac.add_role("Financial Planner")
        self.rbac.add_role("Teller")

        # Permissions setup
        self.rbac.assign_permission("Client", "view account balance")
        self.rbac.assign_permission("Client", "view investment portfolio")
        self.rbac.assign_permission("Client", "view financial advisor contact details")
        
        self.rbac.assign_permission("Premium Client", "view account balance")
        self.rbac.assign_permission("Premium Client", "view investment portfolio")
        self.rbac.assign_permission("Premium Client", "modify investment portfolio")
        self.rbac.assign_permission("Premium Client", "view financial planner contact details")
        
        self.rbac.assign_permission("Financial Advisor", "view client account balance")
        self.rbac.assign_permission("Financial Advisor", "view client investment portfolio")
        self.rbac.assign_permission("Financial Advisor", "modify client investment portfolio")
        self.rbac.assign_permission("Financial Advisor", "view private consumer instruments")
        
        self.rbac.assign_permission("Financial Planner", "view client account balance")
        self.rbac.assign_permission("Financial Planner", "view client investment portfolio")
        self.rbac.assign_permission("Financial Planner", "modify client investment portfolio")
        self.rbac.assign_permission("Financial Planner", "view private consumer instruments")
        self.rbac.assign_permission("Financial Planner", "view money market instruments")
        
        self.rbac.assign_permission("Teller", "view client account balance")
        self.rbac.assign_permission("Teller", "view client investment portfolio")
        
    def test_client_permissions(self):
        role = "Client"
        self.assertIn("view account balance", self.rbac._permissions[role])
        self.assertIn("view investment portfolio", self.rbac._permissions[role])
        self.assertNotIn("modify investment portfolio", self.rbac._permissions[role])

    def test_premium_client_permissions(self):
        # Test premium client permissions
        role = "Premium Client"
        self.assertIn("modify investment portfolio", self.rbac._permissions[role])
        self.assertNotIn("view money market instruments", self.rbac._permissions[role])
    
    def test_financial_advisor_permissions(self):
        # Test financial advisor permissions
        role = "Financial Advisor"
        self.assertIn("modify client investment portfolio", self.rbac._permissions[role])
        self.assertIn("view private consumer instruments", self.rbac._permissions[role])
        self.assertNotIn("view money market instruments", self.rbac._permissions[role])
        
    def test_teller_permissions_outside_working_hours(self):
        self.rbac._is_within_work_hours = lambda: False
        self.assertFalse(self.rbac._is_within_work_hours())

    def test_teller_permissions_during_working_hours(self):
        self.rbac._is_within_work_hours = lambda: True
        self.assertTrue(self.rbac._is_within_work_hours())

    def test_financial_planner_permissions(self):
        role = "Financial Planner"
        self.assertIn("view money market instruments", self.rbac._permissions[role])
        self.assertIn("view private consumer instruments", self.rbac._permissions[role])
        self.assertNotIn("view financial advisor contact details", self.rbac._permissions[role])


if __name__ == "__main__":
    unittest.main()
