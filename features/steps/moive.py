from behave import given, when, then

@given(u'I navigate to the genres_details pages')
def nav(context):
    """ 
    Navigate to the genres page
    """
    context.browser.get('http://localhost:5000/')

@when(u'I click on the link to genres details')
def click(context):
    """ 
    Locate the desired hyperlink
    """
    context.browser.find_element_by_partial_link_text('2').click()
    # context.browser.get('http://localhost:5000/genres_details')

@then(u'I should see the order for that genres')
def details(context):
    """ 
    If successful, we should be directed to include all movies of that genre.
    """
    # use print(context.browser.page_source) to aid debugging
    print(context.browser.page_source)
    assert context.browser.current_url == 'http://localhost:5000/same_genres/2'
    assert 'Movie Title: The Hunt' in context.browser.page_source