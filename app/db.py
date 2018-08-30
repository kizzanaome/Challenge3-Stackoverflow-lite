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
                    ans_id INTEGER PRIMARY KEY,
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

if __name__ == '__main__':
    db = Database()
    db.create_tables()




# class Login(Resource):
#     def post(self):
#         pass



#     def insert_ride_offers(self):
#         """Getting data from the URL body """
#         parser = reqparse.RequestParser()
#         parser.add_argument('name', type=str, required=True)
#         parser.add_argument('details', type=str, required=True)
#         parser.add_argument('price', type=str, required=True)
#         parser.add_argument('token', location='headers')
#         parser.add_argument('driver_name',type=str,required=True)
#         args = parser.parse_args()
#         """ check the token value if its available"""
#         if not args['token']:
#             return make_response(jsonify({"message": "Token is missing"}),
#                                  401)
#         """ implementing token decoding"""
#         decoded = decode_token(args['token'])
#         if decoded["status"] == "Failure":
#             return make_response(jsonify({"message": decoded["message"]}),
#                                  401)

#         offer_name = args['name']
#         offer_details = args['details']
#         price = args['price']
#         driver_name = args['driver_name']
#         """creating a ride offer cursor to 
#         check for already existing ride offer names."""
#         cur_select_ride_offers = con.cursor()
#         cur_select_ride_offers.execute(
#             "select name from rides where driver = '"+driver_name+"' and name='"+offer_name+"'")
#         while True:
#             row = cur_select_ride_offers.fetchone()
#             if row == None:
#                 break

#             if str(row[0]).strip() == str(offer_name).strip():
#                 print('db name : ' + str(row[0]) +
#                       '  url name : ' + str(offer_name).strip())
#                 return make_response(jsonify({"message": 'Sorry,this ride offer is already available.'}),
#                                      400)

#         cur = con.cursor()
#         cur.execute("INSERT INTO rides (name,details,price,driver)  VALUES('" +
#                     offer_name + "','"+offer_details+"','"+price+"','"+driver_name+"')")
#         con.commit()
#         return make_response(jsonify({'message': 'Ride offer created


    
  