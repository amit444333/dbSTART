import psycopg2


# BE ADVISED, THIS CONNECT TO MY DATABASE, IN ORDER TO WORK YOU MUST CHANGE THE CONFIGURATIONS.

"""
Prints all jobs from the 'jobs' table.

No parameters.
"""
def print_jobs():
    conn = psycopg2.connect(host="localhost", dbname="test", user="amit4", password="310795", port=5432)
    cur = conn.cursor()

    cur.execute("SELECT * FROM jobs ORDER BY status, company;")

    for row in cur.fetchall():
        print(row)

    conn.commit()
    cur.close()
    conn.close()


"""
Adds a new job to the 'jobs' table.

Parameters:
    - company (str): The job company.
    - name (str): The job name.
    - status (str): The job status (Approved, Declined, Pending).

No return value.
"""
def add_job():
    conn = psycopg2.connect(host="localhost", dbname="test", user="amit4", password="310795", port=5432)
    cur = conn.cursor()

    company = input('Please enter the job company: ')
    name = input('Please enter the job name: ')
    status = input('Please enter the job status (Approved, Declined, Pending): ')

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
def update_job():
    conn = psycopg2.connect(host="localhost", dbname="test", user="amit4", password="310795", port=5432)
    cur = conn.cursor()

    id = input('Please enter the job_uid: ')
    stat = input('Enter the status change (Approved, Declined, Pending): ')

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
def delete_job():
    conn = psycopg2.connect(host="localhost", dbname="test", user="amit4", password="310795", port=5432)
    cur = conn.cursor()

    id = input('Please enter the job_uid for the job to delete: ')

    sqlstr2 = f"DELETE FROM jobs WHERE job_uid = '{id}'"
    cur.execute(sqlstr2)

    with open('C:/Users/amit4/Desktop/Jobs/status_on_jobs.csv', 'w') as f:
        cur.copy_to(file=f, table='jobs', sep=',')

    conn.commit()
    cur.close()
    conn.close()
