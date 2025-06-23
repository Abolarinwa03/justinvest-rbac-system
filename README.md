# 🏦 justInvest - Role-Based Access Control System

A comprehensive Role-Based Access Control (RBAC) system designed for financial services, featuring secure authentication, time-based restrictions, and hierarchical permission management.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Security](https://img.shields.io/badge/Security-SHA--512-green.svg)
![Testing](https://img.shields.io/badge/Testing-Unit%20Tests-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Project Overview

This system implements enterprise-grade access control for a financial investment platform called **justInvest**. It demonstrates advanced cybersecurity principles, secure coding practices, and real-world application of authentication and authorization mechanisms.

### 🔑 Key Features

- **🔐 Secure Authentication**: SHA-512 password hashing with salt
- **👥 Role-Based Access Control**: 5 distinct user roles with specific permissions
- **⏰ Time-Based Restrictions**: Working hours enforcement for Tellers (9 AM - 5 PM)
- **🛡️ Password Security**: Complex validation with common password exclusions
- **🧪 Comprehensive Testing**: Full unit test coverage
- **📱 User-Friendly Interface**: Interactive login and registration system

## 🏗️ System Architecture

### User Roles & Permissions

| Role | Permissions | Special Restrictions |
|------|-------------|---------------------|
| **Clients** | • View account balance • View investment portfolio • View financial advisor contact | None |
| **Premium Clients** | • All Client permissions • Modify investment portfolio • View financial planner contact | None |
| **Financial Advisors** | • View client accounts • Modify client portfolios • Access private consumer instruments | None |
| **Financial Planners** | • All Advisor permissions • Access money market instruments | None |
| **Tellers** | • View client accounts • View client portfolios | **Time-restricted**: 9 AM - 5 PM only |

### 🔒 Security Features

- **Password Requirements**:
  - 8-12 characters length
  - At least 1 uppercase letter
  - At least 1 lowercase letter  
  - At least 1 digit
  - At least 1 special character (!@#$%?*.)
  - Cannot contain username
  - Blocked common/weak passwords

- **Secure Storage**:
  - SHA-512 hashing algorithm
  - Unique salt per password
  - No plaintext password storage

## 📁 Project Structure

\`\`\`
justinvest-rbac-system/
├── main.py                    # Main application driver
├── problem1c.py              # Core RBAC implementation
├── problem2.py               # Authentication & password validation
├── problem3.py               # User registration system
├── problem4.py               # Login system
├── justInvest.py             # Main user interface
├── problem1test.py           # Unit tests
├── passwd.txt                # User database (hashed passwords)
├── passwd_exclusions.txt     # Common password blacklist
└── README.md                 # Project documentation
\`\`\`

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses Python standard library)

### Installation & Usage

1. **Clone the repository**
   \`\`\`bash
   git clone https://github.com/Abolarinwa03/justinvest-rbac-system.git
   cd justinvest-rbac-system
   \`\`\`

2. **Run the application**
   \`\`\`bash
   python justInvest.py
   \`\`\`

3. **Run tests**
   \`\`\`bash
   python problem1test.py
   \`\`\`

### 💻 Demo Usage

\`\`\`
=== Welcome to justInvest ===
1. Login
2. Signup

Enter your choice (1 for Login, 2 for Signup): 1

=== User Login ===
Enter your username: bola
Enter your password: Abdul@123

Login successful!
Username: bola
Role: Clients
Available permissions:
    - view account balance
    - view investment portfolio
    - view financial advisor contact details
\`\`\`

## 🧪 Testing

The project includes comprehensive unit tests covering:

- ✅ Role permission validation
- ✅ Time-based access control
- ✅ Password security requirements
- ✅ User authentication flows
- ✅ RBAC system functionality

Run tests with: `python problem1test.py`

## 🔧 Technical Implementation

### Core Classes

#### `RoleBasedAccessControl`
- Manages roles and permissions
- Implements time-based restrictions
- Provides permission display functionality

#### `Authentication System`
- Secure password hashing with SHA-512
- Salt generation for enhanced security
- Password complexity validation
- User credential verification

### 🛡️ Security Measures

1. **Password Hashing**: Uses SHA-512 with unique salts
2. **Input Validation**: Comprehensive password requirements
3. **Access Control**: Role-based permission enforcement
4. **Time Restrictions**: Working hours validation for sensitive roles
5. **Common Password Prevention**: Blacklist of weak passwords

## 📊 Code Quality

- **Modular Design**: Separation of concerns across multiple files
- **Clean Architecture**: Well-organized class structure
- **Error Handling**: Comprehensive validation and error messages
- **Documentation**: Clear docstrings and comments
- **Testing**: Unit tests with good coverage

## 🎓 Learning Outcomes

This project demonstrates proficiency in:

- Cybersecurity Fundamentals: Authentication, authorization, secure storage
- Software Design Patterns: RBAC implementation, modular architecture
- Python Programming: Advanced features, standard library usage
- Testing Methodologies: Unit testing, test-driven development
- System Security: Password policies, access control mechanisms

## 🏫 Academic Context

Course: Network and Software Security 
Assignment: RBAC Security System Implementation  
Focus Areas: Cybersecurity, Software Engineering, System Design

## 📈 Future Enhancements

Potential improvements for production use:
- Database integration (PostgreSQL/MySQL)
- Web interface with Flask/Django
- Multi-factor authentication
- Audit logging and monitoring
- API endpoints for system integration
- Docker containerization

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

This is an academic project, but feedback and suggestions are welcome! Feel free to:
- Report issues
- Suggest improvements
- Share feedback on code structure

## 📞 Contact
Developer: Abolarinwa Elegbede
Email: belegbede2003@gmail.com  
LinkedIn: www.linkedin.com/in/abolarinwa-elegbede-62984a276
GitHub: [@Abolarinwa03](https://github.com/Abolarinwa03)

---

