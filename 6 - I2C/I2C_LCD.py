import I2C_LCD_driver


mylcd = I2C_LCD_driver.lcd()

mylcd.lcd_display_string("Hello", 1)

mylcd.lcd_display_string("My name is Sid", 2)
