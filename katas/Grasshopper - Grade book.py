def get_grade(s1, s2, s3):
    grade = 'ABCDF'
    if (s1 + s2 + s3) >= 270:
        return grade[0]
    elif 240 <= (s1 + s2 + s3) < 270:
        return grade[1]
    elif 210 <= (s1 + s2 + s3) < 240:
        return grade[2]
    elif 180 <= (s1 + s2 + s3) < 210:
        return grade[3]
    else:
        return grade[4]