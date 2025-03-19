import mysql.connector

def connect_database():
    try:
        return mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Bebop1216!",
            database = "gym_db"
    )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def add_member(id, name, age):
    connection = connect_database()
    if connection is None:
        return
    cursor = connection.cursor()
    query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
    values = (id, name, age)
    try:
        cursor.execute(query, values)
        connection.commit()
        print("A new member has been added to the database!")
    except mysql.connector.Error as err:
        print(f"An error popped up! {err}")
    finally:
        cursor.close()
        connection.close()

def add_workout_session(member_id, session_date, duration_minutes, calories_burned):
    connection = connect_database()
    if connection is None:
        return
    cursor = connection.cursor()
    query = """INSERT INTO WorkoutSessions
               (member_id,
                session_date,
                duration_minutes,
                calories_burned)
                VALUES(%s, %s, %s, %s)"""
    values = (member_id, session_date, duration_minutes, calories_burned)
    try:
        cursor.execute(query, values)
        connection.commit()
        print("Newly added info has been submitted and accepted!")
    except mysql.connector.Error as err:
        print(f"An error popped up! {err}")
    finally:
        cursor.close()
        connection.close()

def update_member_age(member_id, new_age):
    connection = connect_database()
    if connection is None:
        return
    cursor = connection.cursor()
    query = "UPDATE Members SET age = %s WHERE id = %s"
    values = (new_age, member_id)
    try:
        cursor.execute(query, values)
        connection.commit()
        if cursor.rowcount == 0:
            print("Member doesn't exist in the database. Retry!")
        else:
            print("Member was found!")
    except mysql.connector.Error as err:
        print(f"An error popped up! {err}")
    finally:
        cursor.close()
        connection.close()

def delete_workout_session(session_id):
    connection = connect_database()
    if connection is None:
        return
    cursor = connection.cursor()
    query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
    values = (session_id,)
    try:
        cursor.execute(query, values)
        connection.commit()
        if cursor.rowcount == 0:
            print("Workout session doesn't exist within database! Retry!")
        else:
            print("Workout session deleted successfuly!")
    except mysql.connector.Error as err:
        print(f"An error popped up! {err}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    #add_member(10, "Adam McAdams", 29)
    #add_workout_session(10, "2024-03-02", 32, 50)
    #update_member_age(4, 22)
    delete_workout_session(59)