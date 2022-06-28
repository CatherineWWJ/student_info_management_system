import os.path

filename = 'student.txt'
def main():
    while True:
        menu()
        choose = int(input('请输入您的选择：'))
        if choose in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choose == 0:
                aws = input('确定要退出系统吗？y/n\n')
                if aws == 'y' or aws == 'Y':
                    print('谢谢您的使用！ ')
                    break
                else:
                    continue
            elif choose == 1:
                insertStu()
            elif choose == 2:
                findStu()
            elif choose == 3:
                deleteStu()
            elif choose == 4:
                updateStu()
            elif choose == 5:
                sortStu()
            elif choose == 6:
                countStu()
            else:
                showStu()
        else:
            print('您的选择有误，请重新选择！')
            continue

def menu():
    print('='*23+'学生信息管理系统'+'='*20)
    print('-'*25+'功能菜单'+'-'*25)
    print('\t\t\t\t1.录入学生信息')
    print('\t\t\t\t2.查找学生信息')
    print('\t\t\t\t3.删除学生信息')
    print('\t\t\t\t4.修改学生信息')
    print('\t\t\t\t5.排序')
    print('\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t0.退出系统')

def insertStu():
    stuList = []
    while True:
        id = input('请输入学生ID:')
        name = input('请输入学生姓名：')
        if not id or not name:
            break
        try:
            english = int(input('请输入学生英语成绩：'))
            python = int(input('请输入学生python成绩：'))
            java = int(input('请输入学生英java成绩：'))
        except:
            print('输入无效！不是有效数据！')
            continue
        stu = {'id':id, 'name':name, 'english':english, 'python':python, 'java':java}
        stuList.append(stu)
        ans = input('是否继续添加学生信息？y/n\n ')
        if ans == 'y' or ans == 'Y':
            continue
        else:
            break
    save(stuList)
    print('学生信息录入完毕！')

