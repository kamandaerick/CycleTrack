# **CycleTrack: Bicycle Rental System**

**Deployed Site**: CycleTrack - Rent Your Ride

**Project Blog Article**: CycleTrack: A Journey into Building a Bicycle Rental System  (https://bloglink.com)

**Author**: Erick Kamanda (https://www.linkedin.com/in/erick-kamanda/)

---

## **Introduction**

CycleTrack is a web-based bicycle rental application designed to simplify the process of renting and managing bicycles for both users and administrators. Inspired by the growing demand for eco-friendly transportation options, the platform enables users to rent bicycles on an hourly basis while allowing administrators to track bicycle availability, user activity, and rental durations. The goal of CycleTrack is to provide an intuitive and efficient experience for both users and admins, making it easy to rent and return bicycles while ensuring accurate billing and seamless management.

This project was developed using **Python Flask** for the backend, **SQLAlchemy** for database operations, and **HTML/CSS** (along with Bootstrap) for the frontend. Key features include user registration, bicycle rental and return logic, real-time availability updates, and automated billing based on rental duration.

---

## **Installation**

Follow the steps below to install and set up CycleTrack on your local machine:

### **Requirements**
- Python 3.x
- Flask
- SQLAlchemy
- A virtual environment manager like `venv`
- MySQL or SQLite (depending on your setup)

### **Instructions**
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kamandaerick/CycleTrack.git
   cd CycleTrack
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For Linux/macOS
   # OR
   venv\Scripts\activate      # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Database**:
   - Create the database:
     ```sql
     CREATE DATABASE bicycle_rental;
     ```
   - Update your database configuration in `config.py` (MySQL or SQLite).

5. **Migrate the Database**:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Run the Application**:
   ```bash
   flask run
   ```

7. **Access the App**:
   Open your browser and navigate to `http://localhost:5000` to start using CycleTrack.

---

## **Usage**

Once the application is up and running, here’s how to interact with it:

### **For Users:**
- **Registration/Login**: Sign up and log in using the user dashboard.
- **Rent a Bicycle**: Choose from available bicycles and rent one by specifying the desired rental start time.
- **Return a Bicycle**: When done, return the bicycle using the "Return" button. The system will automatically calculate the rental duration and the amount due.
- **View Rental History**: See all past rentals along with start times, return times, and rental statuses.

### **For Administrators:**
- **Manage Bicycles**: View available and rented bicycles, update statuses, and track rentals.
- **View User Activity**: Check rental history for all users, monitor overdue rentals, and handle returns.

---

## **Contributing**

Contributions to CycleTrack are welcome! Whether you find bugs, want to request new features, or contribute to the codebase, you can follow the steps below:

1. **Fork the Project**
2. **Create a New Branch** (`git checkout -b feature-branch`)
3. **Commit Your Changes** (`git commit -m 'Add new feature'`)
4. **Push to the Branch** (`git push origin feature-branch`)
5. **Open a Pull Request**


---

## **Contact**

For more information or inquiries, feel free to reach out:

- **Email**: kaanthony00@gmail.com
- **LinkedIn**: Erick Kamanda (https://www.linkedin.com/in/erick-kamanda/)
