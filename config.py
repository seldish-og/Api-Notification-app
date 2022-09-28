# glpat-PQuF623u4Hy1UUXJdQiu
# import requests

# headers = {'Accept': '*/*',
#            'Accept-Encoding': 'gzip, deflate, br',
#            'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
#            'Connection': 'keep-alive',
#            'Cookie': 'ring=6bfbfe9CshCa84%2FgeTbNdeD3GQRAQ0a3; cookie_cityid=48; cookie_regionid=40; my_geo=40; dr_df=1; _gid=GA1.2.265274495.1663841688; segSession=ImJlNWFlMzg3Zjk2MTI5MzAyM2ZhYmJjOTQ2MzY1MDhjbm90QXV0aDZiZmJmZTlDc2hDYTg0XC9nZVRiTmRlRDNHUVJBUTBhMyJfYTZjMzhkMzljMzExOGE0ODA2OTMzNTU5ZTA0YjJlMjE; apple-pay-available=0; google-pay-available=1; PHPSESSID=3b4271926395976e9ec51dd6e8af75f2; city=65857; signFrom=drom; _ga_C9HGECLFK7=GS1.1.1663843159.1.1.1663843205.0.0.0; _ga_W0TFWNSLJ7=GS1.1.1663843159.1.1.1663843205.0.0.0; _ga=GA1.2.875769932.1663841688; k6W=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjM4NTczOTcsImtpZCI6ImRMQ2MxZUFvdV9kZkwteFVWMmdiWHlUM0JnWnAyYVNFSS00UGdIVzlkNEkiLCJwcm9qZWN0IjoiZHJvbSIsInN1YiI6InI6NmJmYmZlOUNzaENhODQvZ2VUYk5kZUQzR1FSQVEwYTMifQ.D69_PF8KBFuTCWHUy44C4Yn_iJ4H_tlukDWSJqV4od1NOQfoQIO5cMnwmF8o7ltSutz5BwIAz7xzXynsTQh0rdgLgfE83gI2Tg0hGA3mzXpdqIEnhvGiUPOUmqmEMqGx98s-3dIC_2jktDCpn-CEIqVzH6TDN1kIZQ8saaTrvLk; _gat=1',
#            'Host': 'www.drom.ru',
#            'Origin': 'https://kaluga.drom.ru',
#            'Referer': 'https://kaluga.drom.ru/toyota/proace/47954495.html',
#            'sec-ch-ua': '''"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"''',
#            'sec-ch-ua-mobile': '?0',
#            'sec-ch-ua-platform': "Linux",
#            'Sec-Fetch-Dest': 'empty',
#            'Sec-Fetch-Mode': 'cors',
#            'Sec-Fetch-Site': 'same-site',
#            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
#            }
# url = "https://www.drom.ru/api/sales/bulls/47954495/contacts?contactData=SzvI5Dh67_t2rec208S8bJn8BB2JZeFZNFY31CCzlH4SvBIi2nOIbunYNMNlR5fRLrI&regionIp=3579283701&token=MTY2Mzg1NDQwOXw0Nzk1NDQ5NXw2YmZiZmU5Q3NoQ2E4NC9nZVRiTmRlRDNHUVJBUTBhM3wxMDQ5OTI3MDY4.efe6da2ea3e50174fedef3726f60067c2832ad208816c0b828e1f3ccadb7c344_dTk3Q3R1eXMzS3Mya0U3UXVYeHNUdnNrM0t5dHR0eFF1RTZnSXVzZmt0U3RrRTZpdUVSRUY3c2lGdVFpb3R2dFZKREkwdlNmc3RTaTNFSzRWS3I0MHZyT1RFZHNWQzdXdHRyRHQ3NGlvVmRGVm03RnRoeHV0VmRrdXU0V1ZsN0N0SkRuMHZ5RkZ1cnMzN3NLdENEdHNjPT0%3D.dXpEblQ3eU9vdnl1b004U3Uycm5rdnlpb3V5MlZDN2d1ekRJa3Y4Z3VLdjJWN3NvdXpLdzN6dmtpVVNpVHpLTzBWS3IzSjlFQVY3MjMxeG5WSktFMjdXRUYyNjB0Qzd5VnY0cEZ1OGpUTTY4dEM2eTB0U2FjYT09&dust=VGQ8wPQs&captchaToken=03AIIukzga41KIz7ACzNdqDuGjcUk-qc5baT9BaIwiB_MT4HaZB7r3ATuaIiQiRdOInKa8DZZZcB9tFGkTPQVNj_Vl6dY0yncDXf3lx_d6YbgBRlWS_JXck-byXnDWQiurK2NojnDqjIcDMGQdYtHALaynu-tlkxOJwwOfLH_FGSJQbMcX9Ql6FlhweCDQpiToj8SFkIXK2U8U7O6IG7nBg6IA_g-VcRKzDLUur_izNfFpMX-3geDELs74o46oOmD1OQmNzHpeVxa69_Q6N_-m1LhDibPt_Mx8pl-tHOV1w57GMbU7kbauRJBbYyRK-epsDfp_9BaImFN8yJ4b1LSPw_RjKphUOoMGMoxeMhZ2QqgHGGTBasHVZUttdIVsGrOF-bFODXtY5nMQk1GcUkQA00soNL9-oZdxVxwtp9QmHbOYR6cJZvLyjJc3TSECphIFe-L4HKa0qYTez6R3NREJBTZi10Ady-J8dBzvHuYcJgy1slEAWjDojaTtns70JJpSRpMZ_eHwR8P4Jkkz7bRSh4Fjl6sEpb4b5w"


# r = requests.get(url=url, headers=headers)
# print(str(r.content))
