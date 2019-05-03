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

    def judge_super(self):
        if self.birthyear < 2000 and self.sex == 'male':
            return True
        else:
            return False

class Superman(Human):

    def __init__(self,birthyear, sex, bloodtype, name, skill):

        super().__init__(birthyear, sex, bloodtype)
        self.skill = skill
        self.name = name

    def cast(self):
        print(self.name + ' cast skill: ' + self.skill)

    def judge_super(self):

        if super().judge_super():
            print(self.name + ' is a super man and ' , end = ' ')
            self.cast()
        else:
            print('no, ' + self.name + ' is not a true hero')

            
if __name__ == '__main__':

    he = Human(1998, 'male', 'o')
    she = Human.god_creat_person(2999)
    me = Human(1981, 'male', 'ab')
    nobody = None
    
    s = input('please input the sex: ')
    
    if Human.judge_sex(s):
        nobody = Human(1000, s, 'a')
        print(nobody.birthyear, nobody.sex, nobody.bloodtype)
    else:
        print('there is nobody with the sex {}'.format(s))


    onehero = Superman(1999, 'male', 'XX', 'Batman', 'GreatMuscle')
    otherhero = Superman(1998, 'male', 'AB', 'heroine', 'TimeStop')

    print(he.birthyear, he.sex, he.bloodtype, end = ' ')
    if he.judge_super():
        print('he is a superman')
    else:
        print('he is not a superman')

    print(she.birthyear, she.sex, she.bloodtype, end = ' ')
    if she.judge_super():
        print('she is a superman')
    else:
        print('she is not a superman')

    print(me.birthyear, me.sex, me.bloodtype, end = ' ')
    if me.judge_super():
        print('me is a superman')
    else:
        print('me is not a superman')
    
    onehero.judge_super()
    otherhero.judge_super()
    
