class StudentCard:
    school_name = 'Python 大学'
    def __init__(self, id, name):
        self.id = id
        self.name = name

a = StudentCard(1234, '鈴木太郎')
b = StudentCard(1235, '佐藤花子')
print(a.id, a.name)
print(a.school_name)
print(StudentCard.school_name)

