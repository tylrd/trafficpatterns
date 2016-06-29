from distance import DistanceCalculator
import os
import sys
import datetime


def main():
    origin = os.environ.get("ORIGIN")
    destination = os.environ.get("DESTINATION")
    file_path = os.environ.get("FILE_PATH")
    if origin is None or destination is None or file_path is None:
        print "Set environment variables for ORIGIN, DESTINATION, and FILE_PATH"
        sys.exit(1)

    calculator = DistanceCalculator(origin, destination)
    duration = calculator.calculate()

    f = open(file_path, 'a+')
    f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "," + duration + "\n")
    f.close()


if __name__ == "__main__":
    main()
