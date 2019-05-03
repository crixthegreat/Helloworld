#python code env
#-*-coding:utf-8-*-
#

class Human(object):

    def __init__(self, birthyear, sex, bloodtype):
        self.birthyear = birthyear
        self.sex = sex
        self.bloodtype = bloodtype

    @staticmethod
    def judge_sex(sex):
        if sex in ['male', 'female', 'any']:
            return True
        else:
            return False

    @classmethod
    def god_creat_person(cls, birthyear):
        return cls(birthyear, 'any', 'xxx')

if __name__ == '__main__':

    he = Human(1998, 'male', 'o')
    she = Human.god_creat_person('2999')
    me = Human(1981, 'male', 'ab')


    print(he.birthyear, he.sex, he.bloodtype)
    print(she.birthyear, she.sex, she.bloodtype)
    print(me.birthyear, me.sex, me.bloodtype)

    
    nobody = None
    
    s = input('please input the sex: ')
    
    if Human.judge_sex(s):
        nobody = Human(1000, s, 'a')
        print(nobody.birthyear, nobody.sex, nobody.bloodtype)
    else:
        print('there is nobody with the sex {}'.format(s))
