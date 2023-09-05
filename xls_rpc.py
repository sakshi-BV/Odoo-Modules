import xmlrpc.client


data_url = 'http://localhost:8069'
database = 'sakshi_sahu'
user = 'admin'
password = '7d04365e95bd6d303e36de7b71fee90d77812518'

data_model = xmlrpc.client.ServerProxy(f'{data_url}/xmlrpc/2/object')
common_auth = xmlrpc.client.ServerProxy(f'{data_url}/xmlrpc/2/common')
uid = common_auth.authenticate(database, user, password, {})
# print(data_model,"fffffff",common_auth)

# searching_student = input("Give me your  Enrollment no.")
search_student_record = data_model.execute_kw(
    database, uid, password, 'student.table', 'create',
    [{'student_name':'ashish','standard':12,'age':12,'phone_number':'7566641565'}])

search_student_recordp = data_model.execute_kw(
    database, uid, password, 'student.table', 'read',
    [[search_student_record]], {'fields': []})

print(search_student_recordp)
