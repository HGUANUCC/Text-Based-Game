#No Help Wanted
#Author: Hugh Guan
#Date: Dec. 9th 2021-Jan.7th 2021
#This will be the ascii art that will be used repeatedly, so I could just call the variable instead of the actual ascii art
correct="""
  ______   ______   .______      .______       _______   ______ .___________. __  
 /      | /  __  \  |   _  \     |   _  \     |   ____| /      ||           ||  | 
|  ,----'|  |  |  | |  |_)  |    |  |_)  |    |  |__   |  ,----'`---|  |----`|  | 
|  |     |  |  |  | |      /     |      /     |   __|  |  |         |  |     |  | 
|  `----.|  `--'  | |  |\  \----.|  |\  \----.|  |____ |  `----.    |  |     |__| 
 \______| \______/  | _| `._____|| _| `._____||_______| \______|    |__|     (__)
"""
wrong="""
____    __    ____ .______        ______   .__   __.   _______ 
\   \  /  \  /   / |   _  \      /  __  \  |  \ |  |  /  _____|
 \   \/    \/   /  |  |_)  |    |  |  |  | |   \|  | |  |  __  
  \            /   |      /     |  |  |  | |  . `  | |  | |_ | 
   \    /\    /    |  |\  \----.|  `--'  | |  |\   | |  |__| | 
    \__/  \__/     | _| `._____| \______/  |__| \__|  \______|
"""
#Type writer function
import sys
from time import sleep
#I called this function print1 instead of print so that the typewriter function doesn't apply to my ascii arts
def print1(msg):
	for i in msg:
		sys.stdout.write(i)
		sleep(0.03)
		sys.stdout.flush()
	sys.stdout.write("\n")   
#This is the function that allows the gamer to actually move around in the map, it's also responsible for changing the coordinates of the map and therefore causing different results in the game
def rungame1():
	global x
	global y
	global myinput
	visited  =[ [False for i in range(5)]for j in range(5) ]
	while score<200:
		myinput = input('where do you want to go? (Press w for up, d for right, s for down, and a for left) \ntype q any time you want to quit\n').lower()
		if  myinput == 'd':
			x=x+1
			room(visited)
		elif  myinput == 's':
			y=y-1
			room(visited)
		elif  myinput == 'a':
			x=x-1
			room(visited)
		elif  myinput == 'w':
			y=y+1
			room(visited)
		elif myinput == 'q':
			break
		else:
			print1("invalid command")
#quiz question 1
def question1():
	global answer1
	global points
	answer1=int(input("What does stimulation mean?\n1.the action of pretending\n2.the action of raising excitement \n3. Being scared\n").strip())
	if answer1 == 2:
		points=points+1
		print(correct)
	else:
		print(wrong)
#quiz question 2
def question2():
	global answer2
	global points
	answer2 = int(input("What does keen mean?\n1. Being interested of something\n2. a type of food \n3. being annoying\n").strip())
	if answer2 == 1:
		points=points+1
		print(correct)
	else:
		print(wrong)
#quiz question 3
def question3():
	global answer3
	global points
	answer3=int(input("Who was the vet?\n1.Jacob \n2. Sam \n3. Mr.Zen\n").strip())
	if answer3 == 2:
		points=points+1
		print(correct)
	else:
		print(wrong)
#quiz question 4 
def question4():
	global answer4
	global points
	answer4=int(input("Why wasn't Bluey happy?\n1. He was hungry\n2. He wanted to play video games \n3. He was excluded from other friends\n").strip())
	if answer4 == 3:
		points=points+1
		print(correct)
	else:
		print(wrong)
#quiz question 5
def question5():
	global answer5
	global points
	answer5=int(input("Why did Posy decide to get help at last?\n1.She realized she needs help to do well \n2. She didn't want to take care of the fish anymore \n3. She didn't want people to blame her so she wanted everyone to help her\n").strip())
	if answer5 == 1:
		points=points+1
		print(correct)
	else:
		print(wrong)
#quiz main body 
def runquiz():
	global points
	points=0
	question1()
	("")
	question2()
	("")
	question3()
	("")
	question4()
	("")
	question5()
	print1 ("Nice job, you got %s" % points)
	print1 ("The total score was out of 5")
	print1 ("here are the correct answers: 2,1,2,3, and 1")
	moveon=input("press return when ready")
	if moveon==(""):
		start()

