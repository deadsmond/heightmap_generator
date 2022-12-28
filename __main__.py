from functions.CSV_to_STL import convert_csv_to_stl
from functions.SRTM_to_CSV import convert_srtm_to_csv

if __name__ == '__main__':
    filename = "data/N50E015"

    # 1. get height map from https://dwtkns.com/srtm30m/

    # 2. transform hgt to csv
    convert_srtm_to_csv(filename + ".hgt")

    # 3. get height map coordinates from https://dwtkns.com/srtm30m/srtm30m_bounding_boxes.json
    # for N50E015 its item nr 7886 with data:
    # height_map_coordinates = [
    #     (14.99972222, 49.99972222),
    #     (16.00027778, 49.99972222),
    #     (16.00027778, 51.00027778),
    #     (14.99972222, 51.00027778),
    #     (14.99972222, 49.99972222),
    # ]
    #
    # latitude_top = 51.00027778
    # latitude_bottom = 49.99972222

    # 4. generate stl file from csv file
    # convert_csv_to_stl(filename + ".csv")
