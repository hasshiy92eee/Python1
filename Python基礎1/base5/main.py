#関数を作ろう！(JavaScriptやPHPのfunctionの様なもの)
def fruits ():
    print('apple')
fruits()

def test(text):
    language = 80
    Math = 70
    total = language + Math
    if language >= 70 and Math >= 70:
        print("合格")
    else:
        print("不合格")

test("Some text")

def question_text(text):
    text_q = text + '?'
    return text_q

result_text = question_text("apple")
print(result_text)

def qustion_Math_text(text1,text2):
    return_text1 = text1 + '?'
    return_text2 = text2 + '!'
    return return_text1, return_text2
r1,r2 = qustion_Math_text('programming', 'game')
print(r1)
print(r2)
