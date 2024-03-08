
def sendTestEncoding(type, numOfChar) :
    if(type == "shift") :
        command = "task" +" " + type + " " + "encode" + " " + str(numOfChar)
        ISCt_header = bytes(f"ISCs", 'utf-8')
        total_length = len(command).to_bytes(2, byteorder='big')
        res  = ISCt_header + total_length

        for i in command :
            res += bytes(i, 'utf-8')
        print(res)
        return res



sendTestEncoding("shift",6)