#Condition for ending the main game
def endgame():
	if score>=200:
		print1("Congratulations, Bluey is happier than ever, don't forget, collaboration was always important on your path to success!\n You achieved %s" % score)
	start()

#The introduction or the start before people choose the game
def introduction():
	global score
	global name
	moveon=input("Press return to move on")
	if moveon==(""):
		print ("""
                                                                 
                                                                                                              .  , *                                                                                     
                                                                                                             (#.( ,/   .*        .,                                                                     
                                                                                                                                                                                                        
                                                                                                           ( %, # *    ,/ / ((.(.#( &                                                                   
                                                                                                                                                                                                        
                                                                                                                       ,, . /#      ( ** .                                                              
                                                                                                        ,  ( ,  ( ,.   // / *,      (,,, #                                                              
                                                                                                                                                                                                        
                                                                                                     /#,#(*( ##.( #/ ( ((./ (#.(.(# #,(( #,,( /                                                         
                                                                                                                                                                                                        
                                                                                      ,/ .,** ,. (                                              .* % ,* ,/,, // (                                       
                                                                                    . ., /  / /  / .                                               *. / *. / ,.                                         
                                                                                                                                                                                                        
                                                                         /#*/( ( .                                                                                ((.( *%                               
                                                                                                                                                                                                        
                  /#.* ##.*.%# *,(# ,.*( *,.*                     #(.*                                                                                                      /% *                        
                  .  ,  , ,  , ,  , ,  , .                         . ,                                                                                                    /  .                          
                                     , ,  ,        .  ,                                                                                                                           .                     
                /            . .   ./,/# /  *    . /*,* / ,# ((                                                                                                                * #/ (                   
                                                                                                                                                                                                        
               .&.(#./ (*                     * /( (/,( /,                                    ( .  //*( /(*( /#.( /(                                                                /./,                
                          *                   .                                                                                                                                                         
                          #  / (    .(   ,  # (. # /. .                                                  *   /.                                                                       ./                
                #    # &% , #. , #% *  . ***. *.*. /. ,                                               ( * /# *../ /(                                                                  (. (              
                                                                                                                                                                                                        
                  /            (.// /,.( ( .%   .% (*,/ /*                                 .# (  *           *  ( ( ./,                            //,(.                              */                
                     .                   .    ,                                                  , ,                                                                                                    
                          /                             .  /                                       .  ( .*                                                                                              
                       %% ,  *      #  #           /.   (( .                                       (/.. *  %                                       #                                  #&                
                                                                                                                                                                                                        
                                                           # #/ *                                                                                                                     /(                
                                                                                                                                                                                                        
                                                                  (/ .  *                                                                                                           ,                   
                     &                                          & /. * *                                                                                                            (                   
                                                                                                                                                                                                        
                                                                          # (/ ( (#                                                                               %* /           #(                     
                                                                                                                                                                                                        
                                                                                    * // ,,** ,. / .                                                                 /,/% (                             
                                                                                 .. ,..* /  * / ./ *  /                                                           . ,, /, /.                            
                                                                                                                                                                                                        
                                                                                         % /# #,*# (/*# ##*# (#.% (( % (# #./% #.(% #,(( /./# /**# (/*# (#*#                                            
                                                                                                                                                                                                        
                                                                                                ,/ * ,/ *(,/ *( (       . ,                                                                             
                                                                                              .  .    * .. * .. (       . *                                                                             
                                                                                                      . .  .       ,                                                                                    
                                                                                                   . */ //,/ /( (.*    
 	""")
	#The greeting
	name = input("Hi, I am Bluey, what's your name?\n")
	print1("Hello " + name)
	print1("Welcome to my game " + name)
