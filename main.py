import datetime
myBag = []



  


class MyObj:
  def __init__(self, titel, text, dat):
   
    self.titel = titel
    self.text = text
    self.dat = dat




#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   
def huvudmenu():
    print()
    print('"--------------Huvud Menyn------------------"')
    print('Tryck 1 för att skriva nytt inlägg i loggboken')
    print('Tryck 2 för att skriva ut alla loggar')
    print('Tryck 3 för att Radera en logg')
    print('Tryck 4 för att ta bort alla loggar')
    print('Tryck 0 för att avsluta programmet')
    print('-----------------------------------------')
    print()
  
    inp = läsindata()
    return inp
    
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 
  
def läsindata():

  realInput = 0
  validInt = False
  
  while not validInt:
    strInput = input('Ange ett val från menyn  ')
    if strInput.isdigit():
      inputInteger = int(strInput)
      if inputInteger >= 0 and inputInteger <= 4:
        realInput = inputInteger
        return realInput
        validInt = True

      else:
        print('Ogiltig val! Försök igen!')
        print('Skriv ett nummer mellan 0 och 4')
        
    else:
      print('Ange bara nummer')
      


  return realInput

    
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def läsindata2():

  realInput = 0
  validInt = False
  
  while not validInt:
    
    strInput = input('Vilken list nummer ligger loggen? ')
    if strInput.isdigit():
      inputInteger = int(strInput)
      if inputInteger >= 0 and inputInteger <= 100:
        realInput = inputInteger
        return realInput
        validInt = True
      else:
        print('Ogiltig val! Försök igen!')
        print('Skriv ett nummer mellan 0 och 4')
        
    else:
      print('Ange bara nummer')
      


  return realInput



#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

def läsindata3():

  realInput = 0
  validInt = False
  
  while not validInt:
    
    strInput = input('Hur många gånger vill du logga? ')
    if strInput.isdigit():
      inputInteger = int(strInput)
      if inputInteger >= 0 :
        realInput = inputInteger
        return realInput
        validInt = True

      else:
        print('Ogiltig indata! Försök igen!')
        print('Skriv ett nummer mer än 0 ')
        
    else:
      print('Ange bara nummer')
      


  return realInput


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  
    
def skrivNyttInlägg():
    print('----------------------------------')
    print('Välkommen till Min logBook! ')
    print()

    nub = läsindata3()
    if nub > 0:
      i = 0
      while i < nub:
        print('Ange bok titel {0}'.format(i+1))
        titel = input()
        print('Ange bok text {0}'.format(i+1))
        text = input()
        
        x = datetime.datetime.now().strftime("%x")
        y = datetime.datetime.now().strftime("%X")
        time = x + ' ' + y
        
        myObj = MyObj(titel, text, time)
        myBag.append(myObj)
        i += 1
      print('Alla info har sparat in listan!')  
    else:
      print('Inlägg avslutas!')
      
    
  #xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  
    
def skrivUtAllaLoggar():
    print()
    print()
    print('List av alla loggade info')
    print('===================================================')
    print('S/N \tTitel\t      Text\t      Date')
    print('===================================================')
    for a, b in enumerate(myBag):
     
      print(a + 1, '\t', b.titel,'\t   ', b.text, '\t  ', b.dat)
    
    print('----------------------------------------------------')
 
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
  
def RaderaEttLogg():
    print('List av loggar')
    print('====================================================')
    print('S/N \t Titel\t        Text\t      Date')
    print('===================================================')
    for index, logg in enumerate(myBag):
      
      print(index +1 , '\t', logg.titel,'\t', logg.text, '\t', logg.dat)
      
    print('------------------------------------------------------')
    print('======================================================')
    print()

    if len(myBag) > 0:

      while(True):
       
        mydelete = läsindata2()
        if mydelete < len(myBag) + int(1):
          myBag.pop(mydelete - 1)
          print()
          print('*****Din logg är bort tagit******')
          print()
          break
        else:
          print('Loggen finns inte i listan!')
          break

    else:
      print('Igenting i listan att radera!')
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx  
  


def tabortAllaloggar():
  myBag.clear()
  print('Alla loggade har bort tagit')


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

  



while(True):
  
  val2 = huvudmenu()
  
  if val2 == 0:
    print('Tack! Hej då!')
    break
      
  else:  
      while (True):
        if val2 == 1:
          skrivNyttInlägg()
          break
        elif val2 == 2:
          skrivUtAllaLoggar()
          break
        elif val2 == 3:
           RaderaEttLogg()
           break
        elif val2 == 4:
           tabortAllaloggar()
           break

        

