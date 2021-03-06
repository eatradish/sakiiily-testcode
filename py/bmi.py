def bmi(s):
    print('GET /bmi')
    lst = s.split()
    lst = person(lst[0], lst[1]).convert()
    bmi = bmi_object(lst[0], lst[1]).calc_bmi()
    return bmi

class person:
    weight = height = 0
    def __init__(self, arg_1, arg_2):
        self.arg_1 = arg_1
        self.arg_2 = arg_2

    def convert(self):
        for i in [self.arg_1, self.arg_2]:
            if 'kg' in i:
                weight = i
            elif 'jin' in i:
                weight = i
            elif 'cm' in i:
                height = i
            elif 'm' in i and 'c' not in i:
                height = i
            else:
                pass
        return [weight, height]

class bmi_object:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calc_bmi(self):
        if 'cm' in self.height:
            self.height = float(self.height.replace('cm', '')) / 100
        if 'jin' in self.weight:
            self.weight = float(self.weight.replace('jin', '')) / 2
        if type(self.weight) is str:
            self.weight = float(self.weight.replace("kg", ""))
        if type(self.height) is str:
            self.height = float(self.height.replace("m", ""))
    return "%.1f" % (self.weight / self.height ** 2)


if __name__ =='__main__':
    print(bmi('170cm 50kg'))
