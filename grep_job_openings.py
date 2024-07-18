#!/home/yz/myUtils/venv/bin/python3



import time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import csv



def search_career_website(keyword, company_name, company_url, locator_type, locator_value, items_class):

    # Initialize the WebDriver (ChromeDriver in this example)

    driver = webdriver.Chrome()



    try:

        # Open the career page URL

        driver.get(company_url)



        # Wait for the page to load (you might need to adjust the wait time)

        time.sleep(2)



        # Find the search input field and enter the keyword

        search_input = driver.find_element(locator_type, locator_value)

        search_input.send_keys(keyword)

        search_input.send_keys(Keys.RETURN)



        # Wait for the search results to load

        time.sleep(2)



        # Get the content of the search results

        search_results = driver.page_source



        # Process the search results as needed (you might want to use BeautifulSoup here)



        # Example: Extract job titles

        job_titles = driver.find_elements("class name", items_class)

        job_titles_list = [title.text for title in job_titles]



        # Print job titles for demonstration (you can modify this part)

        print(f"Job Titles at {company_name}: {job_titles_list}")



        # Store the results

        result = {

            'company': company_name,

            'job_titles': job_titles_list

        }



    except Exception as e:

        print(f"Error processing {company_name}: {e}")

        result = None



    # Wait for user input before closing the browser

    input("Press Enter to close the browser...")



    # Close the browser window

    driver.quit()



    return result



def save_results_to_file(results, output_file='search_results.csv'):

    # Get the current date and time

    search_date = time.strftime("%Y-%m-%d %H:%M:%S")



    with open(output_file, 'a', newline='', encoding='utf-8') as csvfile:

        fieldnames = ['search_date', 'company', 'job_titles']

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)



        # Check if the file is empty, then write the header

        if csvfile.tell() == 0:

            writer.writeheader()



        for result in results:

            # Append the search date to the result

            result['search_date'] = search_date



            # Write the result to the file

            writer.writerow(result)



if __name__ == "__main__":

    # Customize with your company details

    company_data = [

    	{

            'name': 'Apple',

            'url': 'https://jobs.apple.com/en-us/search?location=united-states-USA',

            'locator_type': 'id',

            'locator_value': 'searchview',

            'items_class': 'table--advanced-search__title'

        },

        {

            'name': 'Meta',

            'url': 'https://www.metacareers.com/jobs',

            'locator_type': 'class name',

            'locator_value': 'x1ejq31n',

            'items_class': 'xh8yej3'

        },

        {

            'name': 'Amazon',

            'url': 'https://www.amazon.jobs/en/search?base_query=accountant&loc_query=USA&latitude=&longitude=&loc_group_id=&invalid_location=false&country=USA&city=&region=&county=',

            'locator_type': 'id',

            'locator_value': 'search_typeahead',

            'items_class': 'job-link'

        },

        # Add more

    ]



    # Replace 'your_keyword' with the keyword you want to search for

    keyword_to_search = 'accountant'



    search_results = []



    for company_info in company_data:

        result = search_career_website(

            keyword_to_search,

            company_info['name'],

            company_info['url'],

            company_info['locator_type'],

            company_info['locator_value'],

            company_info['items_class'],

        )

        if result:

            search_results.append(result)



    if search_results:

        save_results_to_file(search_results)

        print("Search results saved to search_results.csv")

    else:

        print("No matching results found.")

