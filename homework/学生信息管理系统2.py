"""
项目简介
随着学校的规模变大，对应的学员回越来越多，相应的管理越来越难。 学员信息管理系统主要是对学员的各种信息进行管理，能够让学员的信息关系变得科学化、系统化和规范化。

知识点
实体类
成员变量属性
方法
集合
受众
中级测试工程师
作业内容
编写学员实体类 Student，对应成员变量包含：学号 id、姓名 name、性别 sex；

编写学员管理类 StudentManagement ，实现添加学员方法 addStudent()。

编写StudentManagement的main()方法进行学员信息的添加：

学号：1001,姓名：张三,性别：男。
学号：1002,姓名：莉丝,性别：女。
学号：1003,姓名：王武,性别：男。
编写学员管理类 StudentManagement ，实现删除学员方法 deleteStudent()，根据学员id 删除以下学员：

学号：1002,姓名：莉丝,性别：女。
示例效果
命令行输出打印效果如下：
添加成功，添加的学员信息为：
学号：1001,姓名：张三,性别：男
学号：1002,姓名：莉丝,性别：女
学号：1003,姓名：王武,性别：男
删除成功，删除的学员信息为：
学号：1001,姓名：张三,性别：男
学号：1003,姓名：王武,性别：男
"""
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

    def _get_all_student(self):
        """
        获取所有学员信息
        :return:
        """
        for stu in self.student_list:
            print(stu)

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

    def deleteStudent(self, stu_id:int):
        result = self._get_student_by_stu_id(stu_id)
        if result:
            self.student_list.remove(result)
            print("删除成功，删除的学员信息为：{}".format(result))
            print("删除后的学员信息为：")
            self._get_all_student()
        else:
            print("删除失败，请确认学员信息")

if __name__ == '__main__':
    s1 = Student(1001, "张三", "男")
    s2 = Student(1002, "莉丝", "女")
    s3 = Student(1003, "王武", "男")
    # 实例化学员管理类
    student_list = StudentManagement([])
    print("---------添加多个学员----------")
    # 添加学员信息，传入学员对象列表
    student_list.addStudent([s1, s2, s3])
    student_list.deleteStudent(1002)
