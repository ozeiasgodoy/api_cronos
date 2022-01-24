from data import alchemy

class Blogs(alchemy.Model):
    __tablename__ = 'blog'

    id = alchemy.Column(alchemy.Integer, primary_key = True)
    titulo = alchemy.Column(alchemy.String(80))
    conteudo = alchemy.Column(alchemy.String(600))


def __init__(self, titulo, conteudo):
    self.titulo = titulo
    self.conteudo = conteudo

    def json(self):
            return {'id':self.id,
                    'titulo':self.titulo,
                    'conteudo':self.conteudo
                    }

    def save_to_db(self):
            alchemy.session.add(self)
            alchemy.session.commit()

    @classmethod
    def find_by_name(cls, titulo):
        return cls.query.filter_by(titulo=titulo).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def delete_from_db(self):
        alchemy.session.delete(self)
        alchemy.session.commit()

    def update(self):
        alchemy.session.commit()
