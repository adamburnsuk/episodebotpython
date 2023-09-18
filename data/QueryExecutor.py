import pymysql.cursors

class QueryExecutor:
    def __init__(self):
        # Assuming local host as of now. Adjust as required.
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='example',
                                          db='wordpress',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor)
    
    def get_db_info(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            print(version)
    
    def get_users(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT u.id, u.user_email FROM wp_users u")
            for row in cursor:
                print(f"{row['id']}: {row['user_email']}")
    
    # More functions...

    def close(self):
        self.connection.close()

# Usage:
executor = QueryExecutor()
executor.get_db_info()
executor.get_users()
executor.close()
