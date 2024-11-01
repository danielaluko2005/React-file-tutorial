from app import db

class Friend(db.model):
    id=db.Column(db.Integer,primary_Key=True)
    name=db.Column(db.string(100),nullable=False)
    role=db.Column(db.string(100),nullable=False)
    description=db.Column(db.Text,nullable=False)
    gender=db.Column(db.string(10),nullable=False)
    img_url=db.Column(db.string(200),nullable=True)


    def to_json(self):
        return {
            "id":self.id,
            "name":self.name,
            "role":self.role,
            "description":self.description,
            "gender":self.gender,
            "imgUrl":self.img_url
        }