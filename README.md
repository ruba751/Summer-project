# Real Time Lab 2020/2021 

# About
        This project is about detecting an exit from within a room with an open exit 
        using Orb_slam 
# Team
        Ruba Rushrush
# Reference
        I got help for doing this project from alpha quadratic team
        (Wajeeh Atrash, Saji Asii, Farouk kraeem)
# Instructions
        Inorder to activate this project:
        1- you need to run main.py
        2- when orb slam finishes press "fly"
        and that's it :)
        
# Algorithim
        After scanning the room, orb slam returns a cloud point
        we will calculate the midean point of all points, create a rectangle of length 2*(distance from the midean point and the center(0,0)
        cleaning all points within this rectangle
        detecting which quarter has more valid points (after the cleaning in last step)
        calculate the midean point in that choosen quarter
        calculate the angle and distance to that point from the center
        fly the drone to that point 
        
 # X Z graph for the point cloud I recieved from the orb slam2        
https://user-images.githubusercontent.com/70092224/131532672-f031a495-ba00-475e-8f56-73796b09a2fd.jpeg


 # X Z graph for the point cloud after proccessing
 https://user-images.githubusercontent.com/70092224/131532788-deba1c69-c410-4f91-89ba-6ae4d26fc5f2.jpeg
