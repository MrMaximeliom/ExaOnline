import uuid
import random
import string
def get_random_string(length):
    numbers = 1234567890
    letters = string.ascii_lowercase
    number_and_letters = str(numbers)+letters
    result_str = ''.join(random.choice(number_and_letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

if __name__ == "__main__":
    pass

    # d = '/teacher/user/moayed?csrfmiddlewaretoken=FYlUmXbolBOsxZgOz5jsIo77q6uJUawprlTGmDV4tuD8A5cJ3uEOknOqKZpFa4L3&exam_name=&unique_identifier=&exam_status=Expired&order_by=none&advanced_search=advance&?page=1'
    # if 'page' in d :
    #     s = d.split('?page=',1)
    #     print(s[0]+"?page=1")