#The part that gives the options to choose the game and the basic instructions
def start(): 
	("")
	print("""
.___  ___.      ___       __  .__   __.    .___  ___.  _______ .__   __.  __    __  
|   \/   |     /   \     |  | |  \ |  |    |   \/   | |   ____||  \ |  | |  |  |  | 
|  \  /  |    /  ^  \    |  | |   \|  |    |  \  /  | |  |__   |   \|  | |  |  |  | 
|  |\/|  |   /  /_\  \   |  | |  . `  |    |  |\/|  | |   __|  |  . `  | |  |  |  | 
|  |  |  |  /  _____  \  |  | |  |\   |    |  |  |  | |  |____ |  |\   | |  `--'  | 
|__|  |__| /__/     \__\ |__| |__| \__|    |__|  |__| |_______||__| \__|  \______/  
                                                                                   
	""")
	print("""
 __         .___  ___.      ___       __  .__   __.      _______      ___      .___  ___.  _______ 
/_ |        |   \/   |     /   \     |  | |  \ |  |     /  _____|    /   \     |   \/   | |   ____|
 | |        |  \  /  |    /  ^  \    |  | |   \|  |    |  |  __     /  ^  \    |  \  /  | |  |__   
 | |        |  |\/|  |   /  /_\  \   |  | |  . `  |    |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
 | |  __    |  |  |  |  /  _____  \  |  | |  |\   |    |  |__| |  /  _____  \  |  |  |  | |  |____ 
 |_| (__)   |__|  |__| /__/     \__\ |__| |__| \__|     \______| /__/     \__\ |__|  |__| |_______|
	""")
	print("""
 ___               ___           ______      __    __   __   ________       ______    _______    
|__ \             /   \         /  __  \    |  |  |  | |  | |       /      /  __  \  |   ____|   
   ) |           /  ^  \       |  |  |  |   |  |  |  | |  | `---/  /      |  |  |  | |  |__      
  / /           /  /_\  \      |  |  |  |   |  |  |  | |  |    /  /       |  |  |  | |   __|     
 / /_   __     /  _____  \     |  `--'  '--.|  `--'  | |  |   /  /----.   |  `--'  | |  |        
|____| (__)   /__/     \__\     \_____\_____\\______/  |__|  /________|    \______/  |__|        
.___________.__    __   _______    .______     ______     ______    __  ___                      
|           |  |  |  | |   ____|   |   _  \   /  __  \   /  __  \  |  |/  /                      
`---|  |----|  |__|  | |  |__      |  |_)  | |  |  |  | |  |  |  | |  '  /                       
    |  |    |   __   | |   __|     |   _  <  |  |  |  | |  |  |  | |    <                        
    |  |    |  |  |  | |  |____    |  |_)  | |  `--'  | |  `--'  | |  .  \                       
    |__|    |__|  |__| |_______|   |______/   \______/   \______/  |__|\__\                      
	""")
	print("""
 ____           __       _______     ___   ____    ____  _______    .___________. __    __   _______      _______      ___      .___  ___.  _______ 
|___ \         |  |     |   ____|   /   \  \   \  /   / |   ____|   |           ||  |  |  | |   ____|    /  _____|    /   \     |   \/   | |   ____|
  __) |        |  |     |  |__     /  ^  \  \   \/   /  |  |__      `---|  |----`|  |__|  | |  |__      |  |  __     /  ^  \    |  \  /  | |  |__   
 |__ <         |  |     |   __|   /  /_\  \  \      /   |   __|         |  |     |   __   | |   __|     |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
 ___) |  __    |  `----.|  |____ /  _____  \  \    /    |  |____        |  |     |  |  |  | |  |____    |  |__| |  /  _____  \  |  |  |  | |  |____ 
|____/  (__)   |_______||_______/__/     \__\  \__/     |_______|       |__|     |__|  |__| |_______|    \______| /__/     \__\ |__|  |__| |_______|
                                                                                                                                                    
	""")
	Initiate = int(input("Which activity would you like to play? (type 1,2, or 3)\n"))
	#running main game
	if Initiate == 1:
		print1 ("Welcome to the classroom where Posy is!\n")
		print1 ("You approach a door, this is Room two and also the classroom that you will start this game in. Posy has just realized help is important, as Posy's best friend, of course you are invited to help out!\n")
		print1 ("You turn the knob, and the door swings open, sitting there is a little fish tank, with Bluey inside, hmm, there seems to be a lot of classrooms, this is surely a huge school,\n exploring them would be a good idea...")
		instructions = input("Do you need the basic instructions? yes/no)").lower()         
		if instructions == "yes":
			ready = input("There are 16 rooms for you to discover, use wasd to control the directions, in each room you would POSSIBLY discover something useful. Get to 200 points to win. Good luck!\n Press enter to move on!").strip()
			if ready == "":
				rungame1()  
		elif instructions == "no":
			rungame1()  
	#other option of running quiz
	elif Initiate == 2:
		runquiz()
	#quitting the game
	elif Initiate == 3:
		quit()
