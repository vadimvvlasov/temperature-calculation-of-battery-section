from math import pi
import pandas as pd


def load_section_parameters(file_name):
    return pd.read_excel(file_name)


def get_instances_from_input_data(df, convection_coefficient_calculated, pr=0):
    batary_sections = {}
    for index, row in df.iterrows():
        name = int(row[0])
        batary_sections[name] = BatarySetion(length=row[1],
                                             inner_diameter=row[2],
                                             radial_wall_thickness=row[3],
                                             axial_wall_thickness=row[4],
                                             power_dissipation=15,
                                             convection_coefficient=convection_coefficient_calculated,
                                             temperature_head=None)
        if pr:
            print(f'Секция-{name}, (Т0—Тст) = {batary_sections[name].temperature_head:.1f} °С')
    return batary_sections


def print_surfase_temperature(batary_sections):
    for sec_name, sec_obj in batary_sections.items():
        print(f'Секция-{sec_name}:')
        print(f'    температурный напор (Т0—Тст)={sec_obj.temperature_head:.1f} °С, ')
        print(f'    коэффицинт теплоотдачи a={sec_obj.convection_coefficient:.2f} Вт/(м²·°С), ')


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
        self.convection_coefficient = convection_coefficient
        self.ambient_temperature = ambient_temperature

        if temperature_head is None:
            self.temperature_head = self.get_temperature_from_convection()
        else:
            self.temperature_head = temperature_head

        if convection_coefficient is None:
            self.convection_coefficient = self.get_convection_from_temperature()
        else:
            self.convection_coefficient = convection_coefficient

    def __repr__(self):
        text = f'''Секция-{int(self.inner_diameter * 1e3)}: 
- мощность рассеяния = {self.power_dissipation} Вт,
- коэффициент конвективного теплообмена = {self.convection_coefficient:.3f} Вт/(м²·°С),
- температурный напор = {self.temperature_head:.1f}°С.
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
