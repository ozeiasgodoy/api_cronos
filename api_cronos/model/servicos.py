from data import alchemy

class Servico(alchemy.Model):
    __tablename__ = 'servico'

    id = alchemy.Column(alchemy.Integer, primary_key = True)
    nome = alchemy.Column(alchemy.String(80))
    caminho_imagem = alchemy.Column(alchemy.String(500))
    descricao = alchemy.Column(alchemy.String(500))

    def __init__(self, nome, caminho_imagem, descricao):
        self.nome = nome
        self.caminho_imagem = caminho_imagem
        self.descricao = descricao


    def json(self):
        return {'id':self.id,
                'nome':self.nome,
                'caminho_imagem':self.caminho_imagem,
                'descricao':self.descricao
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
