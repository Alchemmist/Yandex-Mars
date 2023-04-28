from requests import get, post, delete, put


# TEST 1 --------------------------------
"""
print(get('http://localhost:5000/api/jobs/1').json())
print(get('http://localhost:5000/api/jobs/999').json())
print(get('http://localhost:5000/api/jobs/q').json())
print(get('http://localhost:5000/api/jobs').json())
"""

# TEST 2 --------------------------------
"""
# коректный запрос
print(post('http://127.0.0.1:5000/api/jobs', json={"team_leader": 1, 
                                                   "job": "BIG job", 
                                                   "work_size": 100, 
                                                   "collaborators": 'a, b, b', 
                                                   "start_date": "12.09.2022", 
                                                   "end_date": "12.10.2022", 
                                                   "id_finished": False}).json())
# некоректный запрос, не соотвествующие типы
print(post('http://127.0.0.1:5000/api/jobs', json={"team_leader": "asdfsadf", 
                                                   "job": True, 
                                                   "work_size": "sf", 
                                                   "collaborators": 'a, b, b', 
                                                   "start_date": "12.09.2022", 
                                                   "end_date": 23, 
                                                   "id_finished": False}).json())
# некоректный запрос, не переданн json
print(post('http://127.0.0.1:5000/api/jobs').json())

# некоректный запрос, не достаточно полей
print(post('http://127.0.0.1:5000/api/jobs', json={"team_leader": "asdfsadf", 
                                                   "work_size": "sf", 
                                                   "collaborators": 'a, b, b', 
                                                   "end_date": 23, 
                                                   "id_finished": False}).json())
print(get('http://localhost:5000/api/jobs').json())
"""

# TEST 3 --------------------------------
"""
print(delete('http://localhost:5000/api/jobs/999').json())

print(delete('http://localhost:5000/api/jobs/1').json())
print(get("http://localhost:5000/api/jobs").json())
"""

# TEST 4 --------------------------------
"""
# коректные запросы
print(put("http://127.0.0.1:5000/api/jobs/1", json={"id": 1,
                                                   "team_leader": 1, 
                                                   "job": "this so good job", 
                                                   "work_size": 3, 
                                                   "collaborators": 1, 
                                                   "start_date": "12.03.2023" ,
                                                   "end_date": "08.04.2023", 
                                                   "is_finished": False, 
                                                   "user": 2}).json())

# некроектные запросы
print(put("http://127.0.0.1:5000/api/jobs/1", json={"team_leader": 1, 
                                                   "work_size": 3, 
                                                   "collaborators": 1, 
                                                   "start_date": "12.03.2023" ,
                                                   "end_date": "08.04.2023", 
                                                   "user": 2}).json())

print(put("http://127.0.0.1:5000/api/jobs/1", json={"id": 999, 
                                                   "team_leader": "sdfa", 
                                                   "job": True, 
                                                   "work_size": 3, 
                                                   "collaborators": 1, 
                                                   "start_date": "12.03.2023" ,
                                                   "end_date": 134, 
                                                   "is_finished": False, 
                                                   "user": 2}).json())

print(get("http://127.0.0.1:5000/api/jobs").json())
"""

# TEST 5 --------------------------------
"""
print(get('http://localhost:5000/api/v2/users').json())
print(get('http://localhost:5000/api/v2/users/1').json())
print(post('http://localhost:5000/api/v2/users', json={'surname': 'a',
                                                       'name': 'a',
                                                       'age': 1,
                                                       'position': 'a',
                                                       'speciality': 'a',
                                                       'address': 'a',
                                                       'email': 'a',
                                                       'hashed_password': 'a'}).json())
print(delete('http://localhost:5000/api/v2/users/1').json())

print(get('http://localhost:5000/api/v2/users/999').json())
print(delete('http://localhost:5000/api/v2/users/999').json())
"""

# TEST 6 --------------------------------
"""
print(get('http://localhost:5000/api/v2/jobs').json())
print(get('http://localhost:5000/api/v2/jobs/1').json())
print(post('http://localhost:5000/api/v2/jobs', json={"team_leader": 1, 
                                                       "job": "BIG job", 
                                                       "work_size": 100, 
                                                       "collaborators": 'a, b, b', 
                                                       "start_date": "12.09.2022", 
                                                       "end_date": "12.10.2022", 
                                                       "is_finished": True, }).json())
print(delete('http://localhost:5000/api/v2/jobs/1').json())

print(get('http://localhost:5000/api/v2/jobs/999').json())
print(delete('http://localhost:5000/api/v2/jobs/999').json())
"""
