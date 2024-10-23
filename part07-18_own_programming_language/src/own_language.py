# Write your solution here
import string
def run(prog: list)-> list:
    alp_l = list(string.ascii_uppercase)
    
    dc = {alp_l[i]:i for i in range(len(alp_l))}

    dc_ec = { 
        'ADD': lambda x, y: x + y,
        'SUB': lambda x, y: x - y,
        'MUL': lambda x, y: x * y,
        'DIV': lambda x, y: x / y
        } 

    compar_dc = {
         '>=': lambda x, y: x >= y,
         '<=': lambda x, y: x <= y,
         '==': lambda x, y: x == y,
         '>': lambda x, y: x > y,
         '<': lambda x, y: x < y
    } 

    star_i = 0
    res = []
    while True:
        for i in range(len(prog)):

            parts = prog[i].split(" ")

            if parts[0] == "MOV": 
                
                if parts[2] not in dc.keys():
                    dc[parts[1]] = int(parts[2]) 
                else:
                    dc[parts[1]] = int(dc[parts[2]])
                
            if parts[0].lower() == "print":
                    res.append(dc[parts[1]])
            ###math ecuasions
            if parts[0] in dc_ec.keys():       
                if parts[2] not in string.digits:
                    dc[parts[1]] = dc_ec[parts[0]](dc[parts[1]],  dc[parts[2]])
                    
                else:
                    dc[parts[1]] =  dc_ec[parts[0]](dc[parts[1]],  int(parts[2]))
                    
            ### loop 

            if parts[0] == 'begin:':
                start_i = i
            
            if parts[0] == 'IF':
            
                if compar_dc[parts[2]](dc[parts[1]],int(parts[3])): 
                    if parts[4] == "JUMP" and parts[5] == "start":
                        index = prog.index(parts[5] + ":")
                        i = index +1
                        strt_i=i
                        new_lst = prog[i:]
                        print(new_lst)
                        print(dc)
                        run(new_lst)

            # if parts[0].lower() == 'end':
            #     return res 

            
        return res
        # print(dc)
        # print(res)

if __name__=="__main__":
  rs = run(['MOV A 10', 'start:', 'PRINT A', 'SUB A 1', 'IF A > 0 JUMP start', 'END'] )
  print(rs)
