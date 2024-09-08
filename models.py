from sqlalchemy import Column, Integer, String, Boolean
import db

class Tarea(db.Base):
    __tablename__ = 'tarea'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False)
    hecha = Column(Boolean)
    categoria = Column(String)

    def __init__(self, contenido, hecha, categoria=None):
        self.contenido = contenido
        self.hecha = hecha
        self.categoria = categoria

    def __str__(self):
        return 'Tarea {}: {} {} guardada en {}'.format(self.id, self.contenido, self.hecha, self.categoria)
