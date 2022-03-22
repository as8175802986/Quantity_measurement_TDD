import enum


class ExceptionType(enum.Enum):
    VALUE_EXCEPTION = "Given value is not proper"
    UNIT_EXCEPTION = "Given unit is not proper"


class InvalidTypeException(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return f"{self.message}"


class Quantity_measurement:

    @staticmethod
    def inch_to_feet_value(value):
        """
            Description:
                Function to convert inch to feet
            Parameter:
                value
            Return:
                value
        """
        if not value >= 0:
            raise InvalidTypeException(ExceptionType.VALUE_EXCEPTION.value)
        else:
            var = value / 12
            print(var, "feet")
        return var

    @staticmethod
    def feet_to_inch_value(value):
        """
            Description:
                Function to convert feet_to_inch
            Parameter:
                value
            Return:
                value
        """
        if not value >= 0:
            raise InvalidTypeException(ExceptionType.VALUE_EXCEPTION.value)
        else:
            var = value * 12
            print(var, "inch")
        return var

    @staticmethod
    def km_to_meter(value):
        """
                Description:
                    Function to convert km_to_meter
                Parameter:
                    value
                Return:
                    datatype
        """
        if not value >= 0:
            raise InvalidTypeException(ExceptionType.VALUE_EXCEPTION.value)
        else:
            var = value * 1000
        return var

    @staticmethod
    def meter_to_kms(value):
        """
                Description:
                    Function to convert meter_to_kms
                Parameter:
                    value
                Return:
                    datatype
        """
        if not value >= 0:
            raise InvalidTypeException(ExceptionType.VALUE_EXCEPTION.value)
        else:
            var = value / 1000
        return var

    @staticmethod
    def fahrenheit_to_celcius(value):
        """
            Description:
                Function to convert fahrenheit_to_celcius
            Parameter:
                 value
                Return:
                :var
                    """
        if not value >= 0:
            raise InvalidTypeException(ExceptionType.VALUE_EXCEPTION.value)
        else:
            var = ((value - 32) * (5 / 9))
        return var

    @staticmethod
    def celcius_fahrenheit(value):
        """
                    Description:
                        Function to convert fahrenheit_to_celcius
                    Parameter:
                         value
                        Return:
                        :var
                            """
        if not value >= 0:
            raise InvalidTypeException(ExceptionType.VALUE_EXCEPTION.value)
        else:
            var = (value * 1.8) + 32
        return var

    @staticmethod
    def length_comparison(value, unit1):
        """
                    Description:
                        Function to convert and compare length inch_to_feet
                    Parameter:
                         value,unit
                        Return:
                        :var
                            """
        if unit1 == "feet":
            return value
        var = Quantity_measurement.inch_to_feet_value(value)
        return var

    @staticmethod
    def length_addition_in_feet(value1, unit1, value2, unit2):
        """
                    Description:
                        Function to  covert and add length in feet
                       Parameter:
                         value1, unit1, value2, unit2
                        Return:
                        :l
                            """
        l1 = Quantity_measurement.length_comparison(value1, unit1)
        l2 = Quantity_measurement.length_comparison(value2, unit2)
        l = l1 + l2
        print(l, "feet")
        return l

    @staticmethod
    def distance_comparison(value, unit):
        """
             Description:
                 Function to compare and convert distance in km
             Parameter:
                 value, unit
               Return:
                   :var
                         """
        if unit == "km":
            return value
        var = Quantity_measurement.meter_to_kms(value)
        # print(var, unit)
        return var

    @staticmethod
    def distance_addition_in_km(value1, unit1, value2, unit2):
        """
                            Description:
                                Function to  covert and add distance in km
                               Parameter:
                                 value1, unit1, value2, unit2
                                Return:
                                :l
                                    """
        l1 = Quantity_measurement.distance_comparison(value1, unit1)
        l2 = Quantity_measurement.distance_comparison(value2, unit2)
        l = l1 + l2
        print(l, "km")
        return l

    @staticmethod
    def temperature_comparison(value, unit):
        """
                     Description:
                         Function to compare and convert temperature in celcius
                     Parameter:
                         value, unit
                       Return:
                           :var
                                 """
        if unit == "celcius":
            return value
        var= Quantity_measurement.fahrenheit_to_celcius(value)
        # var = ((value - 32) * (5 / 9))
        print(var, unit)
        return var

    @staticmethod
    def temperature_addition_in_celcius(value1, unit1, value2, unit2):
        """
                            Description:
                                Function to  covert and add temperature in celcius
                               Parameter:
                                 value1, unit1, value2, unit2
                                Return:
                                :l
                                    """
        l1 = Quantity_measurement.temperature_comparison(value1, unit1)
        l2 = Quantity_measurement.temperature_comparison(value2, unit2)
        l = l1 + l2
        print(l, "celcius")
        return l