#Room conditions+score calculations+main text of game
def room(visited):
	global score
	global x
	global y
	if (visited[x-1][y-1]):
		print1("You moved back to a room you have already visited.")
	else:
		if (x ==1 and y == 4):
			print1("You walked into a room with shelves of book and stationaries, probably a storage room. \n You lock your sights on a bag of fish food, this would probably come in handy.")
			score = score+50
			print1("Congratulations! Bluey is happier, HP: %s" % score)
		elif (x ==2 and y == 4):
			print1("You walk into a room filled with the classmates of Posy, right in front there is a long line, \nevery student holding a tray, this must be the cafeteria. Suddenly, you hear someone to your left calling your name, you carry your fish bowl over, and they all meet together to play with Bluey, he seems to be in a cheerful mood now")
			score = score+30
			print1("Congratulations! Bluey is happier, HP: %s" % score)
		elif (x ==3 and y == 4):
			print1("Someone bumped into you, your fish bowl falling out of balance and almost spilling water. Bluey wakes up from his napping, \nand it looks like it's not the best time for Bluey")
			score = score-20
			print1("Bluey doesn't look as cheerful, but don't worry, keep exploring to help him! HP: %s" % score)
		elif (x ==4 and y == 4):
			print1("This is a room filled with books, wow! Ms. Smith welcomes you with a smile and hand you some puppets to play, \nsurely Bluey likes some puppet shows!")
			score = score+50
			print1("Congratulations! Bluey is happier, HP: %s" % score)
		elif (x ==1 and y == 3):
			print1("This rooms seems pretty familiar,\n wait, why are you back here at Posy's classroom, room two? We started here!")
		elif (x ==2 and y == 3):
			print1("A pack of food flakes, this will be a great treat for Bluey!")
			score = score+40
			print1("Congratulations! Bluey is happier, HP: %s" % score)
		elif (x ==3 and y == 3):
			print1("Mr.Zen has been waiting in this room, he assembled everyone in the class as a surprise!\n A puppet show performance is put on and seems like Bluey is having a lot of fun! ")
			score = score+100
			print1("Congratulations! Bluey is happier, HP: %s" % score)
		elif (x ==4 and y == 3):
			print1("This looks like an abandned school room, nothing here, and even the walls are falling apart, so boring...")
			score = score-10
			print1("Bluey is slightly bored, he lost a bit of his happiness HP: %s" % score)
		elif (x ==1 and y == 2):
			print1("This is the science room, you always wanted to come here, Bluey seems to be a bit scared of the snake and the lizard,\n but he's doing fine. Sam, the vet offers to check Bluey. Sam is a huge help, thanks very much!")
			score = score+30
			print1("Congratulations! Bluey is happier, HP: %s" % score)
		elif (x ==2 and y == 2):
			print1("You walk into the art room, realizing that Bluey needs to be fed, you rush to feed him some flakes, he got a little hungry though.")
			score = score-20
			print1("Bluey is a bit sad, but you can do this! HP: %s" % score)
		elif (x ==3 and y == 2):
			print1("This is the music classroom, the kids are playing some beautiful music, Bluey is enjoying it!")
			score = score+40
			print1("Congratulations! Bluey is happier, HP: %s" % score)
		elif (x ==4 and y == 2):
			print1("Whoo, this is a surprise, Mr.Zen found out that you didn't do your homework, Bluey doesn't seem to be happy about this.")
			score = score-40
			print1("Bluey is disappointed, better go do some homework... HP: %s" % score)
		elif (x ==1 and y == 1):
			print1("Jacob offers to help change the water in the fish bowl, it does give Bluey a better living environment.")
			score = score+20
			print1("Congratulations! Bluey is happier, HP: %s" % score)
		elif (x ==2 and y == 1):
			print1("You walk into the design lab, Jacob happens to be working there, Jacob happens to have a book of fish care, this is gonna help out.")
			score = score+60
			print1("Congratulations! Bluey is happier, HP: %s" % score)
		elif (x ==3 and y == 1):
			print1("This room is crowded with people, Bluey is a bit scared and shy")
			score = score-20
			print1("Don't worry, this isn't a big deal. Bluey'sHP: %s" % score)
		elif (x ==4 and y == 1):
			print1("Joining in on the assembly, Bluey seems to be enjoying the crowd.")
			score = score+20
			print1("Congratulations! Bluey is happier, HP: %s" % score)
		elif (x==5):
			print1("You are at the edge of the classrooms! You can't go anywhere")
			x=x-1
		elif (x==0):
			print1("You are at the edge of the classrooms! You can't go anywhere")
			x=x+1
		elif (y==5):
			print1("You are at the edge of the classrooms! You can't go anywhere")
			y=y-1
		elif (y==0):
			print1("You are at the edge of the classrooms! You can't go anywhere")
			y=y+1
		visited[x-1][y-1]=True
