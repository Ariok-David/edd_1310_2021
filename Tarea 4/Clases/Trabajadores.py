from Clases.Arrays import Array
import datetime as dt

class Trabajador():

    def __init__(self, numero_trabajador, nombres, paterno, materno, horas_extra, sueldo_base, anio_ingreso):
        self.__numero_trabajador = numero_trabajador
        self.__nombres = nombres
        self.__paterno = paterno
        self.__materno = materno
        self.__horas_extra = horas_extra
        self.__sueldo_base = sueldo_base
        self.__anio_ingreso = anio_ingreso

    def set_numero_trabajador(self, numero_trabajador):
        self.__numero_trabajador = numero_trabajador

    def get_numero_trabajador(self):
        return self.__numero_trabajador

    def set_nombres(self, nombres):
        self.__nombres = __nombres

    def get_nombres(self):
        return self.__nombres

    def set_paterno(self, paterno):
        self.__paterno = paterno

    def get_paterno(self):
        return self.__paterno

    def set_materno(self, materno):
        self.__materno = materno

    def get_materno(self):
        return self.__materno

    def set_horas_extra(self, horas_extra):
        self.__horas_extra = horas_extra

    def get_horas_extra(self):
        return self.__horas_extra

    def set_sueldo_base(self, sueldo_base):
        self.__sueldo_base = sueldo_base

    def get_sueldo_base(self):
        return self.__sueldo_base

    def set_anio_ingreso(self, anio_ingreso):
        self.__anio_ingreso = anio_ingreso

    def get_anio_ingreso(self):
        return self.__anio_ingreso

    def to_string(self):
        return "No.Trabajador:" + self.__numero_trabajador + " Nombres:" + self.__nombres + " Paterno:" + self.__paterno + " Materno:" + self.__materno + " Horas extra:" + self.__horas_extra + " Sueldo Base:" + self.__sueldo_base + " Año de Ingreso:" + self.__anio_ingreso

    def obtener_sueldo_de_trabajador(self):
        sueldo = Array(4)#Creamos el array donde se guardaran los calculos de suelso por horas extra, sueldo base y prestaciones de forma independiente
        sueldo.set_item(self.__nombres + " " + self.__paterno, 0)#Se guardara en el indice 0 el nombre y apellido del tarbajador.
        sueldo.set_item(float(self.__sueldo_base), 1)#Se guardara en el indice 1 el sueldo base del trabajador.
        sueldo.set_item(276.5 * int(self.__horas_extra), 2)#Se guardar en el inidce 2 la cantidad de sueldo por horas extra.
        sueldo.set_item(((3*float(self.__sueldo_base))/100)*(dt.date.today().year - int(self.__anio_ingreso)), 3)#Se guardara en el indice 3 las prestaciones del trabajador.
        return sueldo

    def antiguedad_trabajador(self):
        antiguedad = dt.date.today().year - int(self.__anio_ingreso)
        return antiguedad
