import json
import sqlite3
import time

import requests

from CLITable import Table
from utils import cstring


def calculate_query(question):
    url = "http://localhost:5050"

    payload = {'q': question}
    files = [('csv', open(
        'products.csv', 'rb'))]
    headers = {}

    response = requests.request(
        "POST", url, headers=headers, data=payload, files=files)

    decoded = response.text.encode('utf8')
    jsn = json.loads(decoded)

    params = jsn['params']
    query = jsn['sql']

    if len(params) == 0:
        return query

    new_query = ""
    for i in query:
        if i == "?":
            val = "'" + params.pop(0) + "'"
            new_query += val
        else:
            new_query += i
    return new_query

# ensures number between a certain range
def clamp(n, min, max):
    if n < min:
        return min
    elif n > max:
        return max
    else:
        return n

def print_sql_query(query):
    # execute the query
    db_pth = "/Common/University/Year 3/Final Year Project/git-repository/dataset.sqlite3"
    conn = sqlite3.connect(db_pth)
    c = conn.cursor()

    # execute query and handle any errors
    potential_errors = (sqlite3.Warning, sqlite3.Error, sqlite3.DatabaseError, sqlite3.IntegrityError,
                        sqlite3.ProgrammingError, sqlite3.OperationalError, sqlite3.NotSupportedError)
    try:
        query_obj = c.execute(query)
        column_names = [description[0]
                        for description in query_obj.description]
        query_result = list(query_obj)
        query_result.insert(0, column_names)
    except potential_errors:
        return

    if len(query_result) == 1:
        # red and bold
        print(cstring("Query returned nothing", fg="r", style="b"))
    else:
        for i in range(0, len(query_result)):
            query_result[i] = [str(w) for w in query_result[i]]
        num_columns = len(query_result[0])
        table = Table(query_result[:11], Table.column_width(num_columns), True)
        print(table)
        print(cstring("Note that only the first 10 rows are shown",
                      fg='c', style='b') + '\n')


if __name__ == "__main__":
    while True:
        ask_prompt = "Please ask a question: "
        question = input(cstring(ask_prompt, fg='b', style='b'))
        try:
            generated_query = calculate_query(question)
        except Exception:
            print(cstring("Failed to generate a query", fg='r', style='b') + "\n")
            continue

        result_prompt = "The caluclated query is: "
        print(cstring(result_prompt, fg='y', style='b') + generated_query)

        query_execution_prompt = "Executing the query returns"
        print(cstring(query_execution_prompt, fg='g', style='bu') + "\n")
        time.sleep(clamp(0.15*len(generated_query), 0, 3))

        print_sql_query(generated_query)