#All the above were just functions(This helps me organize my game)
#The starting assigned value of the room
score=0
x = 1
y = 3
#This is where the game actually starts: starts with ascii art
print ("""
____    __    ____  _______  __        ______   ______   .___  ___.  _______                                                             
\   \  /  \  /   / |   ____||  |      /      | /  __  \  |   \/   | |   ____|                                                            
 \   \/    \/   /  |  |__   |  |     |  ,----'|  |  |  | |  \  /  | |  |__                                                               
  \            /   |   __|  |  |     |  |     |  |  |  | |  |\/|  | |   __|                                                              
   \    /\    /    |  |____ |  `----.|  `----.|  `--'  | |  |  |  | |  |____                                                             
    \__/  \__/     |_______||_______| \______| \______/  |__|  |__| |_______|                                                            
                                                                                                                                         
.___________.  ______                                                                                                                    
|           | /  __  \                                                                                                                   
`---|  |----`|  |  |  |                                                                                                                  
    |  |     |  |  |  |                                                                                                                  
    |  |     |  `--'  |                                                                                                                  
    |__|      \______/                                                                                                                   
                                                                                                                                         
.__   __.   ______       __    __   _______  __      .______      ____    __    ____  ___      .__   __. .___________. _______  _______  
|  \ |  |  /  __  \     |  |  |  | |   ____||  |     |   _  \     \   \  /  \  /   / /   \     |  \ |  | |           ||   ____||       \ 
|   \|  | |  |  |  |    |  |__|  | |  |__   |  |     |  |_)  |     \   \/    \/   / /  ^  \    |   \|  | `---|  |----`|  |__   |  .--.  |
|  . `  | |  |  |  |    |   __   | |   __|  |  |     |   ___/       \            / /  /_\  \   |  . `  |     |  |     |   __|  |  |  |  |
|  |\   | |  `--'  |    |  |  |  | |  |____ |  `----.|  |            \    /\    / /  _____  \  |  |\   |     |  |     |  |____ |  '--'  |
|__| \__|  \______/     |__|  |__| |_______||_______|| _|             \__/  \__/ /__/     \__\ |__| \__|     |__|     |_______||_______/
""")
print ("""
     ___      __    __  .___________. __    __    ______   .______                         
    /   \    |  |  |  | |           ||  |  |  |  /  __  \  |   _  \     _                  
   /  ^  \   |  |  |  | `---|  |----`|  |__|  | |  |  |  | |  |_)  |   (_)                 
  /  /_\  \  |  |  |  |     |  |     |   __   | |  |  |  | |      /                        
 /  _____  \ |  `--'  |     |  |     |  |  |  | |  `--'  | |  |\  \----._                  
/__/     \__\ \______/      |__|     |__|  |__|  \______/  | _| `._____(_)                 
                                                                                           
 __    __   __    __    _______  __    __       _______  __    __       ___      .__   __. 
|  |  |  | |  |  |  |  /  _____||  |  |  |     /  _____||  |  |  |     /   \     |  \ |  | 
|  |__|  | |  |  |  | |  |  __  |  |__|  |    |  |  __  |  |  |  |    /  ^  \    |   \|  | 
|   __   | |  |  |  | |  | |_ | |   __   |    |  | |_ | |  |  |  |   /  /_\  \   |  . `  | 
|  |  |  | |  `--'  | |  |__| | |  |  |  |    |  |__| | |  `--'  |  /  _____  \  |  |\   | 
|__|  |__|  \______/   \______| |__|  |__|     \______|  \______/  /__/     \__\ |__| \__|
""")
#Functions being run
introduction()
start()	
endgame()
