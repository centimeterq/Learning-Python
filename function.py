# function syntax

def print_name(parameter) :
    print(parameter)

# penulisan function di python di mulai dengan def nama_function() :

# di dalam () ada parameter, jadi jika kamu ingin memberikan value ke function bisa di dalam () eg : nama_function(value)

print_name("Historia Reiss") # output Historia Reiss

# function return value
# dalam function kamu bisa mereturn sebuah nilai eg :

def pertambahan(a,b) :
    return a + b

pertambahan(2,5) # ini tidak akan mengeluarkan output, karena function pertambahan hanya mereturn sebuah nilai, tidak mencetaknya
# jika ingin memcetak nilai nya harus kalian print terlebih dahulu

print(pertambahan(5,5)) # output 10
