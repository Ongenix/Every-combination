def convert(text):
  text = str(text)
  if len(text) % 2 != 0:return
  
  chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-= ";word = ""
  for i in range(0, len(text), 2):
    statement = int(str(text[i])+str(text[i+1]))
    if statement < len(chars):
      word += chars[statement]
  return word

def main():
  #••-----Options-----••#
  debug = True
  password = "abc"
  colourful_text = True
  max_num = pow(100000, 1000000)
  #••⚠️The-Code-is-Below⚠️••#
  if colourful_text:from colorama import Fore
  last = 0
  for i in range(1000, max_num):
    x = convert(i)
    if debug and x and (last + 1000) < i:
      if colourful_text:
        print(f"{Fore.LIGHTMAGENTA_EX}{x}{Fore.RESET}")
      else:
        print(x)
      last=i
    if x == None:
      i+=10
    elif x == password:
      exit(x)

if __name__ == '__main__':
  main()
