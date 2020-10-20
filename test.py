"""The template of the main script of the machine learning process
"""

import games.arkanoid.communication as comm
from games.arkanoid.communication import ( \
    SceneInfo, GameInstruction, GameStatus, PlatformAction
)

def ml_loop():
    

    # === Here is the execution order of the loop === #
    # 1. Put the initialization code here.

    # 2. Inform the game process that ml process is ready before start the loop.
    comm.ml_ready()
    ballisfall=True
    ball_postition_history=[]
    bx=100
    by=100
    pfm=95
    fbx=100
    # 3. Start an endless loop.
    while True:
       
        scene_info = comm.get_scene_info()
        
        pfm=scene_info.platform[0]+20
        if by < scene_info.ball[1]:
            ballisfall=True
        else:
            ballisfall=False
        bx=scene_info.ball[0]
        by=scene_info.ball[1]
        if bx <= 7:
            print(scene_info.ball)
                
        if bx >= 193:
            print(scene_info.ball)
        if ballisfall:
                      
            if 350 > by > 210:        
               if bx <= 7:
                print(scene_info.ball)
                fbx = 407 - by  
               if bx >= 193:
                print(scene_info.ball)
                fbx = 200-(407-by)
                                  
            if 210>by >120 :
              if bx<=7:
                 fbx = 180
              if bx>=193:
                 fbx = 20      
             
            if pfm < fbx:
               comm.send_instruction(scene_info.frame, PlatformAction.MOVE_RIGHT)
            if pfm > fbx:
               comm.send_instruction(scene_info.frame, PlatformAction.MOVE_LEFT)
        