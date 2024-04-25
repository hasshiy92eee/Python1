class BodyCondition:
    def __init__(self, arg_weight, arg_height):
        self.weight = arg_weight
        self.height = arg_height


    def bmi_calc(self):
        m_height = self.height / 100
        bmi = self.weight / m_height / m_height
        print(bmi)

# クラスの外でインスタンスを作成してメソッドを呼び出すs
bc = BodyCondition(90, 197)
bc.bmi_calc()
