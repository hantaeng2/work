lead = '지역: 서울, 나이: 21, 성명: 한정민'
lead_items = lead.split(',')
dict_lead = dict()

for lead_item in lead_items:
    item_key_value = lead_item.split(':')
    item_key = item_key_value[0].strip()
    item_value = item_key_value[1].strip()
    if item_value.isnumeric():
        item_value = int(item_value)
    dict_lead[item_key] = item_value #딕셔너리에 key, value 배정 방법
    
print(dict_lead)
print(lead_items)
print(item_key_value)

value = input('값을 입력하십시오.')
print(f'입력하신 값은 {value}입니다.')