import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs

from datetime import datetime


blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


# Получение всех работ
@blueprint.route('/api/jobs', methods=['GET'])
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict()
                 for item in jobs]
        }
    )


# Получение одной работы
@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_jobs_by_id(job_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs':
                job.to_dict()
        }
    )


# Добавление работы
@blueprint.route('/api/jobs', methods=['POST'])
def create_jobs():
    if not request.json:
        return jsonify({'error': 'Empty request'})

    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators', 'start_date',
                  'end_date', 'is_finished', 'user']):
        return jsonify({'error': 'Bad request'})\

    db_sess = db_session.create_session()

    job = Jobs(
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        start_date=request.json['start_date'],
        end_date=request.json['end_date'],
        is_finished=request.json['is_finished']
    )
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


# Удаление работы
@blueprint.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    db_sess.delete(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})


# Редактирование работы
@blueprint.route('/api/jobs/<int:job_id>', methods=['PUT'])
def edit_jobs(job_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})

    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators', 'start_date',
                  'end_date', 'is_finished', 'user']):
        return jsonify({'error': 'Bad request'})

    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(job_id)
    print(job, '🎈🎈🎈🎈')
    job.team_leader=request.json['team_leader'],
    job.job=request.json['job'],
    job.work_size=request.json['work_size'],
    job.collaborators=request.json['collaborators'],
    job.start_date=request.json['start_date'],
    job.end_date=request.json['end_date'],
    job.is_finished=request.json['is_finished']

    db_sess.merge(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})
