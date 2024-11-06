import requests
from datetime import datetime, timedelta
from behave import *
from config import KEY

# Generate string in YYYY-MM-DD format for yesterdays date
yesterday = datetime.strftime(datetime.now()-timedelta(1), '%Y-%m-%d')

@given('I create a request to NASA API for APoD of date "{date}"')
def step_impl(context, date):
    if date == "YESTERDAY": date = yesterday
    params = {'api_key':KEY,'date':date}
    response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
    context.response = response

@when('I should receive an OK (200) response')
def step_impl(context):
    assert context.response.status_code == 200

@then('Response should contain following keys: "{keys}"')
def step_impl(context, keys):
    context.json_content = context.response.json()
    for key in keys.split(", "):
        assert key in context.json_content, f"Response does not contain the key: {key}"

@then('Media type (media_type) should be either image or video')
def step_impl(context):
    assert context.json_content['media_type'] in ['image', 'video']