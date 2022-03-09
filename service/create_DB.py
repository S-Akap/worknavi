from faker import Factory
import random
from .models import Sex, Requirement, Citizenship, RegisteredStaff

sex_lis, sex_lis_w = [
    Sex.objects.get(sex='man'),
    Sex.objects.get(sex='woman'),
], [
    6,
    4
]

requirement_lis, requirement_lis_w = [
    Requirement.objects.get(requirement='nothing'),
    None
], [
    7,
    3
]

citizenship_lis, citizenship_lis_w = [
    Citizenship.objects.get(citizenship='japan'),
    None
], [
    8,
    2
]

hourly_pay_lis, hourly_pay_lis_w = [
    1300,
    1350,
    1400,
    1450,
    1500,
    1550,
    1600
], [
    3,
    4,
    6,
    9,
    7,
    3,
    2
]
fake = Factory.create('ja-JP')


def do():
    name = fake.name()
    sex = random.choices(sex_lis, weights=sex_lis_w, k=1)[0]
    age = random.randint(27, 64)
    requirement = None
    hourly_pay = None
    citizenship = None
    residence = None
    is_contact = False

    if random.randint(1, 3) % 2 == 1:
        hourly_pay = random.choices(
            hourly_pay_lis, weights=hourly_pay_lis_w, k=1)[0]

    if random.randint(1, 3) % 2 == 1:
        citizenship = random.choices(
            citizenship_lis, weights=citizenship_lis_w, k=1)[0]

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
