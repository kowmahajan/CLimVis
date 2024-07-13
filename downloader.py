import cdsapi
for year in range(2019, 2023):
    
    c = cdsapi.Client()

    c.retrieve(
        'satellite-fire-burned-area',
        {
            'origin': 'c3s',
            'sensor': 'olci',
            'variable': 'grid_variables',
            'version': '1_1',
            'year': str(year),
            'month': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
            ],
            'nominal_day': '01',
            'format': 'zip',
        },
        'download' + str(year) + '.zip')