from flask import Blueprint, render_template, request,flash, jsonify
from .models import Note
from . import db 
from werkzeug.utils import html
from flask_login import login_required,current_user
import json
views = Blueprint('views', __name__)

@views.route('/note', methods = ['GET', 'POST'])
@login_required
def note():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category = 'error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note Added!', category='success' )
    return render_template('note.html', user = current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/graphs', methods = ['GET', 'POST'])
def graph():
    graph = json.loads(request.data)
    
