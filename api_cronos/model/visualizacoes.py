from data import alchemy

class Visualizacoes(alchemy.Model):
    __tablename__ = 'visualizacao'

    id = alchemy.Column(alchemy.Integer, primary_key = True)
    pagina = alchemy.Column(alchemy.String(150))
    visualizacoes = alchemy.Column(alchemy.Integer)


    def __init__(self, pagina, visualizacoes):
        self.nome = nome
        self.pagina = pagina
        self.visualizacoes = visualizacoes


    def json(self):
        return {'id':self.id,
                'pagina':self.pagina,
                'visualizacoes':self.visualizacoes
                }

    def save_to_db(self):
        alchemy.session.add(self)
        alchemy.session.commit()

    @classmethod
    def find_by_name(cls, pagina):
        return cls.query.filter_by(pagina=pagina).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def delete_from_db(self):
        alchemy.session.delete(self)
        alchemy.session.commit()

    def update(self):
        alchemy.session.commit()
