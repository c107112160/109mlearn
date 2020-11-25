import pickle
import numpy as np
from os import listdir
from os.path import isfile, join

dirpath ='C:\\Users\\user\\Desktop\\lab\\MLGame-beta4.0\\games\\arkanoid\\Log'
BallPosition = []
PlatformPosition = []
LRUP = []
last_ball_x = 0
last_ball_y = 0
files = listdir(dirpath)
log_number = 0 #
pas = 0 
for f in files :
 
      log_number=log_number +1          #
      fpath = join(dirpath,f)       #
      if isfile(fpath):                 #判斷是否為 檔案
         with open(fpath,"rb") as f1 :  #
               data=pickle.load(f1)  
         for i in range(0,len(data)):
             if data[i].status=="GAME_PASS":
               pas +=1
             BallPosition.append(data[i].ball) #陣列最後方加入ball座標
             PlatformPosition.append(data[i].platform)
             if(i>=-1):
                if(last_ball_x - data[i].ball[0] > 0):#判斷左右移動
                    LR = 1
                else:
                    LR = 0  
                if(last_ball_y - data[i].ball[1] > 0):#判斷掉落
                    UP = 0
                else:
                    UP = 1
                LRUP.append(np.array((LR,UP)))
             last_ball_x = data[i].ball[0]
             last_ball_y = data[i].ball[1]             
platx= np.array(PlatformPosition)[:,0][:,np.newaxis]
platx = platx-20
nextp = platx[1:]

instrust = (nextp-platx[0:len(nextp)])/5
ballarray=np.array(BallPosition[0:len(nextp)])
LRUP=np.array((LRUP[0:len(nextp)]))
x=np.hstack((ballarray,LRUP,platx[:-1]))
 
y=instrust
#np.set_printoptions(threshold=np.inf)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 41)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(x_train,y_train)

yknn_bef_scaler = knn.predict(x_test)
acc_knn_bef_scaler = accuracy_score(yknn_bef_scaler,y_test)

print('log number : ' + str(log_number))
print(acc_knn_bef_scaler)
print(pas)

filename = "C:\\Users\\user\\Desktop\\lab\\MLGame-beta4.0\\games\\arkanoid\\ml\\123.sav"
pickle.dump(knn,open(filename,"wb"))
