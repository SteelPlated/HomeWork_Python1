'''2.Напишите программу для. проверки истинности
утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
для всех значений предикат.
'''

x=int(input('Введите x: '))
y=int(input('Введите y: '))
z=int(input('Введите z: '))

if ~(x or y or z)== (~x and ~y and ~z):
    print('true')
else:
    print('false')