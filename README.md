# temperature-calculation-of-battery-section
## super-simple analytical model of convective heat transfer for calculating the temperature on the surface of a cylindrical body

Для описания конвективной теплоотдачи используется формула:

$$q_{cт} = a*(Т_0—Т_{ст}), (1)$$

где $q_{cт}$ — плотность теплового потока на поверхности, $\frac{Вт}{(м^2·°С)}$; $a$ — коэффициент теплоотдачи, $\frac{Вт}{(м^2·°С)}$; $Т_0$ и $Т_{ст}$ — температуры среды (жидкости или газа) и поверхности соответственно. Величину $Т_0-Т_{ст}$ часто обозначают $\DeltaТ$ и называется температурным напором.
  
1. `get_convection_from_temperature`

  Из уравнения (1) следует что коэффициент теплоотдачи равен
  
$$a = {q_{cт}\over{(Т_0—Т_{ст})}}, (2)$$

2. `get_temperature_from_convection`

  Из уравнения (1) следует что температурный напор `temperature_head` равен:
   
$$(Т_0—Т_{ст}) = {q_{cт} \over a}, (3)$$
