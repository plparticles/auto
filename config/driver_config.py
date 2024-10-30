import os

class DriverConfig:
    driver_env = "chrome"
    driver_path = os.path.join(
        os.path.join(
            os.path.join(os.getcwd(), "/driver"),
            "chromedriver"),
        "")