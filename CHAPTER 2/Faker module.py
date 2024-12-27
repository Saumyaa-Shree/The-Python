# MODULE TO GENERATE FAKE DATA FOR THE DATASET

from faker import Faker
fake=Faker()
print(fake.name())
print(fake.address())
print(fake.first_name())
print(fake.last_name())
print(fake.city())
print(fake.state())
print(fake.postcode())
print(fake.country())
print(fake.text())#sentence(),word(),paragraph()
print(fake.phone_number())#email(),domain_name(),url,ipv4(),ipv6()- INTERNET RELATED INFO
print(fake.date_time())#date(),time(),iso8601(),unix_time()- standarized date formats
print(fake.credit_card_number())#FINANCIAL DATA- card_number(),card_provider(),card_type(), card_info()
print(fake.ssn())#SOCIAL SECURITY NUMBER

# YOU CAN GET ANY FAKE AND RANDOMIZED INFO AND DATA USING THIS MODULE
# CHATGPT USE KRO TO CHK ITS OTHER INFINITE FUNCTIONS
""" Applications- 1)for testing softwares using fake data
2)stress testing a database by populating it with loads of fake user info
3)replacing real data with fake for privacy
4)data analysis and visualisation- fake trends and patterns, creating prototypes
5)e-commerce platforms testing - generating fake orders, customers, products
6)game dev- to create names and attributes of random npc
7)API testing???????
8)web dev- need for sample user data to test features"""