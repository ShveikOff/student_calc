import csv
from collections import defaultdict
import time

tic = time.time()

student_dict_by_id = defaultdict(list)
student_dict_by_name = defaultdict(list)
student_dict_by_date = defaultdict(list)

class_dict_by_id = defaultdict(list)
class_dict_by_name = defaultdict(list)

with open (r"student_list_27.txt") as file:
    reader = csv.reader(file)
    for row in reader:
        student_id, student_name, year, semester, class_id = row
        student_id, year, class_id = int(student_id), int(year), int(class_id)
        student_dict_by_id[student_id].append((student_name, (year, semester), class_id))
        student_dict_by_name[student_name].append((student_id, (year, semester), class_id))
        student_dict_by_date[(year, semester)].append((student_id, student_name, class_id))

with open (r"class_list_27.txt") as file:
    reader = csv.reader(file)
    for row in reader:
        class_id, class_name, credit = row
        class_id, credit = int(class_id), int(credit)
        class_dict_by_id[class_id].append((class_name, credit))
        class_dict_by_name[class_name].append((class_id, credit))



def avg_cred_numb (input1, input2):
    all_credits = 0
    for id, info_list in input1.items():
        for item in info_list:
            class_id = item[2]
            all_credits += input2[class_id][0][1]
    return all_credits / len(input1)

def mid_class_cred (input):
    cred_arr = [input[id][0][1] for id in input]
    cred_arr = sorted(cred_arr)
    mid = len(cred_arr) // 2    # int(len(arr)/2)
    if mid*2 == len(cred_arr):
        return sum(cred_arr[mid-1 : mid+1])/2
    else:
        return cred_arr[mid]
   
def avg_cred_numb_by_stud (input1, input2):
    stud_avg_cred_dict = {}
    for id, info_list in input1.items():
        stud_cred = 0
        for item in info_list:
            class_id = item[2]
            stud_cred += input2[class_id][0][1]
        stud_avg_cred_dict[item[0]] = round (stud_cred / len(info_list), 2)
    return stud_avg_cred_dict

def var_class_cred (input1, input2):
    avg = avg_cred_numb(input1, input2)
    div_sum = 0     
    for id, info_list in input1.items():
        stud_cred = 0
        for item in info_list:
            class_id = item[2]
            stud_cred += input2[class_id][0][1]
        div_sum += (stud_cred - avg) ** 2
    
    return div_sum/len(input1)

def david_beckham_classes (input1, input2):
    list_of_classes = []
    for item in input1['David Beckham']:
        class_id = item[2]
        list_of_classes.append(input2[class_id][0][0])
    return list_of_classes

def best_student (input1, input2):
    max_cred = 0
    best_student = ''     
    for name, info_list in input1.items():
        stud_cred = 0
        for item in info_list:
            class_id = item[2]
            stud_cred += input2[class_id][0][1]
        if stud_cred > max_cred: max_cred, best_student = stud_cred, name
    
    return (best_student, max_cred)

def lebron_james_classes (input1, input2):
    list_of_classes = []
    for item in input1['LeBron James']:
        class_id = item[2]
        if item[1] == (2023, 'Spring'):
            list_of_classes.append(input2[class_id][0][0])
    return list_of_classes

def usain_bolt_check (input1, input2):
    for item in input1['Usain Bolt']:
        class_id = item[2]
        if item[1] == (2024, 'Spring'):
            return True
    return False

def maria_roger_check (input):
    if len(input['Maria Sharapova']) > len(input['Roger Federer']):
        return True
    return False

def stud_in_date (input):
    if (2022, 'Spring') in input:
        return True
    return False

def max_class_name (input):
    max_class_name = ''
    for name, info_list in input.items():
        for item in info_list:
            if len(item[0]) > len(max_class_name):
                max_class_name = item[0]
    return max_class_name

print (avg_cred_numb(dict(student_dict_by_id), dict(class_dict_by_id)))
print (mid_class_cred(dict(class_dict_by_id)))
print (avg_cred_numb_by_stud(dict(student_dict_by_id), dict(class_dict_by_id)))
print (var_class_cred(dict(student_dict_by_id), dict(class_dict_by_id)))
print (david_beckham_classes(dict(student_dict_by_name), dict(class_dict_by_id)))
print (best_student(dict(student_dict_by_name), dict(class_dict_by_id)))
print (lebron_james_classes(dict(student_dict_by_name), dict(class_dict_by_id)))
print (usain_bolt_check(dict(student_dict_by_name), dict(class_dict_by_id)))
print (maria_roger_check(dict(student_dict_by_name)))
print (stud_in_date(student_dict_by_date))
print (max_class_name(dict(class_dict_by_id)))

toc = time.time()

print (toc - tic)
