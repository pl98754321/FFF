def create_list(num):
  from random import randint, getrandbits
  listC = [randint(-10,10) for i in range(num)]
  return listC
#----------------------------------------------
def create_dict(num):
  from random import randint, getrandbits
  import string
  dictA = dict()
  le = string.ascii_letters
  for i in range(num):
    if i == randint(1,num):
      dictA[le[randint(1,51)]] = i
    else:
      dictA[i] = le[randint(1,51)]+le[randint(1,51)]+le[randint(1,51)]+le[randint(1,51)]
  return dictA
#----------------------------------------------
def creatlistfriend(j):
  k = []
  k.append(j)
  listfriend = []
  for i in range(k[0].count("title=")):
    num1 = k[i].find("title=")
    k.append(k[i].replace(k[i][0:num1+7],"",1))
    num2 = k[i+1].find("\"")
    listfriend.append(k[i+1][0:num2])
  return listfriend
#--------------
def creatOrNotfunction():
  creatOrNot = input("y/n :: ")
  if creatOrNot == "y":
    return True
  elif creatOrNot == "nomore":
    return 0
  elif creatOrNot == "n":
    return False
  else:
    print("just ",end="")
    return creatOrNotfunction()

def friend_creat():
  from tkinter import filedialog
  import json
  localFile = r'C:\Users\computer\Desktop\dataSci\data_after_raw\\'
  all_friend_list = {}
  numberFriend = int(input("how many friend u have ::"))

  for i in range(numberFriend):
    name = input("Input friendname " + str(i + 1) + " :: ")
    k = filedialog.askopenfilename()
    f = open(k)
    all_friend_list[name] = creatlistfriend(f.read())

    #creat file to keep data
    creatfiles(all_friend_list[name],name,".txt")
  summary_namefile = input("input summary_namefile ::")
  creatfiles(all_friend_list,summary_namefile,".txt")
  return all_friend_list

def creatfiles(data,name,filetype):
  import numpy as np
  import json
  localFile = r'C:\Users\computer\Desktop\dataSci\data_after_raw\\'
  if type(data) == type(np.array([1])):
      np.savetxt(localFile + "summary" + ".txt", data, delimiter=',')
  elif type(data) != str():
    with open(localFile + "summary" + ".txt", 'w+') as name1:
      name1.write(json.dumps(data))
  else :
    with open(localFile + name  + filetype, 'w+') as name1:
        name1.write(str(data))

def checkDictfirend():
  from tkinter import filedialog
  print("do u wat to create Dict fried ",end="")
  if creatOrNotfunction():
      friend_data = friend_creat()
  else :
      print("input firend data ")
      k = filedialog.askopenfilename()
      with open(k, 'r') as inf:
        friend_data = eval(inf.read())
  return friend_data