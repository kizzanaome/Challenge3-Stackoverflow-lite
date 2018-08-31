import psycopg2
class Database:
    def databaseconnections(self):
        try:
            self.connection = psycopg2.connect(
                "dbname ='stack_db' user ='postgres' password ='1460' port ='5433'"
            )
            return self.connection           
        except:
            print ("Cannot connect to database")
                   

    def create_tables(self):           
        """ create tables in the stack_db database"""
        commands = (
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                
                username VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                created_at TEXT NOT NULL DEFAULT TO_CHAR(CURRENT_TIMESTAMP,
                                                     'YYYYMM'),
                updated_at TEXT NOT NULL DEFAULT TO_CHAR(CURRENT_TIMESTAMP,
                                                     'YYYYMM')                
            )
            """,

            """ CREATE TABLE IF NOT EXISTS questions (
                    qstn_id SERIAL PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    qstn_title VARCHAR(255) NOT NULL,
                    description VARCHAR(255) NOT NULL,
                    question_date TEXT NOT NULL DEFAULT TO_CHAR(CURRENT_TIMESTAMP,
                                                     'YYYYMM'),
                    FOREIGN KEY (user_id) 
                        REFERENCES users(user_id) ON DELETE CASCADE                
                    )
            """,
            
            """
            CREATE TABLE IF NOT EXISTS answers (
                    ans_id SERIAL PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    qstn_id INTEGER NOT NULL,
                    ans_body TEXT NOT NULL,
                    most_correct BOOLEAN NOT NULL DEFAULT FALSE,
                    date TEXT NOT NULL DEFAULT TO_CHAR(CURRENT_TIMESTAMP,
                                                     'YYYYMM'),
                    FOREIGN KEY (user_id) 
                        REFERENCES users(user_id)
                        ON UPDATE CASCADE ON DELETE CASCADE,
                    FOREIGN KEY (qstn_id)
                        REFERENCES questions(qstn_id)
                        ON UPDATE CASCADE ON DELETE CASCADE                    
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS comments (
                    id INTEGER PRIMARY KEY,
                    ans_id INTEGER NOT NULL,
                    qstn_id INTEGER NOT NULL,
                    comment INTEGER NOT NULL,
                    date TEXT NOT NULL DEFAULT TO_CHAR(CURRENT_TIMESTAMP,
                                                     'YYYYMM'), 
                    FOREIGN KEY (qstn_id)
                        REFERENCES questions (qstn_id)
                        ON UPDATE CASCADE ON DELETE CASCADE,
                    FOREIGN KEY (ans_id)
                        REFERENCES answers (ans_id)
                        ON UPDATE CASCADE ON DELETE CASCADE
                    
            )
            """)
       
        try:
            connection = self.databaseconnections()
            cursor = connection.cursor()
            for comand in commands:
                cursor.execute(comand)
                print("tables created")
            cursor.close()
            connection.commit()           
        except (Exception, psycopg2.DatabaseError)as Error:
            print(Error)
        finally:
            connection = self.databaseconnections()
            connection.close()

    def delete_test_tables(self):
        connection = self.databaseconnections()
        cursor = connection.cursor()


        delete_queries = (
            """
            DROP TABLE IF EXISTS users CASCADE
            """,

            """
			DROP TABLE IF EXISTS questions CASCADE
						""",

            """
            DROP TABLE IF EXISTS answers CASCADE
            """,
            """
            DROP TABLE IF EXISTS comments CASCADE
            """
        )
        for query in delete_queries:
            cursor.execute(query)  

         
# if __name__ == '__main__':
#     db = Database()
#     db.create_tables()
    
  