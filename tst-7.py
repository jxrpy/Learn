#!/usr/bin/env python3
''' Pass a string to this program to see how long it takes to randomly guess it.
    Just as a warning, you will turn your computer into a heater depending on the size
    of the phrase. Anything over 5 or 6 characters can take a while
''' 
def run(text):
  import random
  
  chars = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
           'v','x','y','w','z']
  
  num_op = {6:('Million',1000000), 7:('Million',1000000), 8:('Million',1000000),
            9:('Billion',1000000000), 10:('Billion',1000000000), 11:('Billion',1000000000),
            12:('Trillion',1000000000000), 13:('Trillion',1000000000000), 14:('Trillion',1000000000000),
            15:('Quadrillion',1000000000000000), 16:('Quadrillion',1000000000000000),
            17:('Quadrillion',1000000000000000), 18:('Quintillion',1000000000000000000),
            19:('Quintillion',1000000000000000000),20:('Quintillion',1000000000000000000)}

  if type(text) is str and text != '':
    text = text.lower()
    for i in text:
      if i in chars:
        pass
      else:
        raise ValueError('Only chars a through z and space are acceptable')
  else:
    raise TypeError('Must be a string of at least one character')
    
  
  def genstr():
    phrase = ''
    for i in range(len(text)):
      phrase += random.choice(chars)
    return phrase
  
  
  def chkstr(phrase):
    if phrase == text:
      return 100
    j = 0
    for i in range(len(phrase)):
      if phrase[i] == text[i]:
        j += 1
    
    return j*100/len(text)
  
  
  best_score = 0
  best_phrase = ''
  prv_best_score = 0
  i = 0
  while True:
    i += 1 
    phrase = genstr()
    score = chkstr(phrase)

    if score == 100:
      print('Even I can do it, phrase:{} on attempt:{:d}'.format(phrase,i))
      break
    elif score > best_score:
      best_score = score
      best_phrase = phrase

    if i % 100000:
      pass
    elif best_score > prv_best_score:
      print('')
      print('Best phrase so far: {} , with a score:{:.2f}%, on try:{:d}'.format(best_phrase,best_score,i))
      marks = ''
      p = 0
      for t in range(len(text)):
        if best_phrase[t] == text[t]:
          marks += '|'
          p += 1
        else:
          marks += ' '
      print('                    '+marks+'  hits:{:d}'.format(p))
      print('Phrase to match   : {}'.format(text))
      prv_best_score = best_score

    if i % 1000000:
      pass
    else:
      zeros = str(i).count('0')
      print('Attempts so far: {:d} {:s}'.format(int(i/num_op[zeros][1]),num_op[zeros][0]))

    if i % 10000000:
      random.shuffle(chars)    # shuffle chars every 10 Million attempts. Make it interesting.

    if i > 99999999999999999999:
      print('==> I GIVE UP <==')
      break

if __name__ == "__main__":
  import sys
  run(sys.argv[1])

