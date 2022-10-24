def arithmetic_arranger(problems, val=False):

  first_line = "" 
  second_line = ""
  dash_line = ""
  answer_line = ""
  calculator = ""

  for p in problems:
    p_list = p.split()
    first = p_list[0]
    second = p_list[1]
    third = p_list[2]

    max_length = max(len(str(first)), len(str(third))) +2 
    
    top = ""
    top = str(first).rjust(max_length)

    bottom = ""
    bottom = str(second) + str(third).rjust(max_length-1)

    dash = ""
    for r in range(max_length):
      dash += "-" 
    
    if len(problems) > 5:
       return "Error: too many problems"
    
    if first.isnumeric() != True or third.isnumeric() != True:
       return "Error: Numbers must only contain digits"

    if len(str(first)) >=5 or len(str(third)) >= 5:
       return "Error: Numbers cannot be more than four digits"

    if second == "-":
        end = int(first) - int(third)
    elif second == "+":
        end = int(first) + int(third)
    else:
        return "Error: Operator must be '+' or '-'"
      
    end = ""
    end = str(end).rjust(max_length)

    if p != problems[-1]:
       first_line += top + "    "    
       second_line += bottom + "    "
       dash_line += dash + "    "
       answer_line += end + "    "
    else:
       first_line += top
       second_line += bottom
       dash_line += dash
       answer_line += end

  if val:
     calculator = first_line + "\n" + second_line + "\n" + dash_line + "\n" + answer_line
  else:
     calculator = first_line + "\n" + second_line + "\n" + dash_line  
    
  return calculator
