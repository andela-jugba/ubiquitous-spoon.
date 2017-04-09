from . import main
from flask import render_template, url_for, redirect, g, flash, session
from ..models import Category, Book
from forms import SearchForm

@main.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    if form.validate_on_submit():
        search_value = form.name.data
        books = Book.findByName(search_value)
        session['books'] = [book.name for book in books]
        form.name.data = ''
        if len(session.get('books')) == 0:
            flash('No records found!')
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form, matches=session.get('books'))
    
@main.route('/second', methods=['GET'])
def second():
    return render_template('index.html', form=SearchForm())
