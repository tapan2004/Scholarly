🎓 Student Result Management System

A secure and scalable Result Management System built with Python (Tkinter) for the GUI and MongoDB (PyMongo) as the backend database.
This system allows students to view results and administrators to manage results efficiently.

🚀 Features

🔒 Secure login system for administrators and students

📊 Add, update, and delete student results

🔍 Search functionality for quick result access

✅ Data validation to ensure clean and consistent inputs

⚡ Optimized MongoDB queries for faster performance

🎨 User-friendly Tkinter GUI

🛠️ Tech Stack

Python

Tkinter (Frontend GUI)

MongoDB (Database)

PyMongo (Database Connector)

📂 Project Structure
📁 Student-Result-Management-System
│-- main.py              # Entry point for the application
│-- db_connection.py     # MongoDB connection setup
│-- gui/                 # Tkinter GUI code
│-- utils/               # Helper functions (validation, etc.)
│-- requirements.txt     # Required dependencies
│-- README.md            # Project documentation

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/tapan2004/Scholarly.git
cd Scholarly/pratcing/SIH


Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows


Install dependencies

pip install -r requirements.txt


Set up MongoDB

Install and run MongoDB locally or use MongoDB Atlas.

Update your connection string in db_connection.py.

Run the application

python main.py


🧑‍💻 Future Improvements

✅ Export results to PDF/Excel

✅ Role-based access control (Admins vs Teachers vs Students)

✅ Cloud deployment with MongoDB Atlas

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.
