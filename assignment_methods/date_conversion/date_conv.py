def date():
    print("\n---Answer 2---")
    import datetime
    date = "19-08-2021" 
    format = "%d-%m-%Y"
    dt_object = datetime.datetime.strptime(date, format)
    print("\nYear using function : ", dt_object.year)
    print("\nYear using slice operator:",date[6:])