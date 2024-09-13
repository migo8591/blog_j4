from flask import Flask
from .public import public_bp
from .auth import auth_bp
from .admin import admin_bp
from extensions import db


def create_app(config):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
    app.config.from_object(config)  # Aplica la configuración
    app.register_blueprint(auth_bp)
    app.register_blueprint(public_bp)
    app.register_blueprint(admin_bp)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    # posts=[]
        
    # @app.route('/')
    # def index():
    #     return render_template("index.html", num_posts=len(posts), posts=posts)
    # @app.route("/p/<string:slug>")
    # def show_post(slug):
    #     # print(url_for("show_post", slug="leccion-1", preview=False))
    #     return render_template("post_view.html", slug_title=slug)
    # @app.route("/admin/post/", methods=["GET", "POST"], defaults={"post_id":None}) #crea el post
    # @app.route("/admin/post/<int:post_id>", methods=["GET","POST"])#modifica el post.
    # def post_form(post_id=None):
    #     form = PostForm()
    #     if form.validate_on_submit():
    #         title = form.title.data
    #         title_slug = form.title_slug.data
    #         content = form.content.data
            
    #         post = {"title": title, "title_slug": title_slug, "content": content}
    #         posts.append(post)  
    #         return redirect(url_for("index"))
    #     return render_template ("admin/post_form.html", form=form)
    # @app.route("/signup/", methods=["GET", "POST"])
    # def show_signup_form():
    #     form = SignupForm()    
        # if request.method == "POST":
            # name = request.form.get("name")
            # email = request.form.get("email")
            # password = request.form.get("password")
            # Guardar los datos en una base de datos
            # name = request.form["name"]
            # email = request.form["email"]
            # password = request.form["password"]
            # Luego comprobamos si se pasó por la URL el parámetro next. Este parámetro lo usaremos para redirigir al usuario a la página que se indica en el mismo. Si no se especifica, simplemente lo redirigimos a la página de inicio.
            # next = request.form.get("next", None)
        # if form.validate_on_submit():
        #     name = form.name.data
        #     email = form.email.data
        #     password = form.password.data
            
        #     next = request.args.get("next", None)
        #     print(f"Usuario:{name}, email {email} y password: {password}. Valor de next: {next}")
        #     if next:
        #         return redirect(next)
        #     return redirect(url_for("index"))
        # return render_template("signup_form.html", form=form)
    
    return app