from sys import exit

class WinLose:

	def lose(self):
		print("You lose.  The animals are sad.  Please leave Pet Place.")
		exit(0)

	def winner(self):
	#if self.happy_animal == ["Golden Retriever", "Peacock", "Bunny"]:
		print("Congratulations!  You won the game.")
		print("All of the animals are so happy!")
		print("""\
**********************************************************************


				      
                  aaiittllttiiaa
              k a i t llyyll t i a k
            k a i t l yynnyy l t i a k					  
          k a i t l y nn  nn y l t i a k						
        k a i t l y n        n y l t i a k  
       k a i t l y n          n y l t i a k 
      k a i t l y n            n y l t i a k

                          .".
                         /  |
                        /  /
                       / ,"
           .-------.--- /
          "._ __.-/ o. o\  
             "   (    Y  )
                  )     /
                 /     (
                /       Y
            .-"         |
           /  _     \    \ 
          /    `. ". ) /' )
         Y       )( / /(,/
        ,|      /     )
       ( |     /     /
        " \_  (__   (__        
            "-._,)--._,)

*********************************************************************
			""")

		exit(0)

	#else:
	#	break