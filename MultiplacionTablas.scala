
8 kyu
Multiplication table for number
Scala:
def multiTable(n: Int): String = 
  var multiplo: Int = 1
  var tabla: String = ""

  while 
      multiplo <= 10
  do 
    tabla = tabla + s"$multiplo * $n = ${multiplo*n}"
    if multiplo < 10 then
      tabla = tabla + "\n"
    multiplo = multiplo + 1

  tabla
    

    
