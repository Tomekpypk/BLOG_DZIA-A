from flask import render_template, request, redirect, url_for
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm

@app.route("/")
def index():
    # Zmieniłem ten fragment kodu na zapytanie, które pobiera wszystkie wpisy
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc()).all()
    return render_template("homepage.html", all_posts=all_posts)

@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
@app.route("/new-post/", methods=["GET", "POST"])
def edit_or_create_entry(entry_id=None):
    entry = Entry.query.get(entry_id) if entry_id else None
    form = EntryForm(obj=entry)
    errors = None
    if request.method == 'POST':
        if form.validate_on_submit():
            if entry:
                form.populate_obj(entry)
            else:
                entry = Entry(
                    title=form.title.data,
                    body=form.body.data,
                    is_published=form.is_published.data
                )
                db.session.add(entry)
            db.session.commit()  # Dodane zatwierdzenie sesji
            return redirect(url_for('index'))  # Przekierowanie na stronę główną po dodaniu/edycji wpisu
        else:
            errors = form.errors
    return render_template("entry_form.html", form=form, errors=errors)


'''from flask import render_template, request, redirect, url_for
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm

@app.route("/")
def index():
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc()).all()
    return render_template("homepage.html", all_posts=all_posts)

@app.route("/new-post/", methods=["GET", "POST"])
@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
def edit_or_create_entry(entry_id=None):
    entry = Entry.query.get(entry_id) if entry_id else None
    form = EntryForm(obj=entry)
    errors = None
    if request.method == 'POST':
        if form.validate_on_submit():
            if entry:
                form.populate_obj(entry)
            else:
                entry = Entry(
                    title=form.title.data,
                    body=form.body.data,
                    is_published=form.is_published.data
                )
                db.session.add(entry)
            db.session.commit()
            return redirect(url_for('index'))  # Przekierowanie na stronę główną po dodaniu/edycji wpisu
        else:
            errors = form.errors
    return render_template("entry_form.html", form=form, errors=errors)
'''


'''from flask import render_template, request, redirect, url_for
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm

@app.route("/")
def index():
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc()).all()
    return render_template("homepage.html", all_posts=all_posts)

@app.route("/new-post/", methods=["GET", "POST"])
def create_entry():
    form = EntryForm()
    errors = None
    if request.method == 'POST':
        if form.validate_on_submit():
            entry = Entry(
                title=form.title.data,
                body=form.body.data,
                is_published=form.is_published.data
            )
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('index'))  # Przekierowanie na stronę główną po dodaniu wpisu
        else:
            errors = form.errors
    return render_template("entry_form.html", form=form, errors=errors)

@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
    entry = Entry.query.get_or_404(entry_id)
    form = EntryForm(obj=entry)
    errors = None
    if request.method == 'POST':
        if form.validate_on_submit():
            form.populate_obj(entry)
            db.session.commit()
            return redirect(url_for('index'))  # Przekierowanie na stronę główną po edycji wpisu
        else:
            errors = form.errors
    return render_template("entry_form.html", form=form, errors=errors)
'''



'''from flask import render_template
from blog import app
from blog.models import Entry
from blog.forms import EntryForm

@app.route("/")
def index():
      all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
      return render_template("homepage.html", all_posts=all_posts)

@app.route("/new-post/", methods=["GET", "POST"])
def create_entry():
   form = EntryForm()
   errors = None
   if request.method == 'POST':
       if form.validate_on_submit():
           entry = Entry(
               title=form.title.data,
               body=form.body.data,
               is_published=form.is_published.data
           )
           db.session.add(entry)
           db.session.commit()
       else:
           errors = form.errors
   return render_template("entry_form.html", form=form, errors=errors)

@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
   entry = Entry.query.filter_by(id=entry_id).first_or_404()
   form = EntryForm(obj=entry)
   errors = None
   if request.method == 'POST':
       if form.validate_on_submit():
           form.populate_obj(entry)
           db.session.commit()
       else:
           errors = form.errors
   return render_template("entry_form.html", form=form, errors=errors)
'''



############################################

'''from flask import render_template, request, redirect, url_for
from blog import app
from blog.models import Entry,db
#from blog.forms import EntryForm

@app.route("/")
def index():
    #all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.pub_date.desc())
    return "Hellow"
@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
@app.route("/new-post/", methods=["GET", "POST"])
def edit_or_create_entry(entry_id=None):
    entry = Entry.query.get(entry_id) if entry_id else None
    #form = EntryForm(obj=entry)
    errors = None
    if request.method == 'POST':
        if form.validate_on_submit():
            if entry:
                #form.populate_obj(entry)
                print("form")
            else:
               #entry = Entry(
                    title=form.title.data,
                    body=form.body.data is_published=form.is_published.data)
                db.session.add(entry)#
            print("form")
            #db.session.commit()
            return redirect(url_for('homepage'))  # Przekierowanie na stronę główną po dodaniu/edycji wpisu
        else:
            errors = "form.errors"
    return "testf"#render_template("entry_form.html", form=form, errors=errors)
'''
'''
from flask import render_template, request, redirect, url_for
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm

@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
@app.route("/new-post/", methods=["GET", "POST"])
def edit_or_create_entry(entry_id=None):
    entry = Entry.query.get(entry_id) if entry_id else None
    form = EntryForm(obj=entry)
    errors = None
    if request.method == 'POST':
        if form.validate_on_submit():
            if entry:
                form.populate_obj(entry)
            else:
                entry = Entry(
                    title=form.title.data,
                    body=form.body.data,
                    is_published=form.is_published.data)
                db.session.add(entry)
            db.session.commit()
            return redirect(url_for('homepage'))  # Przekierowanie na stronę główną po dodaniu/edycji wpisu
        else:
            errors = form.errors
    return render_template("entry_form.html", form=form, errors=errors)
'''

'''from flask import render_template, request, redirect, url_for
from blog.models import Entry, db
from blog import app  # Importujemy instancję aplikacji Flask

@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
@app.route("/new-post/", methods=["GET", "POST"])
def edit_or_create_entry(entry_id=None):
    entry = Entry.query.get(entry_id) if entry_id else None
    from blog.forms import EntryForm  # Importujemy tutaj, aby uniknąć cyklicznego importu
    form = EntryForm(obj=entry)
    errors = None
    if request.method == 'POST':
        if form.validate_on_submit():
            if entry:
                form.populate_obj(entry)
            else:
                entry = Entry(
                    title=form.title.data,
                    body=form.body.data,
                    is_published=form.is_published.data)
                db.session.add(entry)
            db.session.commit()
            return redirect(url_for('index'))  # Przekierowanie na stronę główną po dodaniu/edycji wpisu
        else:
            errors = form.errors
    return render_template("entry_form.html", form=form, errors=errors)'''

'''from flask import render_template, request, redirect, url_for
from blog import app
from blog.models import Entry, db
from blog.forms import EntryForm

@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
@app.route("/new-post/", methods=["GET", "POST"])
def edit_or_create_entry(entry_id=None):
    entry = Entry.query.get(entry_id) if entry_id else None
    form = EntryForm(obj=entry)
    errors = None
    if request.method == 'POST':
        if form.validate_on_submit():
            if entry:
                form.populate_obj(entry)
            else:
                entry = Entry(
                    title=form.title.data,
                    body=form.body.data,
                    is_published=form.is_published.data
                )
                db.session.add(entry)
            db.session.commit()
            return redirect(url_for('homepage'))  # Przekierowanie na stronę główną po dodaniu/edycji wpisu
        else:
            errors = form.errors
    return render_template("entry_form.html", form=form, errors=errors)'''