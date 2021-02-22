import re

#byr (Birth Year)
#byr = int('00000001',2) # 1
#iyr (Issue Year)
#iyr = int('00000010',2) # 2
#eyr (Expiration Year)
#eyr = int('00000100',2) # 4
#hgt (Height)
#hgt = int('00001000',2) # 8
#hcl (Hair Color)
#hcl = int('00010000',2) # 16
#ecl (Eye Color)
#ecl = int('00100000',2) # 32
#pid (Passport ID)
#pid = int('01000000',2) # 64
#cid (Country ID)
#cid = int('00000000',2) # 0 optional

#mapper = {'byr': byr,'iyr':iyr,'eyr':eyr,'hgt':hgt,'hcl':hcl,'ecl':ecl,'pid':pid,'cid':cid}

mapper = {'byr': int('00000001',2),'iyr':int('00000010',2),'eyr':int('00000100',2),'hgt':int('00001000',2),'hcl':int('00010000',2),'ecl':int('00100000',2),'pid':int('01000000',2),'cid':int('00000000',2)}
colors = {'amb','blu','brn','gry','grn','hzl','oth'}


def validator(inputkey,inputvalue):
    if inputkey == 'byr':
        if (inputvalue.isdigit()) and (int(inputvalue) >= 1920) and (int(inputvalue) <= 2002):
            return True
        else:
            return False
    elif inputkey == 'iyr':
        if (inputvalue.isdigit()) and (int(inputvalue) >= 2010) and (int(inputvalue) <= 2020):
            return True
        else:
            return False
    elif inputkey == 'eyr':
        if (inputvalue.isdigit()) and (int(inputvalue) >= 2020) and (int(inputvalue) <= 2030):
            return True
        else:
            return False
    elif inputkey == 'hgt':
        if re.match('^[0-9]+(in)',inputvalue):
            inches = inputvalue.replace('in', '')
            if (int(inches) >= 59) and (int(inches) <= 76):
                return True
            else:
                return False
        elif re.match('^[0-9]+(cm)',inputvalue):
            cms = inputvalue.replace('cm', '')
            if (int(cms) >= 150) and (int(cms) <= 193):
                return True
            else:
                return False
        else:
            return False
    elif inputkey == 'hcl':
        if re.match('^#[0-9a-f]{6}$',inputvalue):
            return True
        else:
            return False
    elif inputkey == 'ecl':
        if inputvalue in colors:
            return True
        else:
            return False
    elif inputkey == 'pid':
        if re.match('^[0-9]{9}$', inputvalue):
            return True
        else:
            return False
    else:
        return False


# Using readlines()
file1 = open('aoc04_1_input.txt', 'r')
Lines = file1.readlines()

passport = 0
validspassports = 0

for line in Lines:
    splitline = line.strip().split()
    if len(splitline) !=0:
        for split in splitline:
            fragment = split.strip().split(':')
            if (len(splitline) != 0) :
                if validator(fragment[0],fragment[1]): passport += mapper[fragment[0]]
    else:
        if passport >= 127:
            validspassports += 1
        passport = 0

print(f"Valid total:{validspassports}")