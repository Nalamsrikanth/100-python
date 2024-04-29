print('''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \.'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\.U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\.U/'.-'    o |'|
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-' 
                    ''')
print(" Welcome to the treasure island")
print("Your mission is to find the treasure")
left_or_right = input("please select which direction you want to go:").lower() # .lower()is used to take the input text in lower case
if left_or_right == "left":
    swim_or_run = input("Thats great you have selected the correct way: now do you want to swim or run:").lower()
    if swim_or_run == "run":
        vehicle = input("Wow you have reach the final stage which way you want to ride: bike, airplane, boat:").lower()
        if vehicle == "bike":
            print("the prize of this game is bike you won")
        elif vehicle == "airplane":
            print("sorry you loss")
        elif vehicle == "boat":
            print("you loss")
    else:
        print("sorry you cant swim")
else:
    print("sorry you loss")