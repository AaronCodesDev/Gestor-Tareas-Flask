from sqlalchemy import Column, Integer, String, Boolean, DateTime
import db
from datetime import datetime

class Tarea(db.Base):
    __tablename__ = 'tarea'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False)
    hecha = Column(Boolean)
    categoria = Column(String)
    fecha_limite = Column(DateTime, nullable=False)  # Cambiado a DateTime

    def __init__(self, contenido, hecha, categoria=None, fecha_limite=None):
        self.contenido = contenido
        self.hecha = hecha
        self.categoria = categoria
        self.fecha_limite = fecha_limite

    def __str__(self):
        return 'Tarea {}: {} {} guardada en {} con fecha límite {}'.format(
            self.id, self.contenido, self.hecha, self.categoria, self.fecha_limite
        )
