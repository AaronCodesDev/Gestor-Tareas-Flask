from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

app = Flask(__name__)

@app.route('/')
def home():
    todas_las_tareas = db.session.query(Tarea).all()
    return render_template('index.html', lista_de_tareas=todas_las_tareas)


@app.route('/crear-tarea', methods=['POST'])
def crear():
    tarea = Tarea(contenido=request.form['contenido_tarea'], hecha=False, categoria = request.form['contenido_categoria'])
    print('bg_'+request.form['contenido_categoria'])
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/tarea-hecha/<int:id>')
def hecha(id):
    tarea = db.session.query(Tarea).filter(Tarea.id == id).first()
    if tarea:
        tarea.hecha = not tarea.hecha
        db.session.commit()
    return redirect(url_for('home'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    tarea = db.session.query(Tarea).filter(Tarea.id == id).first()

    if tarea is None:
        return "Tarea no encontrada", 404

    if request.method == 'POST':
        nuevo_contenido = request.form.get('contenido_tarea')
        if not nuevo_contenido:
            return "El contenido de la tarea no puede estar vacío", 400

        tarea.contenido = nuevo_contenido
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('editar.html', tarea=tarea)

@app.route('/eliminar-tarea/<int:id>')
def eliminar(id):
    db.session.query(Tarea).filter(Tarea.id == id).delete()
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/eliminar-todas-tareas')
def eliminarTodas():
    db.session.query(Tarea).delete()
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    db.Base.metadata.create_all(bind=db.engine)
    app.run(debug=True)
