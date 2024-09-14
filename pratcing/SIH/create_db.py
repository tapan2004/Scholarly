from pymongo import MongoClient
from pymongo.errors import ConfigurationError, OperationFailure, NetworkTimeout

def create_collections():
    # MongoDB connection string
    connection_string = "mongodb+srv://sahapriyanshu88:ezyCplrNUtcKPuiH@cluster0.4qyhzir.mongodb.net/"

    # Connect to MongoDB
    try:
        client = MongoClient(connection_string)
        db = client["rms"]  # Database name
        print("Connected to MongoDB successfully.")
    except (ConfigurationError, NetworkTimeout) as ce:
        print(f"Error connecting to MongoDB: {ce}")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    try:
        # === Create and populate 'course' collection ===
        course_collection = db["course"]
        course_sample = {
            "name": "Computer Science",
            "duration": "4 Years",
            "charges": 20000,  # Changed to integer for consistency with numeric data types
            "description": "Undergraduate course in Computer Science"
        }
        
        # Insert sample data only if the collection is empty
        if course_collection.count_documents({}) == 0:
            course_collection.insert_one(course_sample)
            print("Sample data inserted into 'course' collection.")
        else:
            print("'Course' collection already contains data.")

        # === Create and populate 'student' collection ===
        student_collection = db["student"]
        student_sample = {
            "roll": 1157,  # Assuming roll number is numeric
            "name": "John Doe",
            "email": "john@example.com",
            "gender": "Male",
            "dob": "1998-05-14",
            "contact": "1234567890",
            "admission_date": "2021-09-01",  # Changed key for clarity
            "course": "Computer Science",  # Assumes course name is a string matching an entry in 'course' collection
            "state": "California",
            "city": "Los Angeles",
            "pin": "90001",
            "address": "123 Main St, Los Angeles, CA"
        }
        
        # Insert sample data only if the collection is empty
        if student_collection.count_documents({}) == 0:
            student_collection.insert_one(student_sample)
            print("Sample data inserted into 'student' collection.")
        else:
            print("'Student' collection already contains data.")

        # === Create and populate 'result' collection ===
        result_collection = db["results"]
        result_sample = {
            "roll": 1157,  # Roll number links to the student
            "course": "Computer Science",
            "marks_obtained": 450,  # Changed keys for clarity and consistency
            "full_marks": 500,
            "percentage": "90%"
        }
        
        # Insert sample data only if the collection is empty
        if result_collection.count_documents({}) == 0:
            result_collection.insert_one(result_sample)
            print("Sample data inserted into 'result' collection.")
        else:
            print("'Result' collection already contains data.")

    except OperationFailure as of:
        print(f"Operation failed: {of}")
    except Exception as e:
        print(f"Unexpected error during data insertion: {e}")

    finally:
        # Close the connection
        client.close()
        print("MongoDB connection closed.")

if __name__ == "__main__":
    create_collections()
