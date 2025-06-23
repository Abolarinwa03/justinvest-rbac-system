from problem1c import RoleBasedAccessControl

class Main:
        def __init__(self):
                self.rbac = RoleBasedAccessControl()
                self.users = {
                    "Clients": ["Sasha Kim", "Emery Blake"],
                    "Premium Clients": ["Noor Abbasi", "Zuri Adebayo"],
                    "Financial Advisors": ["Mikael Chen", "Jordan Riley"],
                    "Financial Planners": ["Ellis Nakamura", "Harper Diaz"],
                    "Tellers": ["Alex Hayes", "Adair Patel"],
                }
                self.initialize_roles()
                self.assign_permissions()
        
        def initialize_roles(self):
                roles = ["Clients", "Premium Clients", "Financial Advisors",
                        "Financial Planners", "Tellers"]
                for permission in roles:
                        self.rbac.add_role(permission)
        
        def assign_permissions(self):
               # Client permissions
                client_permissions = ["view account balance",
                   "view investment portfolio",
                   "view financial advisor contact details",]
                for permission in client_permissions:
                        self.rbac.assign_permission("Clients", permission)
       
               # Premium Client permissions
                premium_permissions = client_permissions + ["modify investment portfolio", "view financial planner contact details",]
                for permission in premium_permissions:
                        self.rbac.assign_permission("Premium Clients", permission)
       
               # Financial Advisor permissions
                advisor_permissions = [
                   "view client account balance",
                   "view client investment portfolio",
                   "modify client investment portfolio",
                   "view private consumer instruments",
               ]
                for permission in advisor_permissions:
                        self.rbac.assign_permission("Financial Advisors", permission)
       
               # Financial Planner permissions
                planner_permissions = advisor_permissions + ["view money market instruments"]
                for permission in planner_permissions:
                        self.rbac.assign_permission("Financial Planners", permission)
       
               # Teller permissions
                teller_permissions = ["view client account balance", "view client investment portfolio"]
                for permission in teller_permissions:
                        self.rbac.assign_permission("Tellers", permission)
                        

        def display_user_permissions(self):
                for role, users in self.users.items():
                        print(f"\nRole: {role}")
                        for user in users:
                                print(f"User: {user}")
                        self.rbac.display_permissions(role)



if __name__ == "__main__":
        main = Main()
        main.display_user_permissions()