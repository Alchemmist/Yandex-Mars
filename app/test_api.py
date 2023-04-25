from requests import get, post, delete, put


# TEST 1
"""
print(get('http://localhost:5000/api/jobs/1').json())
print(get('http://localhost:5000/api/jobs/999').json())
print(get('http://localhost:5000/api/jobs/q').json())
print(get('http://localhost:5000/api/jobs').json())
"""

# TEST 2
"""
data = {}
data['team_leader'] = 1,
data['job'] = 'BIG job',
data['work_size'] = 1000,
data['collaborators'] = 'a, b, c',
data['start_date'] = '12.09.2022',
data['end_date'] = '',
data['is_finished'] = ''

print(post('http://127.0.0.1:5000/api/jobs', data=data).json())
"""

# TEST 3
"""
print(delete('http://localhost:5000/api/jobs/999').json())

print(delete('http://localhost:5000/api/jobs/1').json())
print(get("http://localhost:5000/api/jobs").json())
"""

# TEST 4
print(
        put(
            "http://127.0.0.1:5000/api/jobs/1", 
            json={"team_leader": 1, 
                   "job": "this so good job", 
                   "work_size": 3, 
                   "collaborators": 1, 
                   "start_date": "12.03.2023" ,
                   "end_date": "08.04.2023", 
                   "is_finished": False, 
                   "user": 2}
            ).json()
      )
"""
print(get("http://127.0.0.1:5000/api/jobs").json())
"""
