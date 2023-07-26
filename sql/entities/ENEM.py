from sql.configs.base import Base
from sqlalchemy import Column, Integer, Text, String

#Creating a tabble inside the database EnemAnwer, that are inside our server!
class EnemAnswers(Base):
    __tablename__ = "enem_answer"

    #criating the variables that may to be inside the tabble!
    id = Column(Integer, primary_key= True, autoincrement=True )
    title = Column(String, nullable= False)
    answer = Column(Text, nullable= False)

    #Modifing tha pattern of __repr__ of the class to show better the data!
    def __repr__(self):
        return f"ENEM Answer {self.id} - {self.title}"


#Repositorio que puxa a função para cada database
from sql.configs.connection import DataBase_ConnectionHandler

class EnemAnswers_Repository:
    #DELETING
    def delete(self, id):
        try:
            with DataBase_ConnectionHandler() as db:
                db.session.query(EnemAnswers).filter(EnemAnswers.id == id).delete()

                #Atualizar os IDs de todos os dados para ficar em um id sequencial
                records = db.session.query(EnemAnswers).order_by(EnemAnswers.id).all()

                for index, record in enumerate(records, start=1):
                    record.id = index
                
                db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise e

    #INSERTING
    def insert(self,title, answer):
        try:
            with DataBase_ConnectionHandler() as db:
                data_insert = EnemAnswers(title=title, answer=answer)
                db.session.add(data_insert)
                db.session.commit() #Não precisaria ter todos esses comits, só um no final ja resolve para subir a session!
        
        except Exception as e:
            db.session.rollback()
            raise e
            

    #UPDATING
    def update(self, id, answer):
        try:
            with DataBase_ConnectionHandler() as db:
                db.session.query(EnemAnswers).filter(EnemAnswers.id == id).update({ "answer": answer})
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

    #SELECTING to show the data
    def select(self):
        try:
            with DataBase_ConnectionHandler() as db:
                data = db.session.query(EnemAnswers).all()
                return data
        except Exception as e:
            db.session.rollback()
            raise e
        
    def select_question(self, id):
        try:
            with DataBase_ConnectionHandler() as db:
                data = db.session.query(EnemAnswers).filter(EnemAnswers.id == id).one()
                return data.answer
        except Exception as e:
            db.session.rollback()
            raise e
