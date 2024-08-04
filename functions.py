import psycopg2


# BE ADVISED, THIS CONNECT TO MY DATABASE, IN ORDER TO WORK YOU MUST CHANGE THE CONFIGURATIONS.
# BE ADVISED, THIS PROGRAM SAVES THE DATABASE IN A CSV FILE, CONFIGURE THE PATH IN ORDER FOR IT TO WORK.
# SEE LINES 45, 70, 94.

class DBConn:
    def __init__(self, host, dbname, user, password, port):
        self.conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
        self.conn.autocommit = True

    def get_cursor(self):
        return self.conn.cursor()
    
    def close(self):
        self.conn.close()
    
class DBJobs:
    def __init__(self, conn:DBConn, csv_file_path='Jobs/status_on_jobs.csv'):
        self.conn = conn
        self.csv_file_path = csv_file_path
    
    """
    Prints all jobs from the 'jobs' table.

    No parameters.
    """
    def print_jobs(self):
        cur = self.conn.get_cursor()
        cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

        cur.execute("SELECT * FROM jobs ORDER BY status, company;")

        jobs_rows = cur.fetchall()

        cur.close()
        return jobs_rows

    """
    Adds a new job to the 'jobs' table.

    Parameters:
        - company (str): The job company.
        - name (str): The job name.
        - status (str): The job status (Approved, Declined, Pending).

    No return value.
    """
    def add_job(self, company, name, status):
        cur = self.conn.get_cursor()
        cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

        sqlstr = "INSERT INTO jobs (job_uid, company, job_name, status) VALUES (uuid_generate_v4(), %s, %s, %s);"
        cur.execute(sqlstr, (company, name, status))
        with open(self.csv_file_path, 'w') as f:
            cur.copy_to(file=f, table='jobs', sep=',')

        cur.close()


    """
    Updates the status of a job in the 'jobs' table.

    Parameters:
        - id (str): The job UID.
        - stat (str): The new status (Approved, Declined, Pending).

    No return value.
    """
    def update_job(self, id, stat):
        cur = self.conn.get_cursor()
        cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')


        sqlstr2 = "UPDATE jobs SET status = %s WHERE job_uid = %s"
        cur.execute(sqlstr2, (stat, id))

        with open(self.csv_file_path, 'w') as f:
            cur.copy_to(file=f, table='jobs', sep=',')

        cur.close()


    """
    Deletes a job from the 'jobs' table.

    Parameters:
        - id (str): The job UID to delete.

    No return value.
    """
    def delete_job(self, id):
        cur = self.conn.get_cursor()
        cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')

        sqlstr2 = f"DELETE FROM jobs WHERE job_uid = '{id}'"
        cur.execute(sqlstr2)

        with open(self.csv_file_path, 'w') as f:
            cur.copy_to(file=f, table='jobs', sep=',')

        cur.close()
