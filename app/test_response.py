from requests import get, post


# print(get('http://localhost:5000/api/jobs/1').json())
# print(get('http://localhost:5000/api/jobs/999').json())
# print(get('http://localhost:5000/api/jobs/q').json())
# print(get('http://localhost:5000/api/jobs').json())
data = {}
data['team_leader'] = 1,
data['job'] = 'BIG job',
data['work_size'] = 1000,
data['collaborators'] = 'a, b, c',
data['start_date'] = '12.09.2022',
data['end_date'] = '',
data['is_finished'] = ''

print(post('http://127.0.0.1:5000/api/jobs', data=data).json())