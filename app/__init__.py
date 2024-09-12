from flask import Flask,url_for,render_template, request, redirect
from forms import SignupForm

def create_app(config):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    app.config.from_object(config)  # Aplica la configuración
    
    @app.route('/')
    def index():
        posts=["Migue", "Muñoz"]
        return render_template("index.html", num_posts=len(posts))
    @app.route("/p/<string:slug>")
    def show_post(slug):
        # print(url_for("show_post", slug="leccion-1", preview=False))
        return render_template("post_view.html", slug_title=slug)
    @app.route("/admin/post/") #crea el post
    @app.route("/admin/post/<int:post_id>")#modifica el post.
    def post_form(post_id=None):
        return render_template ("admin/post_form.html", post_id=post_id)
    @app.route("/signup/", methods=["GET", "POST"])
    def show_signup_form():
        form = SignupForm()    
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
        if form.validate_on_submit():
            name = form.name.data
            email = form.email.data
            password = form.password.data
            
            next = request.args.get("next", None)
            print(f"Usuario:{name}, email {email} y password: {password}. Valor de next: {next}")
            if next:
                return redirect(next)
            return redirect(url_for("index"))
        return render_template("signup_form.html", form=form)
    
    return app