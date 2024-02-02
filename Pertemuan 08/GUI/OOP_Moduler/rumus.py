class Fahrenheit:
  def __init__(self, suhu):
    self.suhu = suhu

  def get_celcius(self):
    val = (32 - float(self.suhu)) * 5/9
    return val
  
  def get_reamur(self):
    val = (32 - float(self.suhu)) * 4/9
    return val
  
  def get_kelvin(self):
    val = (32 - float(self.suhu)) * 5/9 + 273
    return val

class Reamur:
  def __init__(self, suhu):
    self.suhu = suhu
    
  def get_celcius(self):
    val = float(self.suhu) * 5/4
    return val
  
  def get_fahrenheit(self):
    val = (float(self.suhu) * 9/4) + 32
    return val
  
  def get_kelvin(self):
    val = (float(self.suhu) * 5/4) + 273
    return val

class Kelvin:
  def __init__(self, suhu):
    self.suhu = suhu
    
  def get_celcius(self):
    val = float(self.suhu) - 273
    return val
  
  def get_fahrenheit(self):
    val = 9/5 * (float(self.suhu) - 273) + 32
    return val
  
  def get_reamur(self):
    val = 4/5 * (float(self.suhu) - 273)
    return val