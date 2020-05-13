# run the test dataset

from interactive import calculate_query
import sqlite3
import csv
import sys
import os

db_pth = "/Common/University/Year 3/Final Year Project/git-repository/dataset.sqlite3"
results_path = "test_results_sqlova_explicit.csv"

conn = sqlite3.connect(db_pth)
c = conn.cursor()

potential_errors = (sqlite3.Warning, sqlite3.Error, sqlite3.DatabaseError, sqlite3.IntegrityError,
                    sqlite3.ProgrammingError, sqlite3.OperationalError, sqlite3.NotSupportedError)

test_headers = ["question id", "author questions", "author sql", "generated sql", "correct prediction"]

csv_output = open(os.path.join(os.getcwd(), results_path), "w")

csv_writer = csv.writer(csv_output)
csv_writer.writerow(test_headers)

# getting questions from database
try:
    auth_result = c.execute("select * from author_questions_explicit")
    # format [id, english query, sqlquery]
    query_result = list(auth_result)
except potential_errors:
    sys.exit()

# converting english to sql query
for i in query_result:
    # attempt conversion
    try:
        result = calculate_query(i[1])
    except Exception:
        result = "failed"

    # remove semi colon
    result = result.strip(";")
    
    try:
        auth_result = c.execute(i[2])
        auth_result = list(auth_result)
        
        gen_result = c.execute(result)
        gen_result = list(gen_result)

        if auth_result == gen_result:
            validated = "True"
        else:
            validated = "False"
    except potential_errors as e:
        validated = "False"
        pass

    csv_writer.writerow([i[0], i[1], i[2], result, validated])
    print("Completed", i[0])
    

# excel formula for  counting true, false =COUNTIF(E2:E32, "True") and = COUNTIF(E2:E32, "False")
print("the results are stored in ", os.path.abspath(results_path))
