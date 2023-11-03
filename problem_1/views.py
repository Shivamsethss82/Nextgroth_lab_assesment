from django.shortcuts import render

# Create your views here.

import re
from django.http import JsonResponse

def extract_numbers(request):
    input_text = '{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}'

    regex_pattern = r'"id":(\d+)'
    extracted_numbers = re.findall(regex_pattern, input_text)

    # Convert the extracted numbers to integers
    extracted_numbers = [int(number) for number in extracted_numbers]

    # Return the extracted numbers as a JSON response
    return JsonResponse({'extracted_numbers': extracted_numbers})