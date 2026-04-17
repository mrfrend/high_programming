import pymysql


class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = self.connect()

    def connect(self):
        connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            cursorclass=pymysql.cursors.DictCursor,
        )

        return connection

    def cursor(self):
        return self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def get_companies(self):
        with self.cursor() as cur:
            cur.execute("SELECT * FROM companies")
            return cur.fetchall()

    def get_events_for_company(self, company_id):
        with self.cursor() as cur:
            cur.execute("SELECT * FROM events WHERE company_id = %s", (company_id,))
            return cur.fetchall()

    def get_services_for_event(self, event_id: int):
        with self.cursor() as cur:
            query = """
                SELECT services.* FROM event_services
                JOIN services ON event_services.service_id = services.id
                WHERE event_id = %s
            """
            cur.execute(query, [event_id])
            return cur.fetchall()

    def get_participant_with_phone(self, phone: str):
        with self.cursor() as cur:
            cur.execute(
                "SELECT * FROM participants WHERE phone LIKE %s", [f"%{phone}%"]
            )
            return cur.fetchone()

db = Database("localhost", "root", "", "high_events")
