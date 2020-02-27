from math import pi


class BatarySetion:
    """
    class to model temperature distrinution oh the surface of battery section
    """

    def __init__(self, length, inner_diameter, radial_wall_thickness, axial_wall_thickness, power_dissipation,
                 convection_coefficient, temperature_head, ambient_temperature=300):
        self.length = length
        self.inner_diameter = inner_diameter
        self.radial_wall_thickness = radial_wall_thickness
        self.axial_wall_thickness = axial_wall_thickness
        self.power_dissipation = power_dissipation
        self.temperature_head = temperature_head
        self.ambient_temperature = ambient_temperature

        if convection_coefficient is None:
            self.convection_coefficient = self.get_convection_from_temperature()
        else:
            self.convection_coefficient = convection_coefficient

    def __repr__(self):
        text = f'''Секция-{int(self.inner_diameter * 1e3)}: 
- мощность рассеяния = {self.power_dissipation} Вт, '
- коэффициент конвективного теплообмена = {self.convection_coefficient:.3f} Вт/(м²·°С)
- температурный напор = {self.temperature_head:.1f}°С'
        '''
        return text

    def get_surface_area(self):
        diameter = self.inner_diameter + self.axial_wall_thickness * 2
        length = self.length
        return pi * diameter ** 2 / 4 + pi * diameter * length

    def get_surface_heat_flux(self):
        return self.power_dissipation / self.get_surface_area()

    def get_convection_from_temperature(self):
        """
        a = qcт / (Т0—Тст)
            qcт      -> self.get_surface_heat_flux()
            (Т0—Тст) -> self.temperature_head
        :return: qc []
        """
        return self.get_surface_heat_flux() / self.temperature_head

    def get_temperature_from_convection(self):
        """

        (Т0—Тст) = qcт / a
            qcт      -> self.get_surface_heat_flux()
            a        -> self.convection_coefficient
        :return: (Т0—Тст)
        """
        return self.get_surface_heat_flux() / self.convection_coefficient
