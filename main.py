from pyscript import document, display

def checknumbah(e):
    
    numberz= ["69", "420", "67", "61", "911"]
    
    numone= document.getElementById("numone").value
    name= "isaias u dirty diva dawg"
    
    confirm_numbah = numone in numberz
    
    message = (f'Sorry {name}, your number is not found at this very moment.' , f'CONDRAGULATIONS {name}, YOUR NUMBER AND MY WIGS HAVE BEEN FOUND!!')
    
    document.getElementById("output1").innerHTML = message[confirm_numbah] 
    