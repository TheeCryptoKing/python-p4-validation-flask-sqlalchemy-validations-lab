from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    
    @validates('name')
    def validate_name(self, key, name):
        # need a list to grab and compare db to with string
        names = db.session.query(Author.name).all()
        if not name:
            raise ValueError("what name is you using bigDawg?")
        # didnt clarify unique intially
        elif name in names:
            raise ValueError("names gotta be unique bigDawg!")
        return name
    
    @validates('phone_number')
    def validate_phone_numbers(self, key, phone_number):
        # only need length dont need to verify if exisits 
        if len(phone_number) != 10:
            raise ValueError("numbers need to be less then 10 bigDawg")
        return phone_number 

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('title')
    def validate_title(self, key, title):
        # need a list of title to decide if in it 
        # In python substring is a sequence of characters within another string, substring is asliced or split string
        clickbait = ["Won't Believe", "Secret", "Top", "Guess"]
        if not any(substring in title for substring in clickbait):
            raise ValueError("No clickbait found")
        return title
    
    # @validates('title')
    # def validate_title(self, key, title):
    #     clickbait = ["Won't Believe", "Secret", "Top", "Guess"]
    #     if not any(substring in title for substring in clickbait):
    #         raise ValueError("No clickbait found")
    #     return title
    
    @validates('content')
    def validate_content(self, key, string):
        if len(string) <= 250:
            raise ValueError('Woah speed that roll up') 
        return string  
    
    @validates('summary')
    def validate_summary(self, key, string):
        if len(string) >= 250:
            raise ValueError('Woah speed that roll up') 
        return string  
    
    #Better way
    #     @validates('content', 'summary')
    # def validate_length(self, key, string):
    #     if(key == 'content'):
    #         if len(string) <= 250:
    #             raise  ValueError("Post content must be greater than or equal 250 characters long.")
    #     if(key == 'summary'):
    #         if len(string) >= 250:
    #             raise ValueError("Post summary must be less than or equal to 250 characters long.")
    #     return string
    
    @validates('category')
    def validate_category(self, key, string):
        if string != 'Fiction' and string != 'Non-Fiction':
            raise ValueError('This a fiction store only')
        return string

    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
    
    
