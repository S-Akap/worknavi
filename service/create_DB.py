import random
from .models import Sex, Requirement, Citizenship, RegisteredStaff
try:
    from faker import Factory
    import requests
    import random
except:
    import sys
    sys.exit()

ADDRESS_API_URL = 'http://geoapi.heartrails.com/api/json?method=searchByGeoLocation'


class CreateAddress():
    def __init__(self, max_lat=45.33, min_lat=30.59, max_lon=145.48, min_lon=129.34):
        self.max_lat = max_lat  # 最大緯度
        self.min_lat = min_lat  # 最小緯度
        self.max_lon = max_lon  # 最大経度
        self.min_lon = min_lon  # 最小経度
        self.add_list = []  # 実在する住所を保存

    def make_search_num(self) -> tuple:
        # 緯度生成
        lat = round(random.uniform(self.min_lat, self.max_lat), 6)
        # 経度生成
        lon = round(random.uniform(self.min_lon, self.max_lon), 6)
        return lat, lon

    def get_address_data(self) -> dict:
        lat, lon = self.make_search_num()
        try:
            params = {'method': 'searchByGeoLocation', 'x': lon, 'y': lat}
            data = requests.get(ADDRESS_API_URL, params=params)
        except:
            pass
        else:
            return data.json()['response']

    def add_data(self, data_dict: dict):
        if 'error' in data_dict:  # 住所なしの時
            return

        try:
            x = data_dict['location']
            for i in range(2):  # 先頭2つをadd_listに追加
                add_data = x[i]
                self.add_list.append(
                    [
                        add_data['postal'],
                        add_data['prefecture'],
                        add_data['city'],
                        add_data['town']
                    ]
                )
        except:
            return

    def main(self):
        for i in range(20):
            data_dict = self.get_address_data()
            self.add_data(data_dict=data_dict)

    def return_add_list(self):
        return self.add_list


class CreateRegisteredStaff:
    def __init__(self):
        self.num = int(input('実行回数 ->'))
        self.sex_lis = [
            Sex.objects.get(sex='man'),
            Sex.objects.get(sex='woman'),
        ]
        self.requirement_lis = [
            Requirement.objects.get(requirement='nothing'),
            None
        ]
        self.citizenship_lis = [
            Citizenship.objects.get(citizenship='japan'),
            None
        ]
        self.hourly_pay_lis = [
            1300,
            1350,
            1400,
            1450,
            1500,
            1550,
            1600
        ]
        self.requirement_lis_w = [7, 3]
        self.sex_lis_w = [6, 4]
        self.citizenship_lis_w = [8, 2]
        self.hourly_pay_lis_w = [3, 4, 6, 9, 7, 3, 2]

    def create(self):
        fake = Factory.create('ja-JP')
        name = fake.name()
        sex = random.choices(self.sex_lis, weights=self.sex_lis_w, k=1)[0]
        age = random.randint(27, 64)
        requirement = None
        hourly_pay = None
        citizenship = None
        residence = None
        is_contact = False

        if random.randint(1, 3) % 2 == 1:
            hourly_pay = random.choices(
                self.hourly_pay_lis, weights=self.hourly_pay_lis_w, k=1)[0]

        if random.randint(1, 3) % 2 == 1:
            citizenship = random.choices(
                self.citizenship_lis, weights=self.citizenship_lis_w, k=1)[0]

        if random.randint(1, 3) % 2 == 1:
            requirement = random.choices(
                self.requirement_lis, weights=self.requirement_lis_w, k=1)[0]

        if random.randint(1, 3) % 2 == 1:
            is_contact = True

        if not requirement:
            if not hourly_pay:
                if not citizenship:
                    if not residence:
                        RegisteredStaff.objects.create(
                            name=name, sex=sex, age=age, is_contact=is_contact)
                    else:
                        RegisteredStaff.objects.create(
                            name=name, sex=sex, age=age, residence=residence, is_contact=is_contact)
                else:
                    if not residence:
                        RegisteredStaff.objects.create(
                            name=name, sex=sex, age=age, citizenship=citizenship, is_contact=is_contact)
                    else:
                        RegisteredStaff.objects.create(
                            name=name, sex=sex, age=age, citizenship=citizenship, residence=residence, is_contact=is_contact)
            else:
                if not citizenship:
                    if not residence:
                        RegisteredStaff.objects.create(
                            name=name, sex=sex, age=age, hourly_pay=hourly_pay, is_contact=is_contact)
                    else:
                        RegisteredStaff.objects.create(
                            name=name, sex=sex, age=age, hourly_pay=hourly_pay, residence=residence, is_contact=is_contact)
                else:
                    if not residence:
                        RegisteredStaff.objects.create(
                            name=name, sex=sex, age=age, hourly_pay=hourly_pay, citizenship=citizenship, is_contact=is_contact)
                    else:
                        RegisteredStaff.objects.create(name=name, sex=sex, age=age, hourly_pay=hourly_pay,
                                                       citizenship=citizenship, residence=residence, is_contact=is_contact)
        else:
            if not hourly_pay:
                if not citizenship:
                    if not residence:
                        RegisteredStaff.objects.create(
                            name=name, sex=sex, age=age, requirement=requirement, is_contact=is_contact)
                    else:
                        RegisteredStaff.objects.create(
                            name=name, sex=sex, age=age, requirement=requirement, residence=residence, is_contact=is_contact)
                else:
                    if not residence:
                        RegisteredStaff.objects.create(
                            name=name, sex=sex, age=age, requirement=requirement, citizenship=citizenship, is_contact=is_contact)
                    else:
                        RegisteredStaff.objects.create(name=name, sex=sex, age=age, requirement=requirement,
                                                       citizenship=citizenship, residence=residence, is_contact=is_contact)
            else:
                if not citizenship:
                    if not residence:
                        RegisteredStaff.objects.create(
                            name=name, sex=sex, age=age, requirement=requirement, hourly_pay=hourly_pay, is_contact=is_contact)
                    else:
                        RegisteredStaff.objects.create(
                            name=name, sex=sex, age=age, requirement=requirement, hourly_pay=hourly_pay, residence=residence, is_contact=is_contact)
                else:
                    if not residence:
                        RegisteredStaff.objects.create(name=name, sex=sex, age=age, requirement=requirement,
                                                       hourly_pay=hourly_pay, citizenship=citizenship, is_contact=is_contact)
                    else:
                        RegisteredStaff.objects.create(name=name, sex=sex, age=age, requirement=requirement,
                                                       hourly_pay=hourly_pay, citizenship=citizenship, residence=residence, is_contact=is_contact)
