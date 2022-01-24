from data import alchemy

class Integrante(alchemy.Model):
    __tablename__ = 'integrante'

    id = alchemy.Column(alchemy.Integer, primary_key = True)
    nome = alchemy.Column(alchemy.String(150))
    email = alchemy.Column(alchemy.String(150))
    departamento = alchemy.Column(alchemy.String(200))


    def __init__(self, nome, email, departamento):
        self.nome = nome
        self.email = email
        self.departamento = departamento


    def json(self):
        return {'id':self.id,
                'nome':self.nome,
                'email':self.email,
                'departamento':self.departamento
                }

    def save_to_db(self):
        alchemy.session.add(self)
        alchemy.session.commit()

    @classmethod
    def find_by_name(cls, nome):
        return cls.query.filter_by(nome=nome).first()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def delete_from_db(self):
        alchemy.session.delete(self)
        alchemy.session.commit()

    def update(self):
        alchemy.session.commit()
