# 定义学员实体类
from typing import List


class Student:
    # 定义构造函数
    def __init__(self, stu_id: int, stu_name: str, stu_sex: str):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_sex = stu_sex

    # 定义魔法方法，相当于定义输出的格式,直接打印该类对象的话，就会按照下面的格式进行输出
    # 这个方法跟教程学习的
    def __repr__(self):
        return f"学号：{self.stu_id},姓名：{self.stu_name},性别：{self.stu_sex}"


# 定义学员管理类
class StudentManagement:
    def __init__(self, stu_list: List[Student]):
        if stu_list:
            self.student_list = stu_list
        else:
            self.student_list = []

    def _get_student_by_stu_id(self, stu_id: int):
        """
        私有get方法通过学员id获取学员信息
        :param stu_id:
        :return:
        """
        for stu in self.student_list:
            if stu_id == stu.stu_id:
                return stu

    def getStudent(self, stu_id: int):
        """
        获取学员信息
        :param stu_id:
        :return:
        """
        result = self._get_student_by_stu_id(stu_id)
        if result is None:
            print("查询失败，该学员不存在！")
        else:
            print("查询成功，该学员信息为：\n{}".format(result))

    def addStudent(self, stu: List[Student] or Student):
        """
        添加学员信息
        :param stu:学员信息， Student对象列表或者Student对象
        :return:
        """
        if type(stu) is list:
            add_list = []
            for s in stu:
                result = self._get_student_by_stu_id(s.stu_id)
                if result:
                    print("学员{}已存在，请核对学生信息".format(s.stu_id))
                else:
                    self.student_list.append(s)
                    add_list.append(s)
            if add_list:
                print("添加成功，添加的学员信息为：")
                for i in add_list:
                    print(i)
        else:
            result = self._get_student_by_stu_id(stu.stu_id)
            if result:
                print("学员{}已存在，请核对学生信息".format(stu.stu_id))
            else:
                self.student_list.append(stu)
                print("添加成功，添加的学员信息为：{}".format(stu))


if __name__ == '__main__':
    s1 = Student(1001, "张三", "男")
    s2 = Student(1002, "莉丝", "女")
    s3 = Student(1003, "王武", "男")
    # 实例化学员管理类
    student_list = StudentManagement([])
    print("---------添加多个学员----------")
    # 添加学员信息，传入学员对象列表
    student_list.addStudent([s1, s2, s3])
    s4 = Student(1004, "赵四", "男")
    s5 = Student(1005, "丽丽", "女")
    print("---------添加单个学员----------")
    student_list.addStudent(s4)
    print("-----------------------------")
    student_list.addStudent([s3, s5])
    print("---------查询学员信息----------")
    student_list.getStudent(1001)
    student_list.getStudent(1002)
    student_list.getStudent(1003)
    student_list.getStudent(1004)
    student_list.getStudent(1005)
