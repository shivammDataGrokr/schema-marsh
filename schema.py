from marshmallow import Schema, fields, post_load

class Book:
    def __init__(self, name, author, genre, description):
        self.name = name
        self.author = author
        self.genre = genre
        self.description =  description
    def __repr__(self):
        return f'{self.name} {self.author} {self.genre} {self.description}'

class BookSchema(Schema):
    name = fields.String()
    author = fields.String()
    genre = fields.String()
    description = fields.String()

    #using decorator post-load to deserialize anything that gets loaded into the schema
    @post_load
    def create_book(self, data, **kwargs):
        return Book(**data)

input_data = {}

input_data['name'] = input('Name of the book please! ')
input_data['author'] = input('And Author too! ')
input_data['genre'] = input('What about the genre! ')
input_data['description'] = input('Give it a description! ')

schema = BookSchema()
book = schema.load(input_data)

#person = Person(name=input_data['name'], age=input_data['age'])

#print(person)

result = schema.dump(book)

print(result)