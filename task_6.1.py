res=[]
def parse_log(txt_file="./nginx_logs.txt"):

    if txt_file:
        with open(txt_file,"r",encoding="utf-8") as file:
            for line in file:
                rm_add = line.split(" - - ")[0]
                rq_and_rs = line.split('"')[1]
                rq = rq_and_rs.split()[0]
                rs = rq_and_rs.split()[1]
                yield(rm_add, rq, rs)



if __name__ == "__main__":
   a = parse_log("./nginx_logs.txt")
   for i in a:
       res.append(i)

print(*res, sep='\n')
# print(type(res))
