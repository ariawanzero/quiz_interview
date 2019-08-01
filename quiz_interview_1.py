def main():
  inp = "key1=value1;key2=value2\nkeyA=valueA\n"
  a = load(inp);
  print("Result Load : ")
  print(a)

  textz = store(a)

  print("Result Store : ")
  print(textz)

def load(texts):
  a = []
  for text in texts.split("\n"):
    if text:
      temp = dict()
      for item in text.split(";"):
        temp[item[:item.index("=")]] = item[item.index("=")+1:]
      a.append(temp)

  return a

def store(arr):
  textz = []
  for data in range(len(arr)):
    temp = []
    for key, value in arr[data].items():
      temp.append("{}={}".format(key, value))
    textz.append(";".join(temp))

  return "\n".join(textz)
    
if __name__ == "__main__":
  main()
