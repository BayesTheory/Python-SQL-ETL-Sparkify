import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    conn = psycopg2.connect("host=localhost dbname=testedb user=postgres password=rian")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    conn.close()

    conn = psycopg2.connect("host=localhost dbname=testedb user=postgres password=rian")
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
