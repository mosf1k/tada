from django.db import connection


def get_available_letters(field_name, db_table):
    qn = connection.ops.quote_name
    sql = "SELECT DISTINCT UPPER(SUBSTR(%s, 1, 1)) as letter FROM %s" % (qn(field_name), qn(db_table))
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall() or ()
    return [row[0] for row in sorted(rows)]