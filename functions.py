import psycopg2


# BE ADVISED, THIS CONNECT TO MY DATABASE, IN ORDER TO WORK YOU MUST CHANGE THE CONFIGURATIONS.
# BE ADVISED, THIS PROGRAM SAVES THE DATABASE IN A CSV FILE, CONFIGURE THE PATH IN ORDER FOR IT TO WORK.
# SEE LINES 45, 70, 94.

"""
Prints all jobs from the 'jobs' table.

No parameters.
"""
def print_jobs():
    conn = psycopg2.connect(host="localhost", dbname="test", user="amit4", password="310795", port=5432)
    cur = conn.cursor()

    cur.execute("SELECT * FROM jobs ORDER BY status, company;")

    jobs_rows = cur.fetchall()

    conn.commit()
    cur.close()
    conn.close()
    return jobs_rows

"""
Adds a new job to the 'jobs' table.

Parameters:
    - company (str): The job company.
    - name (str): The job name.
    - status (str): The job status (Approved, Declined, Pending).

No return value.
"""
def add_job(company, name, status):


    conn = psycopg2.connect(host="localhost", dbname="test", user="amit4", password="310795", port=5432)
    cur = conn.cursor()


    sqlstr = "INSERT INTO jobs (job_uid, company, job_name, status) VALUES (uuid_generate_v4(), %s, %s, %s);"
    cur.execute(sqlstr, (company, name, status))
    with open('C:/Users/amit4/Desktop/Jobs/status_on_jobs.csv', 'w') as f:
        cur.copy_to(file=f, table='jobs', sep=',')

    conn.commit()
    cur.close()
    conn.close()


"""
Updates the status of a job in the 'jobs' table.

Parameters:
    - id (str): The job UID.
    - stat (str): The new status (Approved, Declined, Pending).

No return value.
"""
def update_job(id, stat):
    conn = psycopg2.connect(host="localhost", dbname="test", user="amit4", password="310795", port=5432)
    cur = conn.cursor()


    sqlstr2 = "UPDATE jobs SET status = %s WHERE job_uid = %s"
    cur.execute(sqlstr2, (stat, id))

    with open('C:/Users/amit4/Desktop/Jobs/status_on_jobs.csv', 'w') as f:
        cur.copy_to(file=f, table='jobs', sep=',')

    conn.commit()
    cur.close()
    conn.close()


"""
Deletes a job from the 'jobs' table.

Parameters:
    - id (str): The job UID to delete.

No return value.
"""
def delete_job(id):
    conn = psycopg2.connect(host="localhost", dbname="test", user="amit4", password="310795", port=5432)
    cur = conn.cursor()


    sqlstr2 = f"DELETE FROM jobs WHERE job_uid = '{id}'"
    cur.execute(sqlstr2)

    with open('C:/Users/amit4/Desktop/Jobs/status_on_jobs.csv', 'w') as f:
        cur.copy_to(file=f, table='jobs', sep=',')

    conn.commit()
    cur.close()
    conn.close()
