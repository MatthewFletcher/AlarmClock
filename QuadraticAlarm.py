#Alarm clock to generate random math problem to solve


#Imports
import random
import subprocess



#Define problem types






#Generate Quadratic Equation
def solveQuadratic():
    while True:
        #Generates 2 solutions for a quadratic equation and then generates quadratic based from solutions

        #Generate 2 random solutions using randint
        solution1=random.randint(-10,10)
        solution2=random.randint(-10,10)


       #Term numbers are labeled using the power of the exponent.

        #x^2 term
        term2=1

        #Linear term
        term1=-1*(solution1+solution2)

        #Constant term
        term0=solution1*solution2

        # Create strings of acceptable answers
        validanswer1 = "("+str(solution1) + ", " + str(solution2)+")"
        validanswer2 = "("+str(solution2) + ", " + str(solution1)+")"

        #Ask user to solve equation
        print("Solve the following quadratic equation")
        print("Enter your solutions in the form (x1, x2)")

        #Print equation

        #To whoever reads my code, I'm so sorry you have to look at this godawful statement.

        #This ugly section of code displays the equation correctly by removing extraneous signs from viewing.

        if term1>0 and term0>0:
            print("x^2+"+str(term1)+"x+"+str(term0)+"=0")
        elif term1==0 and term0>0:
            print("x^2+"+str(term0)+"=0")
        elif term1<0 and term0>0:
            print("x^2-"+str(-term1)+"x+"+str(term0)+"=0")


        elif term1>0 and term0==0:
            print("x^2+"+str(term1)+"x"+"=0")
        elif term1==0 and term0==0:
            print("x^2+"+"=0")
        elif term1<0 and term0==0:
            print("x^2-"+str(-term1)+"x"+"=0")


        elif term1>0 and term0<0:
            print("x^2+"+str(term1)+"x-"+str(-term0)+"=0")
        elif term1==0 and term0<0:
            print("x^2-"+str(-term0)+"=0")
        elif term1<0 and term0<0:
            print("x^2-"+str(-term1)+"x-"+str(-term0)+"=0")


        #If you manage to get here, then you did something that I didn't even know was possible.
        #Or I suck at debugging. One of the two.
        else:
            print"You shouldn't be here"

        #Cue for solution input. Input must currently be entered as two integers separated by a comma and space, and surround by parentheses.
        getsolution=str(input("Enter the solutions separated by a comma>>>"))


        #Check if the solutions are valid.
        #if the solutions are valid, break out of the loop. Otherwise, make the user solve another problem.
        if getsolution==validanswer1 or getsolution==validanswer2:
            print("Congratulations, problem solved!")
            break
        else:
            print ("Solution incorrect, please try again")



#From Stack Overflow thread "Playing audio files with python"

#Do some random magic I'm not entirely sure on
player = subprocess.Popen(["mplayer", "home/matt/Music/RightNow.mp3", "-ss", "30"], stdin = subprocess.PIPE,stdout = subprocess.PIPE, stderr = subprocess.PIPE)


#After music begins to play, start the problem solving.
solveQuadratic()


#Return a q to the mplayer pipe to kill music
player.stdin.write("q")




