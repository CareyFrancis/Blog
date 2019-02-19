from flask import render_template, request, redirect, url_for, abort
from . import main
from .forms import UpdateProfile, BlogForm
from ..models import User
from flask_login import login_required, current_user
from .. import db
# import markdown2


@main.route('/')
#@login_required
def index():
    title = 'CAREY-BLOG'

    #search_pitch = request.args.get('pitch_query')
    #pitches = Pitch.get_all_pitches()
    #categories = Category.get_categories()
    return render_template('index.html', title=title)


@main.route('/blog/new/', methods=['GET', 'POST'])
#@login_required
def new_blog():

    form = BlogForm()
    if category is None:
        abort(404)

    if form.validate_on_submit():
        blog = form.content.data
        new_blog = Blog(blog=blog)

        new_blog.save_blog()
        return redirect(url_for('main.index'))

    return render_template('blog.html', new_blog_form=form)



@main.route('/blog/comments/new/<int:id>', methods=['GET', 'POST'])
#@login_required
def new_comment(id):
    form = CommentsForm()
    vote_form = UpvoteForm()
    if form.validate_on_submit():
        new_comment = Comment(pitch_id=id, comment=form.comment.data,
                              username=current_user.username, votes=form.vote.data)
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    #title = f'{pitch_result.id} review'
    return render_template('comments.html', comment_form=form, vote_form=vote_form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
#@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = 'photos/{}'.format(filename)
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        return render_template('fourOwFour.html')

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/view/comment/<int:id>')
def view_comments(id):
    '''
    Function that returs  the comments belonging to a particular pitch
    '''
    comments = Comment.get_comments(id)
    return render_template('view_comments.html', comments=comments, id=id)

