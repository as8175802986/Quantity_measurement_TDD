from Quantity_measurement_system.quantity_measurement import Quantity_measurement


class Test:
    @staticmethod
    def test_feet_to_inch():
        result1 = Quantity_measurement.feet_to_inch_value(1)
        result2 = Quantity_measurement.feet_to_inch_value(1)

        assert (result1 == result2)

    @staticmethod
    def test_inch_to_feet():
        result1 = Quantity_measurement.inch_to_feet_value(12)
        expected = 1
        assert (result1 == expected)

    @staticmethod
    def test_km_to_meter():
        result1 = Quantity_measurement.km_to_meter(1)
        expected = 1000
        assert (result1 == expected)

    @staticmethod
    def test_meter_to_kms():
        result1 = Quantity_measurement.meter_to_kms(1500)
        expected = 1.5
        assert (result1 == expected)

    @staticmethod
    def test_fahrenheit_celcius():
        result = Quantity_measurement.fahrenheit_to_celcius(50)
        expected = 10
        assert (result == expected)

    @staticmethod
    def test_length_comparison_equal():
        result1 = Quantity_measurement.length_comparison(5, "feet")
        result2 = Quantity_measurement.length_comparison(60, "inch")
        assert (result1 == result2)

    @staticmethod
    def test_length_comparison_not_equal():
        result1 = Quantity_measurement.length_comparison(5, "feet")
        result2 = Quantity_measurement.length_comparison(48, "inch")
        assert (result1 != result2)

    @staticmethod
    def test_distance_comparison():
        result1 = Quantity_measurement.distance_comparison(5000, "meter")
        result2 = Quantity_measurement.distance_comparison(5000, "meter")
        assert (result1 == result2)

    @staticmethod
    def test_distance_comparison_not_equal():
        result1 = Quantity_measurement.distance_comparison(4, "km")
        result2 = Quantity_measurement.distance_comparison(5000, "meter")
        assert (result1 != result2)

    @staticmethod
    def test_temperature_comparison():
        result1 = Quantity_measurement.temperature_comparison(0, "celcius")
        result2 = Quantity_measurement.temperature_comparison(32, "fahrenheit")
        assert (result1 == result2)

    @staticmethod
    def test_temperature_comparison_not_equal():
        result1 = Quantity_measurement.temperature_comparison(0, "celcius")
        result2 = Quantity_measurement.temperature_comparison(50, "fahrenheit")
        assert (result1 != result2)

    @staticmethod
    def test_length_addition_in_feet():
        result = Quantity_measurement.length_addition_in_feet(60, "inch", 5, "feet")
        expected = 10
        assert (result == expected)

    @staticmethod
    def test_distance_addition_in_km():
        result = Quantity_measurement.distance_addition_in_km(1000, "meter", 5, "km")
        expected = 6
        assert (result == expected)

    @staticmethod
    def test_temperature_addition_in_celcius():
        result = Quantity_measurement.temperature_addition_in_celcius(50, "fahrenheit", 10, "celcius")
        expected = 20
        assert (result == expected)


if __name__ == '__main__':
    Test()
