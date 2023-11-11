import os

Database = {
    'akun1' : {
        'nama': 'Luqman',
        'pin' : '123456',
        'saldo': 50000
    },
    'akun2': {
        'nama': 'hasan', 
        'pin':'311005',
        'saldo': 5000000
    },
    'akun3' : {
        'nama': 'fauzi', 
        'pin':'678910',
        'saldo': 5000000
    }
}

def getData():
    infile = open(os.getcwd()+"\\Percobaan\\database.txt","r").readlines()
    a=0
    b=1
    for i in infile:
        a=a+1
        if(a%3==0):
            Database['akun'+str(b)]['saldo']=eval(i)
            b=b+1
        elif(a%2==0):
            Database['akun'+str(b)]['pin']=i[0:-1]
        else:
            Database['akun'+str(b)]['nama']=i[0:-1]

    print(Database)

def setData(id,pin):
    Database[id]['pin']=pin
    outfile = open(os.getcwd()+"\\Percobaan\\database.txt","w")
    for i in range(1,4):
        outfile.write(str(Database['akun'+str(i)]['nama'])+'\n')
        outfile.write(str(Database['akun'+str(i)]['pin'])+'\n')
        outfile.write(str(Database['akun'+str(i)]['saldo'])+'\n')
    outfile.close()

def main():
    getData()
    setData('akun1',92857984257)
    
main()