def save(lst):
    stu_txt= open(filename, 'a', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def findStu():
    while True:
        idx = int(input('按ID查找请输入1，按姓名查找请输入2：'))
        if idx in [1, 2]:
            if idx == 1:
                find_id = input('请输入学生id：')
                if os.path.exists(filename):
                    with open(filename, 'r', encoding='utf-8') as rfile:
                        stu_old = rfile.readlines()
                        for item in stu_old:
                            d = dict(eval(item))
                            if d['id'] == find_id:
                                count = int(d['english']) + int(d['python']) + int(d['java'])
                                print('id\t\t姓名\t\t英语成绩\tpython成绩\tjava成绩\t总成绩\t\t')
                                print('{0}\t{1}\t\t{2}\t\t{3}\t\t\t{4}\t\t{5}\t\t'.format(d['id'],d['name'],d['english'],d['python'],d['java'],count))
                else:
                    return
            else:
                find_name = input('请输入学生姓名：')
                if os.path.exists(filename):
                    with open(filename, 'r', encoding='utf-8') as rfile:
                        stu_old = rfile.readlines()
                        for item in stu_old:
                            d = dict(eval(item))
                            if d['name'] == find_name:
                                count = int(d['english']) + int(d['python']) + int(d['java'])
                                print('id\t\t姓名\t\t英语成绩\tpython成绩\tjava成绩\t总成绩\t\t')
                                print('{0}\t{1}\t\t{2}\t\t{3}\t\t\t{4}\t\t{5}\t\t'.format(d['id'], d['name'],
                                                                                          d['english'], d['python'],
                                                                                          d['java'], count))
                else:
                    return
        else:
            print('您的输入有误！请重新输入！')
            continue
        ans = input('是否继续查询？y/n')
        if ans == 'y' or ans == 'Y':
            continue
        else:
            break

def deleteStu():
    while True:
        del_id = input('请输入要删除的学生ID：')
        if not id:
            break
        else:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    stuOld = file.readlines()
            else:
                stuOld = []
            flag = False # 标记是否删除
            if stuOld:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in stuOld:
                        d = dict(eval(item)) # 将字符串转换为字典
                        if d['id'] != del_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print('id为{0}的学生信息已被删除！'.format(del_id))
                    else:
                        print(f'没有找到id为{del_id}的学生信息')
            else:
                print('无学生信息！')
                break
            showStu() # 删完之后要重新显示所有学生信息
            ans = input('请问还要继续删除学生信息吗？y/n')
            if ans == 'y' or ans == 'Y':
                continue
            else:
                break

def updateStu():
    showStu()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            stu_old = rfile.readlines()
    else:
        return
    upd_id = input('请输入要修改的学生id：')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in stu_old:
            d = dict(eval(item))
            if d['id'] == upd_id:
                print('找到这名学生，可以修改他的相关信息了！')
                while True:
                    try:
                        d['name'] = input('请输入姓名：')
                        d['english'] = input('请输入英语成绩：')
                        d['python'] = input('请输入python成绩：')
                        d['java'] = input('请输入java成绩：')
                    except:
                        print('您的输入信息有误！')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功！')
            else:
                wfile.write(str(d)+'\n')
        ans = input('是否继续修改学生信息？y/n\n')
        if ans == 'y' or ans == 'Y':
            updateStu()

def sortStu():
    while True:
        showStu()
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as rfile:
                stu_old = rfile.readlines()
                stu_lst = []
                for item in stu_old:
                    d = dict(eval(item))
                    stu_lst.append(d)
            idx1 = int(input('请选择（0升序，1降序）：'))
            isRev = (idx1 == 1)
            if idx1 in [0, 1]:
                idx2 = int(input('请选择排序方式（1.按英语成绩排序 2.按python成绩排序 3.按java成绩排序 0.按总成绩排序）：'))
                if idx2 in [1, 2, 3, 0]:
                    if idx2 == 1:
                        stu_lst.sort(key=lambda x :int(x['english']),reverse=isRev)
                    elif idx2 == 2:
                        stu_lst.sort(key=lambda x :int(x['python']),reverse=isRev)
                    elif idx2 == 3:
                        stu_lst.sort(key=lambda x :int(x['java']),reverse=isRev)
                    else:
                        stu_lst.sort(key=lambda x :int(x['java'])+int(x['python'])+int(x['english']),reverse=isRev)
                    showNew(stu_lst)
                else:
                    print('排序方式输入有误！')
                    continue
            else:
                print('你的选择输入有误！')
                continue
        else:
            return
        ans = input('是否继续进行排序操作？y/n')
        if ans == 'y' or ans == 'Y':
            continue
        else:
            break



def countStu():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            stu_old = rfile.readlines()
            count = len(stu_old)
            print('一共有{0}名学生。'.format(count))
            return
    else:
        return

def showStu():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            stu_lst = rfile.readlines()
            if len(stu_lst) > 0:
                print('ID\t\t姓名\t\t英语成绩\tpython成绩\tJava成绩\t总成绩\t')
                print()
                for item in stu_lst:
                    d = dict(eval(item))
                    count = int(d['english']) + int(d['python']) + int(d['java'])
                    print('{0}\t{1}\t\t{2}\t\t{3}\t\t\t{4}\t\t{5}\t'.format(d['id'],d['name'],d['english'],d['python'],d['java'],count))
    else:
        return

def showNew(lst):
    print('ID\t\t姓名\t\t英语成绩\tpython成绩\tJava成绩\t总成绩\t')
    for item in lst:
        d = item
        count = int(d['english']) + int(d['python']) + int(d['java'])
        print(
            '{0}\t{1}\t\t{2}\t\t{3}\t\t\t{4}\t\t{5}\t'.format(d['id'], d['name'], d['english'], d['python'], d['java'],
                                                              count))
    print('-'*100)

if __name__ == '__main__':
    main()


