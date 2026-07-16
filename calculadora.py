número1 = float(input("Digite o primeiro número: "))
número2 = float(input("Digite o segundo número: "))
operação = input("Digite a operação (+,-,/,*):")

if operação == "+" :
  resultado = número1 + número2

elif operação == "-" :
  resultado = número1 - número2

elif operação == "/" :
   if número1 != 0:
      resultado = número1 / número2

   if número1 < número2 :
      resultado = "não é possível dividir : o dividendo é menor que o divisor"


elif operação == "*" :
   resultado = número1 * número2

elif operação == "%" :
    resultado = "operação inválida : digite uma operação válida (+,-,*,/)"
else:
    resultado = "operação inválida"

print("Resultado:", resultado)

