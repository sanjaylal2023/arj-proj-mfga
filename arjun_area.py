#### program to find volume of a sphere
from os import system, name
from time import sleep


class Area():
    def __init__(self):
          variable001 = 1
    
    def area_square(self):
        len=int(input('Enter length of sq : ' ))
        #print('Enter length ::: ' + str(len))
        #length=int(input('Enter length : '))
        self.len=len
        area_sq = len * len 
        print('Area sq : ' + str(area_sq))
          
    
    def area_rect(self):
        length=int(input('Enter Length of a rectangle : '))
        breadth=int(input('Enter width of a rectangle : '))
        area_sq = length * breadth 
        print('Area rectangle  : ' + str(area_sq))
    
    def area_of_circle(self):
        radius=int(input('Enter Radius : '))
        area_circle=22/7.0 * (radius) * (radius)
        print('Area circle  : ' + str(area_circle))
                    # define our clear function
    def clear(self):
      #print('printing name of system::: ' + name)
    # for windows
        if name == 'nt':
           # print('clearing!!!....')
            _ = system('cls')

'''                    
option=True
area_obj=Area()
try:
    while option:
        area_obj.clear()
        print('Select 1 for area of sq\n')
        print('Select 2 for area of Rect\n')
        print('Select 3 for area of Circle \n')
        print('Select 4 to Exit \n')

        option=int(input('Enter your option'))
           
        if option==1:
            area_obj=Area()
            area_obj.area_square()
            option=True 
        elif option==2:
            area_obj=Area()
            area_obj.area_rect()
            option=True 
        elif option==3:
            try:    
                area_obj=Area()
                area_c=area_obj.area_of_circle()
                area_c=area_c/0
                option=True
            except ZeroDivisionError:
                print('Division by zero!') 
                
        else:
            print('Exiting!!!')
            option=False
            exit
       
        
except KeyboardInterrupt:
                print('someone tried to stop execution with stop button')
except:
                print('do nothing')
finally:
                print('final is finally executing!!')

if __name__ == "__main__":
    print('hi there, I am MAN main ')

'''

#z=area_of_circle()
#a=area_rect()
print('finished my code and uploaded to github')
