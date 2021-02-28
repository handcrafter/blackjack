[1mdiff --git a/player/player.py b/player/player.py[m
[1mindex b2decb7..6ac77c2 100644[m
[1m--- a/player/player.py[m
[1m+++ b/player/player.py[m
[36m@@ -28,6 +28,14 @@[m [mclass Player():[m
         Returns:[m
             int: amount of money the player has bet[m
         """[m
[32m+[m[32m        while True:[m
[32m+[m[32m            try:[m
[32m+[m[32m                inp_bet = input("How much do you want to bet?")[m
[32m+[m[32m            except ValueError:[m
[32m+[m[32m                print("Wrong input. Try again")[m
[32m+[m[32m            else:[m
[32m+[m[32m                break[m
[32m+[m
         raise NotImplementedError[m
 [m
     def act(self) -> Action:[m
[36m@@ -36,4 +44,18 @@[m [mclass Player():[m
         Returns:[m
             Action: action taken by the player[m
         """[m
[32m+[m[32m        while True:[m
[32m+[m[32m            inp_action = input("type h for hit and s for stay")[m
[32m+[m[32m            if inp_action[0].lower() == 'h':[m
[32m+[m[32m                print("Player hits")[m
[32m+[m[32m                return Action.HIT[m
[32m+[m[32m            elif:[m
[32m+[m[32m                inp_action[0].lower() == 's':[m
[32m+[m[32m                print("Player stands")[m
[32m+[m[32m                return Action.STAY[m
[32m+[m[32m            else:[m
[32m+[m[32m                print("Wrong input.Try again")[m
[32m+[m[32m                continue[m
[32m+[m[32m            break[m
[32m+[m
         raise NotImplementedError[m
